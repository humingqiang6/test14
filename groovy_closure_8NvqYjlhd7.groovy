// Замыкание для фильтрации списка
def filterClosure = { list, condition ->
    return list.findAll(condition)
}

// Пример использования
def numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def evenNumbers = filterClosure(numbers, { it % 2 == 0 })
println "Original list: $numbers"
println "Filtered list (even numbers): $evenNumbers"

def words = ["apple", "banana", "cherry", "date"]
def longWords = filterClosure(words, { it.length() > 5 })
println "Original list: $words"
println "Filtered list (longer than 5 chars): $longWords"