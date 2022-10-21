@echo off

echo Run 'T4Commandlet / T4ParagonMigration'

set UE4_KEY_NAME="HKEY_CURRENT_USER\Software\Epic Games\Unreal Engine\Builds"
set UE4_VER=4_25
FOR /F "tokens=2*" %%A IN ('REG QUERY %UE4_KEY_NAME% /v %UE4_VER% 2^> nul') DO set "UE4_Path=%%B"

set HEROS="All"
set OUTPUT_PATH="/Game/TECH4Demo/Entity/ParagonMigrationTest"
set SCRIPT_PATH="%~dp0T4ParagonHeroMetadata.py"

call %UE4_Path%\Engine\Binaries\Win64\UE4Editor-cmd.exe "%~dp0T4GameDeck.uproject" -run=T4ParagonMigration -ForceOverwrite -OutputPath=%OUTPUT_PATH% -ScriptPath=%SCRIPT_PATH% -Hero=%HEROS%

echo timeout -T 3
echo exit /B 0

pause