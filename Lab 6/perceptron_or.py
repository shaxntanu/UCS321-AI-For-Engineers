"""Train a single-layer perceptron to learn the OR function."""

print("PERCEPTRON TRAINING: OR FUNCTION")
print("=" * 58)
print()

# Inputs are binary (0 or 1); the desired outputs use bipolar targets (-1 or +1).
training_data = [
    ([0, 0], -1),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 1),
]

# A small positive learning rate is suitable for this four-row example.
alpha = 0.1
max_epochs = 100
weights = [0.0, 0.0]
bias = 0.0


def bipolar_step(net_input):
    """Return +1 at or above zero, and -1 below zero."""
    return 1 if net_input >= 0 else -1


print(f"Learning rate (alpha): {alpha}")
print(f"Initial weights: {weights}")
print(f"Initial bias: {bias:.2f}")
print()
print("Training progress")
print("Epoch | Weights          | Bias  | Misclassified rows")
print("-" * 58)

converged = False
epochs_completed = 0

for epoch in range(1, max_epochs + 1):
    errors = 0

    for inputs, target in training_data:
        net_input = sum(weight * value for weight, value in zip(weights, inputs)) + bias
        prediction = bipolar_step(net_input)

        if prediction != target:
            # Bipolar perceptron update, including the bias as a trainable weight.
            weights = [
                weight + alpha * target * value
                for weight, value in zip(weights, inputs)
            ]
            bias += alpha * target
            errors += 1

    epochs_completed = epoch
    print(f"{epoch:5} | {str([round(w, 2) for w in weights]):<17} | {bias:5.2f} | {errors:>18}")

    if errors == 0:
        converged = True
        break

if not converged:
    raise RuntimeError(f"Perceptron did not converge within {max_epochs} epochs.")

print()
print(f"Training converged after {epochs_completed} epochs.")
print()
print("Final OR truth table")
print("Input 1 | Input 2 | Target | Net input | Prediction")
print("-" * 58)

for inputs, target in training_data:
    net_input = sum(weight * value for weight, value in zip(weights, inputs)) + bias
    prediction = bipolar_step(net_input)
    print(
        f"   {inputs[0]}    |    {inputs[1]}    |   {target:>2}   |"
        f"   {net_input:>6.2f}  |     {prediction:>2}"
    )

print()
print(f"Learned weights: {[round(weight, 2) for weight in weights]}")
print(f"Learned bias: {bias:.2f}")
