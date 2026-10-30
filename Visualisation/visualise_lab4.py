"""Visualize the McCulloch-Pitts gate truth tables from Lab 4."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT_DIR / "Lab 4" / "figures" / "logic_gate_truth_tables.png"


def main() -> None:
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    gates = [
        ("AND", [1, 1], 2),
        ("OR", [1, 1], 1),
        ("NAND", [-1, -1], -1),
    ]
    figure, axes = plt.subplots(2, 2, figsize=(9, 7))
    binary_cmap = plt.matplotlib.colors.ListedColormap(["#e8efed", "#398a84"])

    for axis, (name, weights, threshold) in zip(axes.flat[:3], gates):
        output_grid = np.zeros((2, 2), dtype=int)
        for first, second in inputs:
            weighted_sum = first * weights[0] + second * weights[1]
            output_grid[first, second] = int(weighted_sum >= threshold)
        axis.imshow(output_grid, cmap=binary_cmap, vmin=0, vmax=1)
        for first in range(2):
            for second in range(2):
                output = output_grid[first, second]
                axis.text(second, first, str(output), ha="center", va="center", fontsize=18, fontweight="bold", color="white" if output else "#293b40")
        axis.set(title=f"{name}  (weights={weights}, threshold={threshold})", xlabel="Input 2")
        axis.set_xticks([0, 1], ["0", "1"])
        axis.set_yticks([0, 1], ["0", "1"])
        axis.set_ylabel("Input 1")
        axis.set_xticks(np.arange(-0.5, 2, 1), minor=True)
        axis.set_yticks(np.arange(-0.5, 2, 1), minor=True)
        axis.grid(which="minor", color="white", linewidth=2)
        axis.tick_params(which="minor", bottom=False, left=False)

    not_axis = axes.flat[3]
    not_outputs = np.array([[1, 0]])
    not_axis.imshow(not_outputs, cmap=binary_cmap, vmin=0, vmax=1, aspect="auto")
    for input_value, output in enumerate(not_outputs[0]):
        not_axis.text(input_value, 0, str(output), ha="center", va="center", fontsize=18, fontweight="bold", color="white" if output else "#293b40")
    not_axis.set(title="NOT  (weight=[-1], threshold=0)", xlabel="Input")
    not_axis.set_xticks([0, 1], ["0", "1"])
    not_axis.set_yticks([])
    not_axis.set_xticks(np.arange(-0.5, 2, 1), minor=True)
    not_axis.grid(which="minor", color="white", linewidth=2)
    not_axis.tick_params(which="minor", bottom=False, left=False)

    figure.suptitle("Lab 4: McCulloch-Pitts neuron outputs", fontsize=14)
    figure.tight_layout()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved visualization to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
