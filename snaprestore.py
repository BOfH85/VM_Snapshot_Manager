#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.2
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung 
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#-------------------------------------------------------------------------------------------

import os, glob
import menu as menu
import pause as pause
import snap as snap
def snaprestore(VMWorkstationPath, cleanscreen, version):
    dateiname=""
    running=1
    name=""
    
    while running == 1:
        menu.menu(cleanscreen)
        print("-------------------------Folgende Snapshots existieren:------------------------")
        for name in glob.glob(os.path.join(VMWorkstationPath, "snapshots", "")+"*.7z"):
            print(name)

        print("-------------------------------------------------------------------------------")
        if version < "3":
            dateiname = raw_input("Bitte Snapshot zum Wiederherstellen eingeben: ")
        else:
            dateiname = input("Bitte Snapshot zum Wiederherstellen eingeben: ")
            
        if name == "":
            print("Keine Snapshots gefunden!")
            pause.pause(version)
            running=0
            
        elif dateiname == "" and running == 1:
            print("Bitte Snapshot auswaehlen!")
            pause.pause(version)
            running=0

        elif (not os.path.isfile(os.path.join(VMWorkstationPath, "snapshots", dateiname)) and running == 1):
            menu.menu(cleanscreen)
            print("Datei "+os.path.join(VMWorkstationPath, "snapshots", dateiname)+" existiert nicht")
            print("-------------------------------------------------------------------------------")
            pause.pause(version)
            running=0
			
        elif dateiname != "" and running == 1 and name != "":
            running=0
            snap.snap(dateiname, cleanscreen, VMWorkstationPath, version)

        else:
            print("Test")
            pause.pause(version)
