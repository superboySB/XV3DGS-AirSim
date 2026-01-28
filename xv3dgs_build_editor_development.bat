REM Build XV3DGSEditor Development (one-time compile to resolve missing module prompt)

@echo off
if "%UE_ROOT%" == "" (
  echo:
  echo:ERROR: UE_ROOT environmant variable is not set. It must be set to the target ^
Unreal engine's root folder path, ex. C:\Program Files\Epic Games\UE_5.2
) else (
  echo:Building XV3DGSEditor Development with UE_ROOT=%UE_ROOT%
  cd %~dp0
  "%UE_ROOT%\Engine\Build\BatchFiles\Build.bat" XV3DGSEditor Win64 Development "%~dp0\XV3DGS.uproject" -waitmutex -CompilerVersion=14.37.32822
)
