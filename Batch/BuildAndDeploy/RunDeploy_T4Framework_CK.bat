echo @echo off

set UE4_VER=4.26
set UE4_KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\EpicGames\Unreal Engine\%UE4_VER%"
FOR /F "tokens=2*" %%A IN ('REG QUERY %UE4_KEY_NAME% /v InstalledDirectory 2^> nul') DO set "UE4_Path=%%B"

set ORIGINAL_SOURCE_PATH=D:\VirtualFlow
set DEPLOY_SOURCE_PATH=D:\VirtualFlow
set DEPLOY_BINARY_PATH=D:\VirtualFlow
set ORIGINAL_SOURCE_REPO_NAME=T4Framework
set DEOPLY_SOURCE_REPO_NAME=T4Framework_CK_Source
set DEPLOY_BINARY_REPO_NAME=T4Framework_CK
set PROJECT_NAME=VirtualFlowBeta


echo ****************************************************
echo [0] Path Setup
echo ****************************************************

set ORIGINAL_SOURCE_PATH="%ORIGINAL_SOURCE_PATH%\%ORIGINAL_SOURCE_REPO_NAME%"
set DEPLOY_SOURCE_PATH="%DEPLOY_SOURCE_PATH%\%DEOPLY_SOURCE_REPO_NAME%"
set DEPLOY_BINARY_PATH="%DEPLOY_BINARY_PATH%\%DEPLOY_BINARY_REPO_NAME%"

set PLUGIN_PATH_CORE="Plugins\T4Framework\T4FrameworkCore"
set PLUGIN_PATH_EDITOR="Plugins\T4Framework\T4FrameworkEditor"
set PLUGIN_PATH_SERVICE="Plugins\T4Framework\T4FrameworkService"
set PLUGIN_PATH_TEST="Plugins\T4Framework\T4FrameworkTest"


echo ****************************************************
echo [1] Copy Deploy Sources
echo ****************************************************

del /S /Q "%DEPLOY_SOURCE_PATH%\Binaries\*"
del /S /Q "%DEPLOY_SOURCE_PATH%\Source\*"
del /S /Q "%DEPLOY_SOURCE_PATH%\Protocol\*"
del /S /Q "%DEPLOY_SOURCE_PATH%\ThirdParty\*"
del /S /Q "%DEPLOY_SOURCE_PATH%\Config\*"
del /S /Q "%DEPLOY_SOURCE_PATH%\Content\*"
del /S /Q "%DEPLOY_SOURCE_PATH%\Plugins\*"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\UpdateHistory.md" "%DEPLOY_SOURCE_PATH%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\ThirdParty.md" "%DEPLOY_SOURCE_PATH%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\INPUT.md" "%DEPLOY_SOURCE_PATH%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\Source\*.*" "%DEPLOY_SOURCE_PATH%\Source\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\Protocol\*.*" "%DEPLOY_SOURCE_PATH%\Protocol\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\ThirdParty\*.*" "%DEPLOY_SOURCE_PATH%\ThirdParty\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\Config\*.*" "%DEPLOY_SOURCE_PATH%\Config\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\Content\VirtualFlow\SystemPack\*.*" "%DEPLOY_SOURCE_PATH%\Content\VirtualFlow\SystemPack\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\Content\VirtualFlow\UIPack\*.*" "%DEPLOY_SOURCE_PATH%\Content\VirtualFlow\UIPack\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\Content\Splash\*.*" "%DEPLOY_SOURCE_PATH%\Content\Splash\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_CORE%\*.uplugin" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Config\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Config\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Source\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Source\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\*.uplugin" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Config\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Config\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Content\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Content\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Source\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Source\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\*.uplugin" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Config\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Config\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Source\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Source\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_TEST%\*.uplugin" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Config\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Config\"
echo f | xcopy /S /Y "%ORIGINAL_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Source\*.*" "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Source\"


echo ****************************************************
echo [2] Build Editor
echo ****************************************************

