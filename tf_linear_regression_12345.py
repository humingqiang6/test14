import tensorflow as tf
import numpy as np

# Generate dummy data
X_train = np.random.rand(100, 1).astype(np.float32)
y_train = 3.5 * X_train + 2.0 + np.random.randn(100, 1).astype(np.float32) * 0.1

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50)

# Print the learned parameters
weights, biases = model.layers[0].get_weights()
print(f"Learned weight: {weights[0][0]:.4f}")
print(f"Learned bias: {biases[0]:.4f}")

# Save the model
model.save('/workspace/my_linear_model.h5')
print("Model saved to /workspace/my_linear_model.h5")