<?php
// Database configuration
$servername = "localhost"; // or your database server address
$username = "your_username"; // your database username
$password = "your_password"; // your database password
$dbname = "your_database"; // your database name

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);

    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    echo "Connected successfully to the database!";
    
    // Perform database operations here

} catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// Close the connection (optional, as it closes automatically at the end of the script)
$pdo = null;
?>