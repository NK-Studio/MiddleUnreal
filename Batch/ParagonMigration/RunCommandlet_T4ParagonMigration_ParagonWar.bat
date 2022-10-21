@echo off

echo Run 'T4Commandlet / T4ParagonMigration Demo'

set UE4_VER=4.25
set UE4_KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\EpicGames\Unreal Engine\%UE4_VER%"
FOR /F "tokens=2*" %%A IN ('REG QUERY %UE4_KEY_NAME% /v InstalledDirectory 2^> nul') DO set "UE4_Path=%%B"

set HEROS="Crunch|Revenant|Morigesh|Terra|Drongo|SunWukong|Sparrow|Rampage"
set OUTPUT_PATH="/Game/T4DemoProjects/Common/Entity/Character/Paragon"
set SCRIPT_PATH="%~dp0T4ParagonHeroMetadata.py"

call %UE4_Path%\Engine\Binaries\Win64\UE4Editor-cmd.exe "%~dp0T4GameDeck.uproject" -run=T4ParagonMigration -GameName=ParagonWar -ForceOverwrite -OutputPath=%OUTPUT_PATH% -ScriptPath=%SCRIPT_PATH% -Hero=%HEROS%

pause

echo timeout -T 3
echo exit /B 0
