# R script for creating a scatter plot and saving it to a file with a random name
# This script generates random data, creates a scatter plot, and saves it as a PNG file.

# Load required libraries (if any)
# In this case, base R is sufficient

# Generate random data
set.seed(42)  # For reproducible results
n_points <- 100
x_data <- rnorm(n_points)
y_data <- x_data + rnorm(n_points, sd = 0.5)  # Add some noise

# Generate a random filename for the output plot
# Using a combination of letters and numbers
random_name <- paste0(sample(c(letters, LETTERS, 0:9), 10, replace = TRUE), collapse = "")
plot_filename <- paste0("/workspace/plot_", random_name, ".png")

# Create the scatter plot
plot(x_data, y_data, main = "Scatter Plot of Random Data", xlab = "X Values", ylab = "Y Values", pch = 19, col = "blue")

# Save the plot to the file
png(filename = plot_filename, width = 800, height = 600)
plot(x_data, y_data, main = "Scatter Plot of Random Data", xlab = "X Values", ylab = "Y Values", pch = 19, col = "blue")
dev.off()

cat("Scatter plot saved to:", plot_filename, "\n")