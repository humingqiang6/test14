# Генерация случайного имени файла с расширением .csv
$randomFileName = [System.IO.Path]::GetRandomFileName() + ".csv"

# Получение списка процессов и экспорт в CSV-файл со случайным именем
Get-Process | Export-Csv -Path $randomFileName -NoTypeInformation

Write-Host "Список процессов сохранен в файл: $randomFileName"