#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.3
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#  V 1.3 19.06.2020: Einfuegen von Loeschoption fuer Snaps @Oliver Jung
#-------------------------------------------------------------------------------------------

import os
import menu as menu
import pause as pause
def snap(dateiname, cleanscreen, VMWorkstationPath, version):
    os.system(cleanscreen)
    menu.menu(cleanscreen)
    print("Snapshot "+dateiname+" will be restores.")
    txtfile=dateiname[0:-2]+"txt"
    descfile = open(os.path.join(VMWorkstationPath, "snapshots", txtfile), "r")
    description=descfile.read()
    print("Snappshot description: "+description)
    pause.pause(version)
    if version < "3":
        confirm=raw_input("WARNING - this will override the original VMDK/VDI-File! Are you sure (Y/N)? ")
    else:
        confirm=input("WARNING - this will override the original VMDK/VDI-File! Are you sure (Y/N)? ")

    if confirm == "Y":
        print("-------------------------------------------------------------------------------")
        print("Restore Snapshot")
        print("7z x \""+os.path.join(VMWorkstationPath, "snapshots", dateiname)+"\" -y -o\""+VMWorkstationPath+"\"")
        os.system("7z x \""+os.path.join(VMWorkstationPath, "snapshots", dateiname)+"\" -y -o\""+VMWorkstationPath+"\"")
        # !! "%VMWorkstationPath%\7z\7z.exe" x "%VMWorkstationPath%\snapshots\%dateiname%" -y -o"%VMWorkstationPath%"
        print("-------------------------------------------------------------------------------")
        pause.pause(version)

    else:
        print("-------------------------------------------------------------------------------")
        print("Cancel Restore")
        pause.pause(version)

def dele(dateiname, cleanscreen, VMWorkstationPath, version):
    os.system(cleanscreen)
    menu.menu(cleanscreen)
    print("Snapshot "+dateiname+" will be deleted.")
    txtfile=dateiname[0:-2]+"txt"
    descfile = open(os.path.join(VMWorkstationPath, "snapshots", txtfile), "r")
    description=descfile.read()
    descfile.close()
    print("Snappshot description: "+description)
    pause.pause(version)
    if version < "3":
        confirm=raw_input("WARNING - Snapshot will be deleted permanently - Are you sure (Y/N)? ")
    else:
        confirm=input("WARNING - Snapshot will be deleted permanently - Are you sure (Y/N)? ")

    if confirm == "Y":
        print("-------------------------------------------------------------------------------")
        print(os.path.join(VMWorkstationPath, "snapshots", txtfile))
        print(os.path.join(VMWorkstationPath, "snapshots", dateiname))
        os.remove(os.path.join(VMWorkstationPath, "snapshots", txtfile))
        os.remove(os.path.join(VMWorkstationPath, "snapshots", dateiname))
        print("Snapshot deleted")
        print("-------------------------------------------------------------------------------")
        pause.pause(version)

    else:
        print("-------------------------------------------------------------------------------")
        print("Cancel Snapshot Delete")
        pause.pause(version)
