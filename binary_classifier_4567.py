import torch
import torch.nn as nn
import torch.nn.functional as F

class BinaryClassifier(nn.Module):
    """
    A simple feedforward neural network for binary classification.
    """
    def __init__(self, input_size, hidden_size1=64, hidden_size2=32, dropout_rate=0.5):
        """
        Initializes the layers of the neural network.

        Args:
            input_size (int): The number of input features.
            hidden_size1 (int): Number of neurons in the first hidden layer. Default is 64.
            hidden_size2 (int): Number of neurons in the second hidden layer. Default is 32.
            dropout_rate (float): Dropout rate for regularization. Default is 0.5.
        """
        super(BinaryClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.fc3 = nn.Linear(hidden_size2, 1)  # Single output for binary classification
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        """
        Defines the forward pass of the model.

        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, input_size).

        Returns:
            torch.Tensor: Output tensor of shape (batch_size, 1) before activation.
        """
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)  # Sigmoid activation is typically applied after this in the loss function (BCEWithLogitsLoss)
        return x

# Example usage:
if __name__ == "__main__":
    # Define model parameters
    INPUT_SIZE = 10  # Example: 10 input features
    model = BinaryClassifier(input_size=INPUT_SIZE)

    # Print model architecture
    print(model)

    # Example forward pass with a batch of 5 samples
    example_input = torch.randn(5, INPUT_SIZE)
    output = model(example_input)
    print(f"Output shape: {output.shape}") # Should be [5, 1]
    print(f"Output values:\n{output}")