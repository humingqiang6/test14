import numpy as np
import tensorflow as tf

# Generate some dummy data for demonstration
# Features (X) and target variable (y) with a linear relationship y = 2*X + 1 plus some noise
np.random.seed(42)
X = np.random.rand(100, 1).astype(np.float32)
y = 2 * X.squeeze() + 1 + np.random.randn(100).astype(np.float32) * 0.1

# Define the model using Keras Sequential API
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
print("Training the model...")
model.fit(X, y, epochs=100, verbose=0)

# Print final loss
final_loss = model.history.history['loss'][-1]
print(f"Training completed. Final loss (MSE): {final_loss:.4f}")

# Make a prediction on a new sample
new_X = np.array([[0.5]], dtype=np.float32)
predicted_y = model.predict(new_X)
print(f"Prediction for input {new_X[0][0]:.2f}: {predicted_y[0][0]:.4f}")