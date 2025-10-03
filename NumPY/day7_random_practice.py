
import numpy as np

# 1. Random float between 0 and 1
print("Random float (0-1):")
print(np.random.rand(), "\n")

# 2. Random array of floats (0-1)
print("Random array (3x2):")
print(np.random.rand(3, 2), "\n")


# 3. Random integers
print("Random integer (1-9):")
print(np.random.randint(1, 10), "\n")

print("Random integer array (4x3 between 1-100):")
print(np.random.randint(1, 100, size=(4, 3)), "\n")

# 4. Random numbers from normal distribution
print("Normal distribution (mean=0, std=1):")
print(np.random.randn(5), "\n")

print("Normal distribution (mean=50, std=5, size=10):")
print(np.random.normal(loc=50, scale=5, size=10), "\n")

# 5. Random numbers from uniform distribution
print("Uniform distribution (between 5 and 10):")
print(np.random.uniform(5, 10, size=5), "\n")

# 6. Shuffle an array
arr1 = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr1)
print("Shuffled array:")
print(arr1, "\n")

# 7. Random choice
arr2 = np.array([10, 20, 30, 40, 50])
print("Random choice from array (3 values, no repeat):")
print(np.random.choice(arr2, size=3, replace=False), "\n")

# 8. Random seed (for reproducibility)
np.random.seed(42)
print("Random numbers with seed=42 (always same):")
print(np.random.rand(3), "\n")