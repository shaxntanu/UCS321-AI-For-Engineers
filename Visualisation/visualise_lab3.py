"""Plot the house-size list from Lab 3."""

from pathlib import Path

import matplotlib.pyplot as plt


ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT_DIR / "Lab 3" / "figures" / "house_sizes.png"


def main() -> None:
    house_sizes = [1200, 1500, 2000, 1800, 2500, 1650]
    house_labels = [f"House {index}" for index in range(1, len(house_sizes) + 1)]

    figure, axis = plt.subplots(figsize=(8, 4.8))
    bars = axis.bar(house_labels, house_sizes, color="#398a84", width=0.68)
    axis.bar_label(bars, labels=[f"{size:,}" for size in house_sizes], padding=4, fontsize=9)
    axis.set(title="House sizes stored in the Lab 3 list", xlabel="List item", ylabel="Area (sq ft)")
    axis.set_ylim(0, 2900)
    axis.grid(axis="y", alpha=0.25)
    axis.set_axisbelow(True)
    figure.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved visualization to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
