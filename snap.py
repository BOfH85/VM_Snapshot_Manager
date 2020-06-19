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
    print("Der Snapshot "+dateiname+" wird wiederhergestellt.")
    txtfile=dateiname[0:-2]+"txt"
    descfile = open(os.path.join(VMWorkstationPath, "snapshots", txtfile), "r")
    description=descfile.read()
    print("Snappshotbeschreibung: "+description)
    pause.pause(version)
    if version < "3":
        confirm=raw_input("ACHTUNG - ueberschreibt die originale VMDK/VDI-Datei! Sind Sie sicher (J/N)? ")
    else:
        confirm=input("ACHTUNG - ueberschreibt die originale VMDK/VDI-Datei! Sind Sie sicher (J/N)? ")
        
    if confirm == "J":
        print("-------------------------------------------------------------------------------")
        print("Snapshot zurueckspielen")
        print("7z x \""+os.path.join(VMWorkstationPath, "snapshots", dateiname)+"\" -y -o\""+VMWorkstationPath+"\"") 
        os.system("7z x \""+os.path.join(VMWorkstationPath, "snapshots", dateiname)+"\" -y -o\""+VMWorkstationPath+"\"") 
        # !! "%VMWorkstationPath%\7z\7z.exe" x "%VMWorkstationPath%\snapshots\%dateiname%" -y -o"%VMWorkstationPath%"
        print("-------------------------------------------------------------------------------")
        pause.pause(version)
        
    else:
        print("-------------------------------------------------------------------------------")
        print("Wiederherstellung abgebrochen")
        pause.pause(version)

def dele(dateiname, cleanscreen, VMWorkstationPath, version):
    os.system(cleanscreen)
    menu.menu(cleanscreen)
    print("Der Snapshot "+dateiname+" wird geloescht.")
    txtfile=dateiname[0:-2]+"txt"
    descfile = open(os.path.join(VMWorkstationPath, "snapshots", txtfile), "r")
    description=descfile.read()
    descfile.close()
    print("Snappshotbeschreibung: "+description)
    pause.pause(version)
    if version < "3":
        confirm=raw_input("ACHTUNG - Snapshot wird dauerhaft geloescht - Sind Sie sicher (J/N)? ")
    else:
        confirm=input("ACHTUNG - Snapshot wird dauerhaft geloescht - Sind Sie sicher (J/N)? ")
        
    if confirm == "J":
        print("-------------------------------------------------------------------------------")
        print(os.path.join(VMWorkstationPath, "snapshots", txtfile))
        print(os.path.join(VMWorkstationPath, "snapshots", dateiname))
        os.remove(os.path.join(VMWorkstationPath, "snapshots", txtfile))
        os.remove(os.path.join(VMWorkstationPath, "snapshots", dateiname))
        print("Snapshot geloescht")
        print("-------------------------------------------------------------------------------")
        pause.pause(version)
        
    else:
        print("-------------------------------------------------------------------------------")
        print("Loeschen abgebrochen")
        pause.pause(version)
    

