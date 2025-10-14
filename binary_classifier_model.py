import torch
import torch.nn as nn
import torch.nn.functional as F

class BinaryClassifier(nn.Module):
    """
    A simple feedforward neural network for binary classification.
    """
    def __init__(self, input_size, hidden_size1=64, hidden_size2=32):
        """
        Initializes the layers of the neural network.

        Args:
            input_size (int): The number of features in the input data.
            hidden_size1 (int): Number of neurons in the first hidden layer. Default is 64.
            hidden_size2 (int): Number of neurons in the second hidden layer. Default is 32.
        """
        super(BinaryClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.fc3 = nn.Linear(hidden_size2, 1)  # Output layer for binary classification
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        """
        Defines the forward pass of the model.

        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, input_size).

        Returns:
            torch.Tensor: Output tensor of shape (batch_size, 1) containing logits.
        """
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)  # Logits, typically passed through sigmoid for probability
        return x

# Example usage:
if __name__ == "__main__":
    # Define a model for a dataset with 10 features
    model = BinaryClassifier(input_size=10)

    # Create a dummy batch of data (batch_size=5, features=10)
    dummy_input = torch.randn(5, 10)

    # Perform a forward pass
    output = model(dummy_input)
    print(f"Model output shape: {output.shape}") # Should be [5, 1]
    print(f"Model output (logits): {output.squeeze()}")