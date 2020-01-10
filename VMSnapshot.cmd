@echo off
title VM Workstation Player Snapshotverwaltung V 1.1 © 2019 Oliver Jung
color 3E
mode con lines=35 cols=156
setlocal enabledelayedexpansion
:: VM Snapshotwiederherstellung V 1.1
:: (c) 10.08.2019 Oliver Jung
::
::
:: V 1.1 12.12.2019: Verbesserung Programmlogik @Oliver Jung 
:: V 2.0 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung 
::
:Variable erzeugen
::-------------------------------------------------------------------------------------------
set VMWorkstationPath=%~dp0
set VMWorkstationPath=%VMWorkstationPath:~0,-1%

for /F "tokens=*" %%a in ('dir "%VMWorkstationPath%\*.vmdk" /a-d /b /s') do set VMDKPath=%%a
for /F "tokens=*" %%a in ('dir "%VMWorkstationPath%\*.vmdk" /a-d /b') do set VMDKName=%%a
set VMDKName=%VMDKNAME:~0,-5%
set timestamp=%date:~-4%%date:~-7,2%%date:~-10,2%_%time:~-11,2%%time:~-8,2%%time:~-5,2%

::-------------------------------------------------------------------------------------------

mkdir "%VMWorkstationPath%\snapshots"

:RUN
call :MENU
echo Bitte Auswaehlen:
echo 1) Snapshot erstellen
echo 2) Snapshot wiederherstellen
echo 3) Beenden

set /p choice=Auswahl (1/2/3): 

::-------------------------------------------------------------------------------------------


IF "%choice%"=="3" (
 GOTO :END
)ELSE (
 IF "%choice%"=="1" (
GOTO :SNAPCREATE
)ELSE ( 
 IF "%choice%"=="2" (
GOTO :SNAPRESTORE
) ELSE (
ECHO Bitte Auswahl treffen!
PAUSE
GOTO :RUN
)
)
)

:SNAPCREATE
call :MENU
echo -----------------------------------------------------Folgender Snapshot wird erstellt:-------------------------------------------------------------
echo Eingabedatei: "%VMDKPath%"
Echo Ausgabedatei: "%VMWorkstationPath%\snapshots\%VMDKName%_%timestamp%.7z"
::-------------------------------------------------------------------------------------------
IF NOT EXIST "%VMDKPath%" (
  call :MENU
  ECHO Keine VMDK-Datei gefunden!
  echo -------------------------------------------------------------------------------------------------------------------------------------------------
  Pause
  GOTO :RUN
)

IF EXIST "%VMDKPath%" (
 set /p description=Snapshotbeschreibung: 
 ECHO !description!>"%VMWorkstationPath%\snapshots\%VMDKName%_%timestamp%.txt"
 REM echo ----------------------------------------------------------------------------------------
 echo Snapshot erstellen
 "%VMWorkstationPath%\7z\7z.exe" a -t7z -m0=lzma2:d1024m -mx=9 -aoa -mfb=64 -md=32m -ms=on "%VMWorkstationPath%\snapshots\%VMDKName%_%timestamp%.7z" "%VMDKPath%" 
 REM robocopy "%VMWorkstationPath%" "%VMWorkstationPath%\snapshots" "%VMDKName%.vmdk"
 REM ren "%VMWorkstationPath%\snapshots\%VMDKName%.vmdk" "%VMDKName%_%timestamp%.vms"
 echo ---------------------------------------------------------------------------------------------------------------------------------------------------
 Pause
 GOTO :RUN
)



:SNAPRESTORE
call :MENU
echo -----------------------------------------------------Folgende Snapshots existieren:----------------------------------------------------------------
REM dir "%VMWorkstationPath%\snapshots\*.vms" /B /A-D
dir "%VMWorkstationPath%\snapshots\*.7z" /B /A-D
echo ---------------------------------------------------------------------------------------------------------------------------------------------------

set /p dateiname=Bitte Snapshot zum Wiederherstellen eingeben:

IF "%dateiname%"=="" (
 ECHO Bitte Snapshot auswaehlen!
 PAUSE
 GOTO :SNAPRESTORE
)

IF NOT EXIST "%VMWorkstationPath%\snapshots\%dateiname%" (
  call :MENU
  ECHO Datei "%VMWorkstationPath%\snapshots\%dateiname%" existiert nicht
  echo ---------------------------------------------------------------------------------------------------------------------------------------------------
  Pause
  GOTO :RUN
)
 
IF EXIST "%VMWorkstationPath%\snapshots\%dateiname%" (
GOTO :SNAP
)

:SNAP
cls
::-------------------------------------------------------------------------------------------
  call :MENU
  echo Der Snapshot %dateiname% wird wiederhergestellt.
  set txtfile=%dateiname:~0,-3%.txt
  set /p description=<"%VMWorkstationPath%\snapshots\%txtfile%" 
  echo Snappshotbeschreibung: !description!
 
  set /p confirm="ACHTUNG dies ueberschreibt die originale VMDK-Datei. Sind Sie sicher (J/N)? "
  IF NOT %confirm%==J (
  echo ---------------------------------------------------------------------------------------------------------------------------------------------------
  Pause
  GOTO :RUN
  )  


  IF %confirm%==J (
    echo ---------------------------------------------------------------------------------------------------------------------------------------------------
    echo Snapshot zurueckspielen
    REM copy "%VMWorkstationPath%\snapshots\%dateiname%" "%VMWorkstationPath%\%VMDKName%.vmdk" /z /y
    "%VMWorkstationPath%\7z\7z.exe" x "%VMWorkstationPath%\snapshots\%dateiname%" -y -o"%VMWorkstationPath%"
    echo ---------------------------------------------------------------------------------------------------------------------------------------------------
    Pause
    GOTO :RUN
   )

:END
 echo ---------------------------------------------------------------------------------------------------------------------------------------------------
 echo ###################################################################################################################################################
 goto :eof
 
 :MENU
::-------------------------------------------------------------------------------------------
cls
echo ###################################################################################################################################################
echo ################################################### ________________________________________ ######################################################
echo ###################################################^|VM Workstation Player Snapshotverwaltung^|######################################################
echo ###################################################^|                 V. 1.1                 ^|######################################################
echo ###################################################^|            ©2019 Oliver Jung           ^|######################################################
echo ###################################################^|________________________________________^|######################################################
echo ###################################################                                          ######################################################
echo ###################################################################################################################################################
echo ---------------------------------------------------------------------------------------------------------------------------------------------------
goto :eof