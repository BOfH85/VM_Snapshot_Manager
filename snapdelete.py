#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.3
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#  V 1.3 19.06.2020: Einfuegen von Loeschoption fuer Snaps @Oliver Jung
#-------------------------------------------------------------------------------------------

import os, glob
import menu as menu
import pause as pause
import snap as snap

def snapdelete(VMWorkstationPath, cleanscreen, version):
    dateiname=""
    running=1
    name=""

    while running == 1:
        menu.menu(cleanscreen)
        print("-------------------------Following Snapshots exists:---------------------------")
        for name in glob.glob(os.path.join(VMWorkstationPath, "snapshots", "")+"*.7z"):
            print(name+" Size: "+str(round(((os.stat(os.path.join(VMWorkstationPath, "snapshots", name)).st_size)/1000000000), 2))+" GB")

        print("-------------------------------------------------------------------------------")
        if version < "3":
            dateiname = raw_input("Please select Snapshot to delete: ")
        else:
            dateiname = input("Please select Snapshot to delete: ")

        if name == "":
            print("No Snapshots found!")
            pause.pause(version)
            running=0

        elif dateiname == "" and running == 1:
            print("Please select Snapshot!")
            pause.pause(version)
            running=0

        elif (not os.path.isfile(os.path.join(VMWorkstationPath, "snapshots", dateiname)) and running == 1):
            menu.menu(cleanscreen)
            print("File "+os.path.join(VMWorkstationPath, "snapshots", dateiname)+" does not exist!")
            print("-------------------------------------------------------------------------------")
            pause.pause(version)
            running=0

        elif dateiname != "" and running == 1 and name != "":
            running=0
            snap.dele(dateiname, cleanscreen, VMWorkstationPath, version)

        else:
            print("Test")
            pause.pause(version)
