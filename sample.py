# -*- coding: utf-8 -*-
"""Untitled58.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n_tRtJs5KXFtp6EXLIqijjVdGxJKKAHu
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Data
def generate_data(num_samples=100):
    np.random.seed(42)
    hours_studied = np.random.uniform(0, 10, num_samples)
    hours_slept = np.random.uniform(0, 10, num_samples)
    # Rule: pass if hours_studied * 0.5 + hours_slept * 0.2 > 4.5
    labels = (hours_studied * 0.5 + hours_slept * 0.2 > 4.5).astype(int)
    data = np.column_stack((hours_studied, hours_slept))
    return data, labels

# Step 2: Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Step 3: Train the Network
def train_fnn(data, labels, learning_rate=0.01, epochs=1000):
    np.random.seed(42)
    weights = np.random.randn(2)  # Initialize weights randomly
    bias = np.random.randn()     # Initialize bias randomly

    losses = []  # Store losses for plotting

    for epoch in range(epochs):
        # Forward pass
        linear_output = np.dot(data, weights) + bias
        predictions = sigmoid(linear_output)

        # Compute the loss (Binary Cross-Entropy)
        loss = -(labels * np.log(predictions) + (1 - labels) * np.log(1 - predictions)).mean()
        losses.append(loss)

        # Backward pass (Gradient Descent)
        d_loss_pred = predictions - labels
        d_pred_linear = sigmoid_derivative(linear_output)

        gradient_weights = np.dot(data.T, d_loss_pred * d_pred_linear) / len(data)
        gradient_bias = np.sum(d_loss_pred * d_pred_linear) / len(data)

        # Update weights and bias
        weights -= learning_rate * gradient_weights
        bias -= learning_rate * gradient_bias

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return weights, bias, losses

# Step 4: Plot Decision Boundary
def plot_decision_boundary(data, labels, weights, bias):
    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = sigmoid(weights[0] * xx + weights[1] * yy + bias)
    Z = (Z > 0.5).astype(int)

    plt.contourf(xx, yy, Z, alpha=0.6, cmap=plt.cm.Paired)
    plt.scatter(data[:, 0], data[:, 1], c=labels, edgecolor='k', cmap=plt.cm.Paired)
    plt.title("Decision Boundary")
    plt.xlabel("Hours Studied")
    plt.ylabel("Hours Slept")
    plt.show()

# Step 5: Plot Training Loss
def plot_training_loss(losses):
    plt.plot(losses)
    plt.title("Training Loss Over Epochs")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show()

# Generate synthetic data
data, labels = generate_data()

# Train the FNN
trained_weights, trained_bias, losses = train_fnn(data, labels)

# Print learned weights
print("Learned Weights:", trained_weights)
print("Learned Bias:", trained_bias)

# Plot decision boundary
plot_decision_boundary(data, labels, trained_weights, trained_bias)

# Plot training loss
plot_training_loss(losses)

