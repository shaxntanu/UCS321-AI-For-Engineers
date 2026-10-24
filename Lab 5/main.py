"""Run K-means and DBSCAN clustering on the country development dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


LAB_DIR = Path(__file__).resolve().parent
DATA_PATH = LAB_DIR / "Country-data.csv"
FIGURES_DIR = LAB_DIR / "figures"
ASSIGNMENTS_PATH = LAB_DIR / "country_cluster_assignments.csv"

RANDOM_STATE = 42
PCA_VARIANCE_TO_RETAIN = 0.95
DBSCAN_EPS = 1.1
DBSCAN_MIN_SAMPLES = 4


def load_country_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the data and separate country names from numeric features."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_PATH.name}. Keep it in the same folder as main.py."
        )

    country_data = pd.read_csv(DATA_PATH)
    if "country" not in country_data.columns:
        raise ValueError("The dataset must contain a 'country' column.")

    features = country_data.drop(columns="country")
    if not all(pd.api.types.is_numeric_dtype(dtype) for dtype in features.dtypes):
        raise ValueError("All columns apart from 'country' must be numeric.")
    if features.isna().any().any():
        raise ValueError("The numeric features contain missing values.")

    return country_data, features


def find_kmeans_cluster_count(pca_features):
    """Compare a small range of K values using inertia and silhouette score."""
    inertia_by_k = {}
    silhouette_by_k = {}

    for k in range(1, 11):
        model = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=20)
        labels = model.fit_predict(pca_features)
        inertia_by_k[k] = model.inertia_

        if k >= 2:
            silhouette_by_k[k] = silhouette_score(pca_features, labels)

    best_k = max(silhouette_by_k, key=silhouette_by_k.get)
    return best_k, inertia_by_k, silhouette_by_k


def save_pca_variance_plot(pca: PCA) -> None:
    """Save a plot showing individual and cumulative explained variance."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    component_numbers = range(1, len(pca.explained_variance_ratio_) + 1)
    cumulative_variance = pca.explained_variance_ratio_.cumsum()

    figure, axis = plt.subplots(figsize=(7, 4.5))
    axis.bar(
        component_numbers,
        pca.explained_variance_ratio_,
        color="steelblue",
        label="Individual component",
    )
    axis.plot(
        component_numbers,
        cumulative_variance,
        color="darkorange",
        marker="o",
        label="Cumulative variance",
    )
    axis.axhline(
        PCA_VARIANCE_TO_RETAIN,
        color="gray",
        linestyle="--",
        label=f"{PCA_VARIANCE_TO_RETAIN:.0%} target",
    )
    axis.set_title("PCA explained variance")
    axis.set_xlabel("Principal component")
    axis.set_ylabel("Explained variance ratio")
    axis.set_xticks(list(component_numbers))
    axis.set_ylim(0, 1.05)
    axis.grid(axis="y", alpha=0.25)
    axis.legend()

    figure.tight_layout()
    figure.savefig(FIGURES_DIR / "pca_explained_variance.png", dpi=180)
    plt.close(figure)


