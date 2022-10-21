@echo off

echo Run '[T4Framework] WorldServer - StartNewWorld'

set UE4_VER=4.26
set UE4_KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\EpicGames\Unreal Engine\%UE4_VER%"
FOR /F "tokens=2*" %%A IN ('REG QUERY %UE4_KEY_NAME% /v InstalledDirectory 2^> nul') DO set "UE4_Path=%%B"

set UE4_EDIT_EXE="%UE4_Path%\Engine\Binaries\Win64\UE4Editor-cmd.exe"

call %UE4_EDIT_EXE% "%~dp0../../VirtualFlowBeta.uproject" -run=T4WorldServerService -ProjectID=StartNewWorld -IP=59.18.154.247 -Port=1320 -WorldID=CityTower

pause

echo timeout -T 3
echo exit /B 0
