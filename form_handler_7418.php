<?php
// Обработка формы
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Проверка наличия данных формы
    if (isset($_POST['name']) && isset($_POST['email'])) {
        $name = htmlspecialchars($_POST['name']);
        $email = htmlspecialchars($_POST['email']);

        // Простой пример валидации
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            // Здесь можно добавить логику сохранения в базу данных или файл
            $data = "Имя: $name, Email: $email\n";
            file_put_contents('form_data.txt', $data, FILE_APPEND | LOCK_EX);
            echo "Данные успешно сохранены.";
        } else {
            echo "Неверный формат email.";
        }
    } else {
        echo "Не все поля формы заполнены.";
    }
} else {
    echo "Данные формы не отправлены методом POST.";
}
?>