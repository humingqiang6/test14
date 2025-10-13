// Определение структуры User
#[derive(Debug)]
struct User {
    name: String,
    age: u32,
}

fn main() {
    // Создание экземпляра структуры User
    let user = User {
        name: "Alice".to_string(),
        age: 30,
    };

    // Вывод в консоль для демонстрации
    println!("Создан пользователь: {:?}", user);

    // Генерация случайного имени файла (имитация)
    // В реальном Rust-коде использовалась бы библиотека, например, `rand`
    let random_filename = format!("user_data_{}.txt", 12345); // 12345 - фиктивное "случайное" число

    // Вывод имени файла
    println!("Сохранение в файл: {}", random_filename);

    // В реальном Rust-коде использовалась бы стандартная библиотека для записи в файл
    // use std::fs::File;
    // use std::io::Write;
    // let mut file = File::create(&random_filename)?;
    // writeln!(file, "Name: {}, Age: {}", user.name, user.age)?;
    println!("(Код Rust для сохранения в файл был бы здесь, если бы он был скомпилирован)");
}