// Groovy closure for filtering a list
// This closure filters a list of numbers, returning only the even ones
def filterEvenNumbers = { list ->
    return list.findAll { it % 2 == 0 }
}

// Example usage
def numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def evenNumbers = filterEvenNumbers(numbers)

println "Original list: $numbers"
println "Filtered list (even numbers only): $evenNumbers"

// Another example with a closure that filters strings by length
def filterByLength = { list, minLength ->
    return list.findAll { it.length() >= minLength }
}

def words = ["apple", "cat", "elephant", "dog", "hippopotamus"]
def longWords = filterByLength(words, 5)

println "Original list of words: $words"
println "Filtered list (words with 5 or more characters): $longWords"
