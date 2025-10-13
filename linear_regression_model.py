import tensorflow as tf
import numpy as np

# Generate some dummy data for training
# Features (X) and target (y) with a linear relationship y = 2*X + 1 + noise
X_train = np.random.random((100, 1)).astype(np.float32)
y_train = 2 * X_train.flatten() + 1 + 0.1 * np.random.randn(100).astype(np.float32)

# Define a simple Sequential model for linear regression
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model with optimizer, loss function, and metric
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['mae'])

# Print a summary of the model
print("Model Summary:")
model.summary()

# Train the model
print("\nTraining the model...")
history = model.fit(X_train, y_train, epochs=50, verbose=0)

# Print final loss
print(f"\nFinal training loss: {history.history['loss'][-1]:.4f}")

# Get the learned weights (slope and bias)
weights, bias = model.layers[0].get_weights()
print(f"Learned slope (weight): {weights[0][0]:.4f}")
print(f"Learned bias: {bias[0]:.4f}")

# Save the entire model to an HDF5 file
model.save('linear_regression_model.h5')
print("\nModel saved as 'linear_regression_model.h5'")

# Optional: Load the model back and make a prediction
loaded_model = tf.keras.models.load_model('linear_regression_model.h5')
sample_input = np.array([[0.5]], dtype=np.float32)
prediction = loaded_model.predict(sample_input)
print(f"\nPrediction for input {sample_input[0][0]}: {prediction[0][0]:.4f}")