call "%UE4_Path%\Engine\Binaries\DotNET\UnrealBuildTool.exe" Shipping Win64 "%DEPLOY_SOURCE_PATH%\%PROJECT_NAME%.uproject" -TargetType="Game" -Progress -waitmutex -Clean
if not "%ERRORLEVEL%" == "0" goto ERROR
call "%UE4_Path%\Engine\Binaries\DotNET\UnrealBuildTool.exe" Development Win64 "%DEPLOY_SOURCE_PATH%\%PROJECT_NAME%.uproject" -TargetType="Game" -Progress -waitmutex -Clean
if not "%ERRORLEVEL%" == "0" goto ERROR
call "%UE4_Path%\Engine\Binaries\DotNET\UnrealBuildTool.exe" Development Win64 "%DEPLOY_SOURCE_PATH%\%PROJECT_NAME%.uproject" -TargetType="Editor" -Progress -waitmutex -Clean
if not "%ERRORLEVEL%" == "0" goto ERROR
call "%UE4_Path%\Engine\Binaries\DotNET\UnrealBuildTool.exe" Shipping Win64 "%DEPLOY_SOURCE_PATH%\%PROJECT_NAME%.uproject" -TargetType="Game" -Progress -waitmutex
if not "%ERRORLEVEL%" == "0" goto ERROR
call "%UE4_Path%\Engine\Binaries\DotNET\UnrealBuildTool.exe" Development Win64 "%DEPLOY_SOURCE_PATH%\%PROJECT_NAME%.uproject" -TargetType="Game" -Progress -waitmutex
if not "%ERRORLEVEL%" == "0" goto ERROR
call "%UE4_Path%\Engine\Binaries\DotNET\UnrealBuildTool.exe" Development Win64 "%DEPLOY_SOURCE_PATH%\%PROJECT_NAME%.uproject" -TargetType="Editor" -Progress -waitmutex
if not "%ERRORLEVEL%" == "0" goto ERROR


echo ****************************************************
echo [3] Deploy Binary
echo ****************************************************

del /S /Q "%DEPLOY_BINARY_PATH%\Binaries\*"
del /S /Q "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_CORE%\Binaries\*"
del /S /Q "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\*"
del /S /Q "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Content\*"
del /S /Q "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\*"
del /S /Q "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_TEST%\Binaries\*"
del /S /Q "%DEPLOY_BINARY_PATH%\Content\VirtualFlow\SystemPack\*"
del /S /Q "%DEPLOY_BINARY_PATH%\Content\VirtualFlow\UIPack\*"
del /S /Q "%DEPLOY_BINARY_PATH%\Content\Splash\*"

echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\UpdateHistory.md" "%DEPLOY_BINARY_PATH%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\ThirdParty.md" "%DEPLOY_BINARY_PATH%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\INPUT.md" "%DEPLOY_BINARY_PATH%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Binaries\*.exe" "%DEPLOY_BINARY_PATH%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Binaries\*.dll" "%DEPLOY_BINARY_PATH%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Binaries\*.pdb" "%DEPLOY_BINARY_PATH%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Binaries\*.modules" "%DEPLOY_BINARY_PATH%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Binaries\*.target" "%DEPLOY_BINARY_PATH%\Binaries\"

echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\*.uplugin" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_CORE%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Config\*.ini" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_CORE%\Config\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Binaries\*.dll" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_CORE%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Binaries\*.pdb" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_CORE%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_CORE%\Binaries\*.modules" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_CORE%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\*.uplugin" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Config\*.ini" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Config\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Content\*.*" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Content\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\*.dll" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\*.pdb" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\*.modules" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_EDITOR%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\*.uplugin" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_SERVICE%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Config\*.ini" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_SERVICE%\Config\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\*.dll" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\*.pdb" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\*.modules" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_SERVICE%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\*.uplugin" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_TEST%\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Config\*.ini" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_TEST%\Config\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Binaries\*.dll" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_TEST%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Binaries\*.pdb" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_TEST%\Binaries\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\%PLUGIN_PATH_TEST%\Binaries\*.modules" "%DEPLOY_BINARY_PATH%\%PLUGIN_PATH_TEST%\Binaries\"

echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Content\Splash\*.*" "%DEPLOY_BINARY_PATH%\Content\Splash\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Content\VirtualFlow\SystemPack\*.*" "%DEPLOY_BINARY_PATH%\Content\VirtualFlow\SystemPack\"
echo f | xcopy /S /Y "%DEPLOY_SOURCE_PATH%\Content\VirtualFlow\UIPack\*.*" "%DEPLOY_BINARY_PATH%\Content\VirtualFlow\UIPack\"

echo timeout -T 3
echo exit /B 0
goto QUIT


:ERROR
echo Error!!!
pause


:QUIT
