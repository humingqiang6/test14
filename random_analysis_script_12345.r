# Load the CSV file into a data frame
data <- read.csv("data.csv")

# Print the first few rows of the data frame
print("First 6 rows of the dataset:")
print(head(data))

# Print summary statistics for numeric columns
print("Summary statistics:")
print(summary(data))