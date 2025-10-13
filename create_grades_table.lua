#!/usr/bin/env lua

-- Define a table to store student grades
local student_grades = {
    Alice = 92,
    Bob = 85,
    Charlie = 78,
    David = 96,
    Eve = 88
}

-- Calculate the average grade
local total = 0
local count = 0
for name, grade in pairs(student_grades) do
    total = total + grade
    count = count + 1
end

local average = total / count

-- Print the table and the average
print("Student Grades:")
for name, grade in pairs(student_grades) do
    print(name .. ": " .. grade)
end
print("Average Grade: " .. average)

-- Save the table and average to a new file with a random name
local file_name = "grades_output_" .. math.random(10000, 99999) .. ".lua"
local file = io.open(file_name, "w")
if file then
    file:write("-- Student Grades and Average\n")
    file:write("local student_grades = {\n")
    for name, grade in pairs(student_grades) do
        file:write("    " .. name .. " = " .. grade .. ",\n")
    end
    file:write("}\n")
    file:write("local average = " .. average .. "\n")
    file:write("-- End of data\n")
    file:close()
    print("Data saved to " .. file_name)
else
    print("Error: Could not open file for writing: " .. file_name)
end
