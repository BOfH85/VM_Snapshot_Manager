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
def snaprestore(VMWorkstationPath, cleanscreen):
    dateiname=""
    running=1
    name=""
    while running == 1:
        menu.menu(cleanscreen)
        print("-------------------------Folgende Snapshots existieren:------------------------")
        for name in glob.glob(os.path.join(VMWorkstationPath, "snapshots", "")+"*.7z"):
            print name
            print("-------------------------------------------------------------------------------")
            dateiname = raw_input("Bitte Snapshot zum Wiederherstellen eingeben: ")

        if name == "":
            print("Keine Snapshots gefunden!")
            pause.pause()
            running=0
            
        if dateiname == "" and running == 1:
            print("Bitte Snapshot auswaehlen!")
            pause.pause()
            running=0

        if (not os.path.isfile(os.path.join(VMWorkstationPath, "snapshots", dateiname)) and running == 1 ):
			menu.menu(cleanscreen)
			print("Datei "+os.path.join(VMWorkstationPath, "snapshots", dateiname)+" existiert nicht")
			print("-------------------------------------------------------------------------------")
			pause.pause()
			#run()
        if dateiname != "" and running == 1 and name != "":
            running=0
            snap.snap(dateiname, cleanscreen, VMWorkstationPath)
