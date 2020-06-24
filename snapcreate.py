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
def snapcreate( cleanscreen, VMDKPath, VMWorkstationPath, VMDKName, timestamp, version ):
    menu.menu(cleanscreen)
    print("-----------------------Folgender Snapshot wird erstellt:-----------------------")
    print("Eingabedatei: "+VMDKPath)
    Ausgabedatei=os.path.join(VMWorkstationPath, "snapshots", "")+VMDKName+"_"+timestamp+".7z"
    print("Ausgabedatei: "+Ausgabedatei)
    if not os.path.isfile(VMDKPath):
        menu.menu(cleanscreen)
        print("Keine VMDK-Datei gefunden!")
        print ("-------------------------------------------------------------------------------")
        pause.pause(version)
    else:
        if version < "3":
            confirm=raw_input("Snapshot jetzt erstellen (J/N)? ")
        else:
            confirm=input("Snapshot jetzt erstellen (J/N)? ")

        if confirm == "J":
            if os.path.isfile(VMDKPath):
                if version < "3":
                    description= raw_input("Snapshotbeschreibung: ")
                else:
                    description= input("Snapshotbeschreibung: ")
                    descfile = open(os.path.join(VMWorkstationPath, "snapshots", "")+VMDKName+"_"+timestamp+".txt","w")
                    descfile.write(description)
                    print("Snapshot erstellen")
                    print("7z a -t7z -m0=lzma2:d1024m -mx=9 -aoa -mfb=64 -md=32m -ms=on \""+Ausgabedatei+"\" \""+VMDKPath+"\"")
                    os.system("7z a -t7z -m0=lzma2:d1024m -mx=9 -aoa -mfb=64 -md=32m -ms=on \""+Ausgabedatei+"\" \""+VMDKPath+"\"")
                    print("-------------------------------------------------------------------------------")
                    pause.pause(version)
        else:
            print("-------------------------------------------------------------------------------")
            print("Snapshoterstellung abgebrochen")
            pause.pause(version)
