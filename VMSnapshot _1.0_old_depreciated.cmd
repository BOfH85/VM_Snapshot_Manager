@echo off
setlocal enabledelayedexpansion
:: VM Snapshotwiederherstellung V 1.0
:: (c) 10.08.2019 Oliver Jung

:Variable erzeugen
::-------------------------------------------------------------------------------------------
set VMWorkstationPath=%~dp0
set VMWorkstationPath=%VMWorkstationPath:~0,-1%

for /F "tokens=*" %%a in ('dir "%VMWorkstationPath%\*.vmdk" /a-d /b /s') do set VMDKPath=%%a
for /F "tokens=*" %%a in ('dir "%VMWorkstationPath%\*.vmdk" /a-d /b') do set VMDKName=%%a
set VMDKName=%VMDKNAME:~0,-5%
set timestamp=%date:~-10,2%%date:~-7,2%%date:~-4%_%time:~-11,2%%time:~-8,2%%time:~-5,2%
::-------------------------------------------------------------------------------------------

mkdir "%VMWorkstationPath%\snapshots"

:RUN
::-------------------------------------------------------------------------------------------
cls
::-------------------------------------------------------------------------------------------
echo ########################################################################################
echo ######################VM Workstation Player Snapshotverwaltung 1.0######################
echo ########################################################################################
echo ----------------------------------------------------------------------------------------
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
cls
::-------------------------------------------------------------------------------------------
echo ########################################################################################
echo ######################VM Workstation Player Snapshotverwaltung 1.0######################
echo ########################################################################################
echo ----------------------------------------------------------------------------------------
echo -----------------------------Folgender Snapshot wird erstellt:--------------------------
echo Eingabedatei: "%VMDKPath%"
Echo Ausgabedatei: "%VMWorkstationPath%\snapshots\%VMDKName%_%timestamp%.7z"
::-------------------------------------------------------------------------------------------
IF NOT EXIST "%VMDKPath%" (
  cls
  echo ########################################################################################
  echo ######################VM Workstation Player Snapshotverwaltung 1.0######################
  echo ########################################################################################
  echo ----------------------------------------------------------------------------------------
  ECHO Keine VMDK-Datei gefunden!
  echo ----------------------------------------------------------------------------------------
  Pause
  GOTO :RUN
)

IF EXIST "%VMDKPath%" (
 set /p description=Snapshotbeschreibung: 
 ECHO !description!>"%VMWorkstationPath%\snapshots\%VMDKName%_%timestamp%.txt"
 echo ----------------------------------------------------------------------------------------
 echo Snapshot erstellen
 %VMWorkstationPath%\7za.exe" a -mx0 "%VMWorkstationPath%snapshots\%VMDKName%_%timestamp%.7z" "%VMDKPath%"
 echo ----------------------------------------------------------------------------------------
 Pause
 GOTO :RUN
)



:SNAPRESTORE
cls
::-------------------------------------------------------------------------------------------
echo ########################################################################################
echo ######################VM Workstation Player Snapshotverwaltung 1.0######################
echo ########################################################################################
echo ----------------------------------------------------------------------------------------
echo -----------------------------Folgende Snapshots existieren:-----------------------------
dir "%VMWorkstationPath%\snapshots\*.7z" /B /A-D
echo ----------------------------------------------------------------------------------------

set /p dateiname=Bitte Snapshot zum Wiederherstellen eingeben:

IF "%dateiname%"=="" (
 ECHO Bitte Snapshot auswaehlen!
 PAUSE
 GOTO :SNAPRESTORE
)

IF NOT EXIST "%VMWorkstationPath%\snapshots\%dateiname%" (
  cls
  echo ########################################################################################
  echo ######################VM Workstation Player Snapshotverwaltung 1.0######################
  echo ########################################################################################
  echo ----------------------------------------------------------------------------------------
  ECHO Datei "%VMWorkstationPath%\snapshots\%dateiname%" existiert nicht
  echo ----------------------------------------------------------------------------------------
  Pause
  GOTO :RUN
)
 
IF EXIST "%VMWorkstationPath%\snapshots\%dateiname%" (
GOTO :SNAP
)

:SNAP
cls
::-------------------------------------------------------------------------------------------
echo ########################################################################################
echo ######################VM Workstation Player Snapshotverwaltung 1.0######################
echo ########################################################################################
echo ----------------------------------------------------------------------------------------
  echo Der Snapshot %dateiname% wird wiederhergestellt.
  set txtfile=%dateiname:~0,-3%txt
  set /p description=<"%VMWorkstationPath%\snapshots\%txtfile%" 
  echo Snappshotbeschreibung: !description!
 
  set /p confirm="ACHTUNG dies ueberschreibt die originale VMDK-Datei. Sind Sie sicher (J/N)? "
  IF NOT %confirm%==J (
  echo ----------------------------------------------------------------------------------------
  Pause
  GOTO :RUN
  )  


  IF %confirm%==J (
    echo ----------------------------------------------------------------------------------------
    echo Snapshot zurueckspielen
    "%VMWorkstationPath%\7za.exe" x "%VMWorkstationPath%\snapshots\%dateiname%" -y -o"%VMWorkstationPath%"
    echo ----------------------------------------------------------------------------------------
    Pause
    GOTO :RUN
   )


:END
 echo ----------------------------------------------------------------------------------------
 echo ########################################################################################