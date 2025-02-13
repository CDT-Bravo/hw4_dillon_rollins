param (
    [string]$ServerUrl = "http://localhost:5000",  # Update as needed
    [string]$ClientId = "unique_client_id_123"       # Update as needed
)

# Set the security protocol
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

function Register-Client {
    $registerUrl = "$ServerUrl/api/v1/register"
    $body = @{ client_id = $ClientId } | ConvertTo-Json
    try {
        $response = Invoke-RestMethod -Uri $registerUrl -Method Post -Body $body -ContentType "application/json"
        if ($response.status -eq "registered") {
            Write-Output "Client registered successfully."
        } else {
            Write-Output "Failed to register client."
        }
    } catch {
        Write-Output "Error registering client: $_"
    }
}

function Get-Task {
    $taskUrl = "$ServerUrl/api/v1/task?client_id=$ClientId"
    try {
        $response = Invoke-RestMethod -Uri $taskUrl -Method Get
        if ($response.task) {
            return $response.task
        } else {
            Write-Output "No task available."
            return $null
        }
    } catch {
        Write-Output "Error retrieving task: $_"
        return $null
    }
}

function Execute-Task {
    param (
        [string]$Task
    )
    Write-Output "Executing task: $Task"
    $result = "Task executed successfully: $Task"
    return $result
}

function Send-Result {
    param (
        [string]$Result
    )
    $resultUrl = "$ServerUrl/api/v1/result"
    $body = @{ client_id = $ClientId; result = $Result } | ConvertTo-Json
    try {
        $response = Invoke-RestMethod -Uri $resultUrl -Method Post -Body $body -ContentType "application/json"
        if ($response.status -eq "success") {
            Write-Output "Result sent successfully."
        } else {
            Write-Output "Failed to send result."
        }
    } catch {
        Write-Output "Error sending result: $_"
    }
}

function Main {
    Register-Client
    while ($true) {
        $task = Get-Task
        if ($task) {
            $result = Execute-Task -Task $task
            Send-Result -Result $result
        }
        Start-Sleep -Seconds 10  # Adjust the interval as needed
    }
}

Main