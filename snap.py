#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.2
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung 
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#-------------------------------------------------------------------------------------------

import os
import menu as menu
import pause as pause
def snap(dateiname, cleanscreen, VMWorkstationPath):
    os.system(cleanscreen)
    menu.menu(cleanscreen)
    print("Der Snapshot "+dateiname+" wird wiederhergestellt.")
    txtfile=dateiname[0:-2]+"txt"
    descfile = open(os.path.join(VMWorkstationPath, "snapshots", txtfile), "r")
    description=descfile.read()
    print("Snappshotbeschreibung: "+description)
    pause.pause()
    confirm=raw_input("ACHTUNG - ueberschreibt die originale VMDK/VDI-Datei! Sind Sie sicher (J/N)? ")
    
    if confirm == "J":
        print("-------------------------------------------------------------------------------")
        print("Snapshot zurueckspielen")
        os.system("7z x "+os.path.join(VMWorkstationPath, "snapshots", dateiname).replace(" ", "\\ ")+" -y -o"+VMWorkstationPath.replace(" ", "\\ ")) 
        # !! "%VMWorkstationPath%\7z\7z.exe" x "%VMWorkstationPath%\snapshots\%dateiname%" -y -o"%VMWorkstationPath%"
        print("-------------------------------------------------------------------------------")
        pause.pause()
        
    else:
        print("-------------------------------------------------------------------------------")
        print("Wiederherstellung abgebrochen")
        pause.pause()	
