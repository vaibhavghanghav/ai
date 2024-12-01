import numpy as np
import matplotlib.pyplot as plt
import skimage.measure as measure
from skimage import draw

# Fuzzy membership functions
def thin_membership(aspect_ratio):
    """Fuzzy set for thin shapes (high aspect ratio)."""
    return min(1, max(0, (aspect_ratio - 1) / 2))

def wide_membership(aspect_ratio):
    """Fuzzy set for wide shapes (low aspect ratio)."""
    return min(1, max(0, (2 - aspect_ratio) / 2))

def curved_membership(stroke_count):
    """Fuzzy set for curved shapes (low stroke count)."""
    return min(1, max(0, (5 - stroke_count) / 5))

def straight_membership(stroke_count):
    """Fuzzy set for straight shapes (high stroke count)."""
    return min(1, max(0, (stroke_count - 2) / 5))

# Simulated handwritten character shape
def generate_character():
    """Generate a simple handwritten character shape."""
    image = np.zeros((100, 100), dtype=int)
    rr, cc = draw.line(20, 20, 80, 80)  # Simple diagonal line (could be part of 'X')
    image[rr, cc] = 1
    return image

def extract_features(character_image):
    """Extract features from a binary image (e.g., aspect ratio, stroke count)."""
    # Aspect Ratio: Width / Height
    height, width = character_image.shape
    aspect_ratio = width / height

    # Stroke Count: Count number of objects (connected components)
    labeled, num_features = measure.label(character_image, connectivity=2)
    return aspect_ratio, num_features

def match_shape(character_image):
    """Match the shape to a fuzzy set."""
    aspect_ratio, stroke_count = extract_features(character_image)

    # Apply fuzzy logic to determine if the shape is thin, wide, curved, or straight
    thin_score = thin_membership(aspect_ratio)
    wide_score = wide_membership(aspect_ratio)
    curved_score = curved_membership(stroke_count)
    straight_score = straight_membership(stroke_count)

    print(f"Aspect Ratio: {aspect_ratio}")
    print(f"Stroke Count: {stroke_count}")
    print(f"Thin Score: {thin_score}")
    print(f"Wide Score: {wide_score}")
    print(f"Curved Score: {curved_score}")
    print(f"Straight Score: {straight_score}")

    # Example of fuzzy decision making
    if thin_score > wide_score:
        print("The shape is more Thin")
    else:
        print("The shape is more Wide")

    if curved_score > straight_score:
        print("The shape is Curved")
    else:
        print("The shape is Straight")

# Generate a character and match it
character_image = generate_character()
plt.imshow(character_image, cmap='gray')
plt.title("Generated Handwritten Character")
plt.show()

# Perform shape matching
match_shape(character_image)
