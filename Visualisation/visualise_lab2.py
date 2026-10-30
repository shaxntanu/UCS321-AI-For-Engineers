"""Show the original missing scores and the mean-imputed Lab 2 scores."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parent.parent
LAB_DIR = ROOT_DIR / "Lab 2"
SCORE_COLUMNS = ["Math", "Science", "English"]
OUTPUT_PATH = LAB_DIR / "figures" / "mean_imputation.png"


def main() -> None:
    original = pd.read_csv(LAB_DIR / "original_dataset.csv").set_index("StudentID")
    imputed = pd.read_csv(LAB_DIR / "mean_imputed_dataset.csv").set_index("StudentID")
    original_scores = original[SCORE_COLUMNS]
    imputed_scores = imputed[SCORE_COLUMNS]

    figure, axes = plt.subplots(1, 2, figsize=(11.5, 5.4), gridspec_kw={"width_ratios": [1, 1.2]})

    missing = original_scores.isna().to_numpy()
    axes[0].imshow(missing, cmap=plt.matplotlib.colors.ListedColormap(["#dce9e8", "#e07a3f"]), aspect="auto", vmin=0, vmax=1)
    axes[0].set_title(f"Original scores\n{int(missing.sum())} missing values")
    axes[0].set_ylabel("Student ID")
    axes[0].set_yticks(range(len(original_scores)), original_scores.index)
    axes[0].set_xticks(range(len(SCORE_COLUMNS)), SCORE_COLUMNS)
    for row in range(len(original_scores)):
        for column in range(len(SCORE_COLUMNS)):
            axes[0].text(column, row, "—" if missing[row, column] else "✓", ha="center", va="center", color="#25343b", fontsize=9)

    value_image = axes[1].imshow(imputed_scores.to_numpy(), cmap="YlGnBu", aspect="auto", vmin=75, vmax=96)
    axes[1].set_title("After column-mean imputation")
    axes[1].set_yticks(range(len(imputed_scores)), imputed_scores.index)
    axes[1].set_xticks(range(len(SCORE_COLUMNS)), SCORE_COLUMNS)
    for row in range(len(imputed_scores)):
        for column in range(len(SCORE_COLUMNS)):
            axes[1].text(column, row, f"{imputed_scores.iloc[row, column]:.1f}", ha="center", va="center", color="#172b35", fontsize=8)
    colorbar = figure.colorbar(value_image, ax=axes[1], fraction=0.046, pad=0.04)
    colorbar.set_label("Score")

    for axis in axes:
        axis.tick_params(axis="x", rotation=20)
        axis.set_xticks(np.arange(-0.5, len(SCORE_COLUMNS), 1), minor=True)
        axis.set_yticks(np.arange(-0.5, len(original_scores), 1), minor=True)
        axis.grid(which="minor", color="white", linewidth=1.2)
        axis.tick_params(which="minor", bottom=False, left=False)
    figure.suptitle("Lab 2: mean imputation fills missing subject scores", fontsize=14)
    figure.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved visualization to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
