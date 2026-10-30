"""Train a single-layer perceptron to learn the OR function."""


TRAINING_DATA = [
    ([0, 0], -1),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 1),
]
ALPHA = 0.1
MAX_EPOCHS = 100


def bipolar_step(net_input):
    """Return +1 at or above zero, and -1 below zero."""
    return 1 if net_input >= 0 else -1


def train_perceptron(alpha=ALPHA, max_epochs=MAX_EPOCHS):
    """Train the OR perceptron and return weights, bias, and errors per epoch."""
    weights = [0.0, 0.0]
    bias = 0.0
    error_history = []
    parameter_history = []

    for _ in range(max_epochs):
        errors = 0

        for inputs, target in TRAINING_DATA:
            net_input = sum(weight * value for weight, value in zip(weights, inputs)) + bias
            prediction = bipolar_step(net_input)

            if prediction != target:
                weights = [
                    weight + alpha * target * value
                    for weight, value in zip(weights, inputs)
                ]
                bias += alpha * target
                errors += 1

        error_history.append(errors)
        parameter_history.append((weights.copy(), bias))
        if errors == 0:
            return weights, bias, error_history, parameter_history

    raise RuntimeError(f"Perceptron did not converge within {max_epochs} epochs.")


def main():
    weights, bias, error_history, parameter_history = train_perceptron()

    print("PERCEPTRON TRAINING: OR FUNCTION")
    print("=" * 58)
    print()
    print(f"Learning rate (alpha): {ALPHA}")
    print(f"Initial weights: {[0.0, 0.0]}")
    print("Initial bias: 0.00")
    print()
    print("Training progress")
    print("Epoch | Weights          | Bias  | Misclassified rows")
    print("-" * 58)
    for epoch, (errors, (epoch_weights, epoch_bias)) in enumerate(
        zip(error_history, parameter_history), start=1
    ):
        formatted_weights = [round(weight, 2) for weight in epoch_weights]
        print(
            f"{epoch:5} | {str(formatted_weights):<17} | "
            f"{epoch_bias:5.2f} | {errors:>18}"
        )

    print()
    print(f"Training converged after {len(error_history)} epochs.")
    print()
    print("Final OR truth table")
    print("Input 1 | Input 2 | Target | Net input | Prediction")
    print("-" * 58)
    for inputs, target in TRAINING_DATA:
        net_input = sum(weight * value for weight, value in zip(weights, inputs)) + bias
        prediction = bipolar_step(net_input)
        print(
            f"   {inputs[0]}    |    {inputs[1]}    |   {target:>2}   |"
            f"   {net_input:>6.2f}  |     {prediction:>2}"
        )

    print()
    print(f"Learned weights: {[round(weight, 2) for weight in weights]}")
    print(f"Learned bias: {bias:.2f}")


if __name__ == "__main__":
    main()
