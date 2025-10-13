import keras
import numpy as np

# Define a simple Sequential model
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(8,))  # Input shape (8,) -> Dense layer with 10 units
])

# Display the model's architecture
model.summary()

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Example of saving the model's configuration (optional)
# config = model.get_config()
# print(config)
