from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample data
animals = ['cat', 'dog', 'fish', 'cat', 'dog', 'bird']

# Reshape the data to be a 2D array
animals_array = np.array(animals).reshape(-1, 1)

# Initialize the OneHotEncoder
encoder = OneHotEncoder()

# Fit and transform the data
one_hot_encoded = encoder.fit_transform(animals_array)

# Display the result
print("Animals: ", animals)
print("One-Hot Encoded:\n", one_hot_encoded)