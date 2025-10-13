# R script to create a bar plot
# Define data
categories <- c("A", "B", "C", "D")
values <- c(10, 25, 15, 30)

# Create the bar plot
barplot(values, 
        names.arg = categories,
        main = "Simple Bar Plot",
        xlab = "Categories",
        ylab = "Values",
        col = "lightblue",
        border = "black")

# Save the plot as a PNG file
png("bar_plot.png")
barplot(values, 
        names.arg = categories,
        main = "Simple Bar Plot",
        xlab = "Categories",
        ylab = "Values",
        col = "lightblue",
        border = "black")
dev.off()