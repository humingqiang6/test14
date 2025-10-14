# R script to generate a bar plot and save it

# Define data
categories <- c("A", "B", "C", "D")
values <- c(10, 15, 8, 12)

# Create the bar plot
barplot(values,
        names.arg = categories,
        main = "Simple Bar Plot",
        xlab = "Categories",
        ylab = "Values",
        col = "lightblue",
        border = "black")

# Optionally, save the plot to a file
# png("bar_plot.png")
# barplot(values, names.arg = categories, main = "Simple Bar Plot", xlab = "Categories", ylab = "Values", col = "lightblue", border = "black")
# dev.off()