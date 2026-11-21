import numpy as np
import pandas as pd

# Generate ten reproducible random numbers and store them in a Series.
rng = np.random.default_rng(seed=42)
values = rng.random(10)
numbers = pd.Series(values, index=[f"item_{i}" for i in range(1, 11)], name="value")

print("Series:")
print(numbers)

# Indexing: retrieve by label and by integer position.
print("\nIndexing:")
print("item_3:", numbers.loc["item_3"])
print("First item:", numbers.iloc[0])

# Filtering: keep values greater than the Series mean.
print("\nValues above the mean:")
print(numbers[numbers > numbers.mean()])

# Summary statistics.
print("\nStatistics:")
print("Mean:", numbers.mean())
print("Median:", numbers.median())
print("Minimum:", numbers.min())
print("Maximum:", numbers.max())