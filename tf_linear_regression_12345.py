import tensorflow as tf
import numpy as np

# Generate dummy data
X = np.random.rand(100, 1).astype(np.float32)
y = 3.5 * X + 2.1 + np.random.randn(100, 1).astype(np.float32)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
print("Training the model...")
model.fit(X, y, epochs=50, verbose=0)

print("Model training complete.")
print("Model weights (slope):", model.get_weights()[0])
print("Model bias (intercept):", model.get_weights()[1])

# Make a prediction
prediction = model.predict([[0.5]])
print("Prediction for input 0.5:", prediction[0][0])