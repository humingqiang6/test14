# PowerShell script to get processes and save to a file with a random name
$processes = Get-Process
$outputFileName = "processes_" + (Get-Random -Maximum 10000) + ".csv"
$processes | Export-Csv -Path $outputFileName -NoTypeInformation
Write-Host "Process list saved to $outputFileName"