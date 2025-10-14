open System
open System.IO

// Функция для обработки списка чисел: вычисление квадратов и суммы
let processNumbers numbers =
    let squares = List.map (fun x -> x * x) numbers
    let sum = List.sum numbers
    (squares, sum)

// Основная часть программы
[<EntryPoint>]
let main argv =
    let inputNumbers = [1; 2; 3; 4; 5]

    let (squares, total) = processNumbers inputNumbers

    // Генерация случайного имени файла
    let fileName = Path.GetRandomFileName() + ".txt"

    // Формирование содержимого файла
    let fileContent = sprintf "Original: %A\nSquares: %A\nSum: %d" inputNumbers squares total

    // Запись в файл
    File.WriteAllText(fileName, fileContent)
    printfn "Results written to %s" fileName

    0 // Возврат кода завершения