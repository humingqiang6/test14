// F# Script for processing a list of numbers

// Original list of numbers
let numbers = [3; 1; 4; 1; 5; 9; 2; 6; 5; 3; 5]

// Function to calculate the sum of a list
let sumList lst = List.sum lst

// Function to calculate the average of a list
let avgList lst = 
    match lst with
    | [] -> 0.0
    | _ -> (float (sumList lst)) / (float (List.length lst))

// Function to get unique numbers and sort them
let uniqueSorted lst = lst |> List.distinct |> List.sort

// Process the list
let total = sumList numbers
let average = avgList numbers
let uniqueNumbers = uniqueSorted numbers

// Print results to console
printfn "Original list: %A" numbers
printfn "Sum: %d" total
printfn "Average: %.2f" average
printfn "Unique sorted list: %A" uniqueNumbers

// Save results to a string
let resultsString = 
    sprintf "Original list: %A\nSum: %d\nAverage: %.2f\nUnique sorted list: %A" 
        numbers total average uniqueNumbers

// Write results to a file with a random name
open System
open System.IO

let random = Random()
let fileName = sprintf "results_%d.txt" (random.Next(10000, 99999))
File.WriteAllText(fileName, resultsString)

printfn "Results saved to %s" fileName