import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # Initialize weights and bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        return 1 if np.dot(inputs, self.weights[1:]) + self.weights[0] >= 0 else 0

    def train(self, X, y):
        for _ in range(self.epochs):
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights[1:] += self.learning_rate * error * inputs
                self.weights[0] += self.learning_rate * error  # Bias update

# Simple dataset (AND gate)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # Expected output for AND gate

# Create and train Perceptron
p = Perceptron(input_size=2)
p.train(X, y)

# Test the Perceptron
for inputs in X:
    print(f"Input: {inputs} Prediction: {p.predict(inputs)}")