def save_kmeans_selection_plot(inertia_by_k, silhouette_by_k, best_k) -> None:
    """Save elbow and silhouette plots used to choose K."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    axes[0].plot(list(inertia_by_k), list(inertia_by_k.values()), marker="o")
    axes[0].set_title("K-means elbow method (PCA features)")
    axes[0].set_xlabel("Number of clusters (K)")
    axes[0].set_ylabel("Inertia")
    axes[0].set_xticks(list(inertia_by_k))
    axes[0].grid(alpha=0.25)

    axes[1].bar(list(silhouette_by_k), list(silhouette_by_k.values()), color="steelblue")
    axes[1].axvline(best_k, color="darkorange", linestyle="--", label=f"Selected K = {best_k}")
    axes[1].set_title("Silhouette score by K")
    axes[1].set_xlabel("Number of clusters (K)")
    axes[1].set_ylabel("Silhouette score")
    axes[1].set_xticks(list(silhouette_by_k))
    axes[1].legend()
    axes[1].grid(axis="y", alpha=0.25)

    figure.tight_layout()
    figure.savefig(FIGURES_DIR / "kmeans_model_selection.png", dpi=180)
    plt.close(figure)


def save_cluster_plot(pca: PCA, pca_features, kmeans_labels, dbscan_labels) -> None:
    """Plot the assignments on the first two principal components."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True, sharey=True)
    x_values = pca_features[:, 0]
    y_values = pca_features[:, 1]

    for cluster_id in sorted(set(kmeans_labels)):
        members = kmeans_labels == cluster_id
        axes[0].scatter(
            x_values[members],
            y_values[members],
            s=34,
            alpha=0.75,
            label=f"Cluster {cluster_id}",
        )
    axes[0].set_title("K-means")

    for cluster_id in sorted(set(dbscan_labels)):
        members = dbscan_labels == cluster_id
        if cluster_id == -1:
            axes[1].scatter(
                x_values[members],
                y_values[members],
                s=38,
                marker="x",
                color="gray",
                alpha=0.75,
                label="Noise (-1)",
            )
        else:
            axes[1].scatter(
                x_values[members],
                y_values[members],
                s=34,
                alpha=0.75,
                label=f"Cluster {cluster_id}",
            )
    axes[1].set_title(f"DBSCAN (eps={DBSCAN_EPS}, min_samples={DBSCAN_MIN_SAMPLES})")

    for axis in axes:
        axis.set_xlabel(
            f"PC1 ({pca.explained_variance_ratio_[0] * 100:.1f}% variance)"
        )
        axis.grid(alpha=0.2)
        axis.legend(fontsize=8)
    axes[0].set_ylabel(
        f"PC2 ({pca.explained_variance_ratio_[1] * 100:.1f}% variance)"
    )

    figure.suptitle("Country clusters (models use the retained PCA components)")
    figure.tight_layout()
    figure.savefig(FIGURES_DIR / "cluster_assignments.png", dpi=180)
    plt.close(figure)


def print_cluster_sizes(method_name: str, labels) -> None:
    """Print cluster sizes, including DBSCAN's noise label when present."""
    print(f"\n{method_name} cluster sizes:")
    for cluster_id, count in pd.Series(labels).value_counts().sort_index().items():
        cluster_name = "Noise (-1)" if cluster_id == -1 else f"Cluster {cluster_id}"
        print(f"  {cluster_name}: {count}")


def main() -> None:
    country_data, features = load_country_data()
    scaled_features = StandardScaler().fit_transform(features)
    pca = PCA(n_components=PCA_VARIANCE_TO_RETAIN, random_state=RANDOM_STATE)
    pca_features = pca.fit_transform(scaled_features)

    best_k, inertia_by_k, silhouette_by_k = find_kmeans_cluster_count(pca_features)
    kmeans = KMeans(n_clusters=best_k, random_state=RANDOM_STATE, n_init=20)
    kmeans_labels = kmeans.fit_predict(pca_features)
    kmeans_silhouette = silhouette_score(pca_features, kmeans_labels)

    dbscan_labels = DBSCAN(
        eps=DBSCAN_EPS,
        min_samples=DBSCAN_MIN_SAMPLES,
    ).fit_predict(pca_features)

    save_pca_variance_plot(pca)
    save_kmeans_selection_plot(inertia_by_k, silhouette_by_k, best_k)
    save_cluster_plot(pca, pca_features, kmeans_labels, dbscan_labels)

    results = country_data[["country"]].copy()
    results["kmeans_cluster"] = kmeans_labels
    results["dbscan_cluster"] = dbscan_labels
    results.to_csv(ASSIGNMENTS_PATH, index=False)

    dbscan_cluster_count = len(set(dbscan_labels) - {-1})
    dbscan_noise_count = int((dbscan_labels == -1).sum())

    print(f"Loaded {len(country_data)} countries and {features.shape[1]} numeric features.")
    print(
        f"PCA retained {pca.n_components_} components "
        f"({pca.explained_variance_ratio_.sum():.1%} of variance)."
    )
    print(f"Selected K for K-means: {best_k}")
    print(f"K-means silhouette score: {kmeans_silhouette:.3f}")
    print(f"DBSCAN clusters: {dbscan_cluster_count}")
    print(f"DBSCAN noise points: {dbscan_noise_count}")
    print_cluster_sizes("K-means", kmeans_labels)
    print_cluster_sizes("DBSCAN", dbscan_labels)
    print(f"\nSaved figures to: {FIGURES_DIR}")
    print(f"Saved assignments to: {ASSIGNMENTS_PATH.name}")


if __name__ == "__main__":
    main()
