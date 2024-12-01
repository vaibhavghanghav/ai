import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Step 1: Define a range of possible values for a feature (e.g., aspect ratio)
x = np.linspace(0, 1, 100)  # Example range for normalized feature values

# Step 2: Define membership functions
triangle = fuzz.trimf(x, [0.2, 0.5, 0.8])  # Triangular membership function
trapezoid = fuzz.trapmf(x, [0.1, 0.3, 0.7, 0.9])  # Trapezoidal membership function
gaussian = fuzz.gaussmf(x, 0.5, 0.1)  # Gaussian membership function

# Visualize membership functions
plt.figure(figsize=(8, 4))
plt.plot(x, triangle, label="Triangle")
plt.plot(x, trapezoid, label="Trapezoid")
plt.plot(x, gaussian, label="Gaussian")
plt.title("Fuzzy Membership Functions for Shape Matching")
plt.xlabel("Feature Value")
plt.ylabel("Membership Degree")
plt.legend()
plt.show()

# Step 3: Example feature extraction for a handwritten character
character_feature = 0.45  # Example feature value (normalized)

# Step 4: Calculate membership degrees
triangle_degree = fuzz.interp_membership(x, triangle, character_feature)
trapezoid_degree = fuzz.interp_membership(x, trapezoid, character_feature)
gaussian_degree = fuzz.interp_membership(x, gaussian, character_feature)

print("Membership Degrees:")
print(f"Triangle: {triangle_degree:.2f}")
print(f"Trapezoid: {trapezoid_degree:.2f}")
print(f"Gaussian: {gaussian_degree:.2f}")

# Step 5: Combine membership degrees (using an example rule-based approach)
overall_similarity = max(triangle_degree, trapezoid_degree, gaussian_degree)
print(f"Overall Similarity: {overall_similarity:.2f}")
