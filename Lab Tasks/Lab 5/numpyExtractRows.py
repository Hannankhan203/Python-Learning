import numpy as np

randomArray = np.random.rand(10, 4)

print("Original 10x4 random array:")
print(randomArray)
print(f"Shape: {randomArray.shape}")
print()

firstFiveRows = randomArray[:5]

print("First five rows:")
print(firstFiveRows)
print(f"Shape: {firstFiveRows.shape}")
print()

print(f"Original array has {randomArray.shape[0]} rows")
print(f"Extracted array has {firstFiveRows.shape[0]} rows")