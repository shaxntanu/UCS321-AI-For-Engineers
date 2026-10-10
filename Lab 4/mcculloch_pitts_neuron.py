# Lab 4: McCulloch-Pitts Neuron Implementation

print("McCULLOCH-PITTS NEURON IMPLEMENTATION")
print("=" * 50)
print()

# McCulloch-Pitts Neuron Function
def mcculloch_pitts(inputs, weights, threshold):
    """
    McCulloch-Pitts neuron model.
    
    Parameters:
    inputs: list of binary inputs (0 or 1)
    weights: list of weights for each input
    threshold: activation threshold
    
    Returns:
    output: binary output (0 or 1)
    """
    # Calculate weighted sum
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))
    
    # Apply threshold activation
    output = 1 if weighted_sum >= threshold else 0
    
    return output

print("Example 1: AND Gate using McCulloch-Pitts Neuron")
print("-" * 50)
# AND Gate: both inputs must be 1 for output to be 1
# Weights: [1, 1], Threshold: 2
and_weights = [1, 1]
and_threshold = 2

print("Weights:", and_weights)
print("Threshold:", and_threshold)
print()

print("Truth Table for AND Gate:")
print("Input 1 | Input 2 | Weighted Sum | Output")
print("-" * 45)

test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
for inp in test_inputs:
    weighted_sum = sum(i * w for i, w in zip(inp, and_weights))
    output = mcculloch_pitts(inp, and_weights, and_threshold)
    print(f"   {inp[0]}    |   {inp[1]}    |      {weighted_sum}       |   {output}")

print()
print()

print("Example 2: OR Gate using McCulloch-Pitts Neuron")
print("-" * 50)
# OR Gate: at least one input must be 1 for output to be 1
# Weights: [1, 1], Threshold: 1
or_weights = [1, 1]
or_threshold = 1

print("Weights:", or_weights)
print("Threshold:", or_threshold)
print()

print("Truth Table for OR Gate:")
print("Input 1 | Input 2 | Weighted Sum | Output")
print("-" * 45)

for inp in test_inputs:
    weighted_sum = sum(i * w for i, w in zip(inp, or_weights))
    output = mcculloch_pitts(inp, or_weights, or_threshold)
    print(f"   {inp[0]}    |   {inp[1]}    |      {weighted_sum}       |   {output}")

print()
print()

print("Example 3: NOT Gate using McCulloch-Pitts Neuron")
print("-" * 50)
# NOT Gate: single input, output is opposite
# Weight: [-1], Threshold: 0
not_weights = [-1]
not_threshold = 0

print("Weights:", not_weights)
print("Threshold:", not_threshold)
print()

print("Truth Table for NOT Gate:")
print("Input | Weighted Sum | Output")
print("-" * 30)

not_inputs = [(0,), (1,)]
for inp in not_inputs:
    weighted_sum = sum(i * w for i, w in zip(inp, not_weights))
    output = mcculloch_pitts(inp, not_weights, not_threshold)
    print(f"  {inp[0]}   |      {weighted_sum}       |   {output}")

print()
print()

print("Example 4: NAND Gate using McCulloch-Pitts Neuron")
print("-" * 50)
# NAND Gate: output is 0 only when both inputs are 1
# Weights: [-1, -1], Threshold: -1
nand_weights = [-1, -1]
nand_threshold = -1

print("Weights:", nand_weights)
print("Threshold:", nand_threshold)
print()

print("Truth Table for NAND Gate:")
print("Input 1 | Input 2 | Weighted Sum | Output")
print("-" * 45)

for inp in test_inputs:
    weighted_sum = sum(i * w for i, w in zip(inp, nand_weights))
    output = mcculloch_pitts(inp, nand_weights, nand_threshold)
    print(f"   {inp[0]}    |   {inp[1]}    |      {weighted_sum}       |   {output}")

print()
print("=" * 50)
print("McCulloch-Pitts Neuron Implementation Complete!")
