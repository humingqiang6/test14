# PowerShell script to get current user information
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object System.Security.Principal.WindowsPrincipal($currentUser)

Write-Output "User Name: $($currentUser.Name)"
Write-Output "User Type: $($principal.Identity.AuthenticationType)"
Write-Output "Is Admin: $($principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator))"