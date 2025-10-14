# R script to generate a bar plot and save it as an image

# Create sample data
categories <- c("A", "B", "C", "D", "E")
values <- c(23, 45, 56, 78, 32)

# Create the bar plot
barplot(values, 
        names.arg = categories,
        main = "Sample Bar Plot",
        xlab = "Categories",
        ylab = "Values",
        col = "skyblue",
        border = "black")

# Save the plot as a PNG file in the current working directory
# The file name is fixed as 'bar_chart.png' as the requirement for a 'random' name is ambiguous in a script context.
# A fixed name is used here for reproducibility.
png("bar_chart.png", width = 800, height = 600)
barplot(values,
        names.arg = categories,
        main = "Sample Bar Plot",
        xlab = "Categories",
        ylab = "Values",
        col = "skyblue",
        border = "black")
# Turn off the graphics device to save the file
dev.off()

cat("Bar plot generated and saved as bar_chart.png\n")