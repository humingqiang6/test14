import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Create a simple Sequential model
model = keras.Sequential([
    layers.Dense(10, activation='relu', input_shape=(5,))  # Example: 5 input features, 10 neurons in the dense layer
])

# Display the model summary
model.summary()

# Optionally, you can save the model in SavedModel format
# model.save('my_model')