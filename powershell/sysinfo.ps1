function getIP{ 
    (get-netipaddress).ipv4address | Select-String "192*"
} 

function getUser{
    $env:Username
}

function getHost{
    $Host.Name
}

function getVersion{
    $Host.Version.Major
}

$IP = getIP 
$User = getUser
$HostName = getHost
$ver = getVersion
$DATE = Get-Date

$BODY = "This machine's IP is $IP. User is $User. Hostname is $HostName. PowerShell $ver. Today's Date is $DATE."

Set-Content -Path C:\Users\tstegeman\Documents\GitHub\IT3038C-Scripts\powershell\IT3038C-Windows-SysInfo.txt -Value $BODY