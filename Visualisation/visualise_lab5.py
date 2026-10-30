"""Generate a compact PCA, K-means, and DBSCAN overview for Lab 5."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


ROOT_DIR = Path(__file__).resolve().parent.parent
LAB_DIR = ROOT_DIR / "Lab 5"
OUTPUT_PATH = LAB_DIR / "figures" / "pca_clustering_overview.png"
RANDOM_STATE = 42
PCA_VARIANCE_TO_RETAIN = 0.95
DBSCAN_EPS = 1.1
DBSCAN_MIN_SAMPLES = 4


def main() -> None:
    data = pd.read_csv(LAB_DIR / "Country-data.csv")
    features = data.drop(columns="country")
    scaled = StandardScaler().fit_transform(features)
    pca = PCA(n_components=PCA_VARIANCE_TO_RETAIN, random_state=RANDOM_STATE)
    pca_features = pca.fit_transform(scaled)

    assignments = pd.read_csv(LAB_DIR / "country_cluster_assignments.csv")
    assignments = data[["country"]].merge(
        assignments, on="country", how="left", validate="one_to_one"
    )
    if assignments[["kmeans_cluster", "dbscan_cluster"]].isna().any().any():
        raise ValueError("Cluster assignments are incomplete. Run Lab 5/main.py first.")
    kmeans_labels = assignments["kmeans_cluster"].to_numpy(dtype=int)
    dbscan_labels = assignments["dbscan_cluster"].to_numpy(dtype=int)
    best_k = len(set(kmeans_labels))

    figure, axes = plt.subplots(1, 3, figsize=(15.5, 4.9))
    components = range(1, pca.n_components_ + 1)
    cumulative_variance = pca.explained_variance_ratio_.cumsum()
    axes[0].bar(components, pca.explained_variance_ratio_, color="#398a84", label="Individual")
    axes[0].plot(components, cumulative_variance, color="#e07a3f", marker="o", linewidth=2, label="Cumulative")
    axes[0].axhline(
        PCA_VARIANCE_TO_RETAIN,
        color="#59666b",
        linestyle="--",
        linewidth=1,
        label="95% target",
    )
    axes[0].set(
        title=f"PCA retains {pca.n_components_} components",
        xlabel="Principal component",
        ylabel="Explained variance",
    )
    axes[0].set_xticks(list(components))
    axes[0].set_ylim(0, 1.05)
    axes[0].legend(fontsize=8, frameon=False)
    axes[0].grid(axis="y", alpha=0.2)

    x_values, y_values = pca_features[:, 0], pca_features[:, 1]
    for axis, labels, title in (
        (axes[1], kmeans_labels, f"K-means (K={best_k})"),
        (axes[2], dbscan_labels, f"DBSCAN (eps={DBSCAN_EPS}, min={DBSCAN_MIN_SAMPLES})"),
    ):
        for cluster_id in sorted(set(labels)):
            members = labels == cluster_id
            if cluster_id == -1:
                axis.scatter(
                    x_values[members], y_values[members], marker="x", s=38,
                    color="#4c5661", alpha=0.8, label=f"Noise ({members.sum()})"
                )
            else:
                axis.scatter(
                    x_values[members], y_values[members], s=33, alpha=0.78,
                    label=f"Cluster {cluster_id} ({members.sum()})"
                )
        axis.set(
            title=title,
            xlabel=f"PC1 ({pca.explained_variance_ratio_[0]:.1%})",
            ylabel=f"PC2 ({pca.explained_variance_ratio_[1]:.1%})",
        )
        axis.grid(alpha=0.2)
        axis.legend(fontsize=7, frameon=False, loc="best")

    figure.suptitle("Country development indicators: PCA projection and cluster assignments", fontsize=14)
    figure.tight_layout()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(figure)
    print(
        f"Loaded saved K={best_k} cluster labels; PCA retained {pca.n_components_} "
        f"components ({pca.explained_variance_ratio_.sum():.1%} variance)."
    )
    print(f"Saved visualization to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
