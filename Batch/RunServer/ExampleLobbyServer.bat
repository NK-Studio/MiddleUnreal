@echo off

echo Run '[T4Framework] LobbyServer'

set UE4_VER=4.26
set UE4_KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\EpicGames\Unreal Engine\%UE4_VER%"
FOR /F "tokens=2*" %%A IN ('REG QUERY %UE4_KEY_NAME% /v InstalledDirectory 2^> nul') DO set "UE4_Path=%%B"

set UE4_EDIT_EXE="%UE4_Path%\Engine\Binaries\Win64\UE4Editor-cmd.exe"

echo %UE4_EDIT_EXE%

call %UE4_EDIT_EXE% "%~dp0../../VirtualFlowBeta.uproject" -run=T4LobbyServerServiceCommandlet -port=1232

pause

echo timeout -T 3
echo exit /B 0
