# Read the email content from the file
$emailContent = Get-Content -Path "C:\data\email.txt" -Raw

# Use regex to find all email addresses in the content
$emails = $emailContent | Select-String -Pattern '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' -AllMatches

# Extract and save emails
if ($emails.Matches.Count -gt 0) {
    $emailsFound = $emails.Matches | ForEach-Object { $_.Value }
    $emailsFound | Set-Content -Path "C:\data\email-sender.txt"
    Write-Host "Extracted sender email(s) saved to C:\data\email-sender.txt"
} else {
    Write-Host "No email address found in the email content."
}
