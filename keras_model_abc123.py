import keras
from keras import layers

# Create a Sequential model
model = keras.Sequential()

# Add a Dense layer with 10 units and ReLU activation
model.add(layers.Dense(10, activation='relu', input_shape=(784,)))

# Print the model summary
model.summary()

# Save the model architecture as a Python script (example)
# Note: Keras models are typically saved in other formats like SavedModel or HDF5.
# Saving the definition as a .py file is possible but less common for loading later.
model.save('my_model.keras')
