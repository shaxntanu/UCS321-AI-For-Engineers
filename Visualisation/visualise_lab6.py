"""Plot the learned OR perceptron boundary and epoch errors from Lab 6."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


ROOT_DIR = Path(__file__).resolve().parent.parent
LAB_DIR = ROOT_DIR / "Lab 6"
OUTPUT_PATH = LAB_DIR / "figures" / "perceptron_or_training.png"


def main() -> None:
    sys.path.insert(0, str(LAB_DIR))
    from perceptron_or import ALPHA, TRAINING_DATA, train_perceptron

    weights, bias, error_history, _ = train_perceptron()
    figure, axes = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1.25, 1]})

    x_grid, y_grid = np.meshgrid(np.linspace(-0.12, 1.12, 250), np.linspace(-0.12, 1.12, 250))
    net_grid = weights[0] * x_grid + weights[1] * y_grid + bias
    axes[0].contourf(x_grid, y_grid, net_grid >= 0, levels=[-0.5, 0.5, 1.5], colors=["#f4e9e5", "#d8ece8"], alpha=0.95)
    axes[0].contour(x_grid, y_grid, net_grid, levels=[0], colors=["#263b5a"], linewidths=2)

    for inputs, target in TRAINING_DATA:
        is_positive = target == 1
        label_offsets = {
            (0, 0): (10, 12),
            (0, 1): (10, -22),
            (1, 0): (-82, 12),
            (1, 1): (-82, 12),
        }
        axes[0].scatter(
            inputs[0], inputs[1], s=150, marker="o" if is_positive else "X",
            color="#398a84" if is_positive else "#d16b48", edgecolor="white",
            linewidth=1.2, zorder=4,
        )
        axes[0].annotate(
            f"({inputs[0]}, {inputs[1]}) → {target:+d}",
            (inputs[0], inputs[1]), xytext=label_offsets[tuple(inputs)], textcoords="offset points", fontsize=8,
        )

    axes[0].set_title(
        f"Learned boundary: {weights[0]:.1f}x₁ + {weights[1]:.1f}x₂ {bias:+.1f} = 0\n"
        f"net = 0 threshold; α = {ALPHA}",
        fontsize=11,
    )
    axes[0].set(xlabel="Binary input x₁", ylabel="Binary input x₂", xlim=(-0.12, 1.12), ylim=(-0.12, 1.12))
    axes[0].set_xticks([0, 1])
    axes[0].set_yticks([0, 1])
    axes[0].grid(alpha=0.2)

    epochs = np.arange(1, len(error_history) + 1)
    axes[1].plot(epochs, error_history, marker="o", color="#d16b48", linewidth=2)
    axes[1].fill_between(epochs, error_history, color="#d16b48", alpha=0.14)
    axes[1].set(title="Training errors by epoch", xlabel="Epoch", ylabel="Misclassified training rows")
    axes[1].set_xticks(epochs)
    axes[1].set_yticks(range(0, max(error_history) + 1))
    axes[1].set_ylim(bottom=0)
    axes[1].grid(alpha=0.25)

    figure.suptitle(f"Lab 6: OR perceptron converges in {len(error_history)} epochs", fontsize=14)
    figure.tight_layout()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved visualization to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
