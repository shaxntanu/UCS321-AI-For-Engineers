"""Plot Lab 1's from-scratch house-price linear regression example."""

from pathlib import Path

import matplotlib.pyplot as plt


ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT_DIR / "Lab 1" / "figures" / "linear_regression.png"


def main() -> None:
    areas = [1000, 1500, 2000, 2500, 3000]
    prices = [30, 45, 60, 75, 90]
    train_areas, train_prices = areas[:4], prices[:4]
    test_area, actual_test_price = areas[4], prices[4]

    count = len(train_areas)
    sum_x = sum(train_areas)
    sum_y = sum(train_prices)
    sum_xy = sum(x * y for x, y in zip(train_areas, train_prices))
    sum_x_squared = sum(x * x for x in train_areas)
    slope = (count * sum_xy - sum_x * sum_y) / (count * sum_x_squared - sum_x**2)
    intercept = (sum_y - slope * sum_x) / count
    predicted_test_price = slope * test_area + intercept

    line_areas = list(range(900, 3151, 50))
    line_prices = [slope * area + intercept for area in line_areas]

    figure, axis = plt.subplots(figsize=(8.5, 5.2))
    axis.plot(line_areas, line_prices, color="#276678", linewidth=2.5, label="Fitted regression line")
    axis.scatter(train_areas, train_prices, color="#276678", s=65, zorder=3, label="Training houses")
    axis.scatter(
        [test_area], [actual_test_price], marker="*", s=190,
        color="#e07a3f", edgecolor="white", linewidth=0.8, zorder=4,
        label="Held-out house (actual)",
    )
    axis.scatter(
        [test_area], [predicted_test_price], marker="o", s=95,
        facecolor="white", edgecolor="#25316d", linewidth=2, zorder=5,
        label="Model prediction",
    )
    axis.annotate(
        f"Test: {test_area:,} sq ft\nActual = predicted = {predicted_test_price:.0f} Lakhs",
        xy=(test_area, predicted_test_price), xytext=(-245, -48),
        textcoords="offset points", arrowprops={"arrowstyle": "->", "color": "#555"},
        fontsize=9,
    )
    axis.set(title="House price prediction with linear regression", xlabel="Area (sq ft)", ylabel="Price (Lakhs)")
    axis.grid(alpha=0.25)
    axis.legend(frameon=False)
    figure.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved visualization to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
