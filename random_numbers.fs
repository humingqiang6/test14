open System

// Функция для обработки списка чисел: вычисление суммы квадратов четных чисел
let processNumbers numbers =
    numbers
    |> List.filter (fun x -> x % 2 = 0)  // Фильтруем четные числа
    |> List.map (fun x -> x * x)         // Возводим в квадрат
    |> List.sum                          // Суммируем

[<EntryPoint>]
let main argv =
    let numbers = [1; 2; 3; 4; 5; 6; 7; 8; 9; 10] // Пример списка чисел
    let result = processNumbers numbers
    printfn "Сумма квадратов четных чисел: %d" result
    0