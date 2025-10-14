use std::fs::File;
use std::io::Write;
use uuid::Uuid;

// Определение структуры User
#[derive(Serialize, Deserialize, Debug)]
struct User {
    имя: String,
    возраст: u32,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Создание экземпляра пользователя
    let пользователь = User {
        имя: "Алексей".to_string(),
        возраст: 30,
    };

    // Генерация случайного UUID для имени файла
    let случайное_имя = Uuid::new_v4();

    // Сериализация структуры в JSON
    let json_данные = serde_json::to_string(&пользователь)?;

    // Запись JSON в файл с случайным именем в директории /tmp
    let путь_к_файлу = format!("/tmp/{}.json", случайное_имя);
    let mut файл = File::create(&путь_к_файлу)?;
    файл.write_all(json_данные.as_bytes())?;

    println!("Структура User сохранена в файл: {}", путь_к_файлу);
    Ok(())
}