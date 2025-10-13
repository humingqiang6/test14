<?php
// Обработка формы и сохранение данных в файл

// Указываем директорию для сохранения файлов
$uploadDir = __DIR__ . '/uploads/';

// Создаем директорию, если она не существует
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

// Проверяем, была ли форма отправлена методом POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';

    // Простая валидация
    if (!empty($name) && !empty($email)) {
        // Создаем строку данных
        $data = "Имя: " . $name . "\nEmail: " . $email . "\n---\n";

        // Генерируем случайное имя файла
        $randomFileName = $uploadDir . uniqid('form_data_', true) . '.txt';

        // Сохраняем данные в файл
        if (file_put_contents($randomFileName, $data)) {
            echo "Данные успешно сохранены в файл: " . $randomFileName;
        } else {
            echo "Ошибка при сохранении файла.";
        }
    } else {
        echo "Пожалуйста, заполните все поля формы.";
    }
} else {
    // Если форма не отправлена, отображаем HTML-форму
    ?>
    <!DOCTYPE html>
    <html>
    <head>
        <title>Форма</title>
    </head>
    <body>
        <form method="post" action="">
            <label for="name">Имя:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            <input type="submit" value="Отправить">
        </form>
    </body>
    </html>
    <?php
}
?>