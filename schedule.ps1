
# SCHEDULE TASK WITH WINDOWNS SCHEDULER
$action = New-ScheduledTaskAction -Execute 'Powershell.exe' -Argument 'E:\demo\VideoPS.ps1'
$trigger =  New-ScheduledTaskTrigger -Daily -At 10am

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "VideoPS Demo" -Description "Shane was here"