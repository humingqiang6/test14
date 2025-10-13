import tensorflow as tf
import numpy as np

# Generate random data for demonstration
num_samples = 100
X = np.random.rand(num_samples).astype(np.float32)
y = 3.5 * X + 2.0 + np.random.randn(num_samples).astype(np.float32)  # y = 3.5x + 2 + noise

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
print("Training the model...")
model.fit(X, y, epochs=100, verbose=0)

# Print the learned parameters
weights, biases = model.layers[0].get_weights()
print(f"Learned parameters: Weight = {weights[0][0]:.4f}, Bias = {biases[0]:.4f}")

# Save the model (optional)
# model.save('my_linear_model.h5')