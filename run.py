#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.2
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung 
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#-------------------------------------------------------------------------------------------

import end as end
import snapcreate as snapcreate
import snaprestore as snaprestore
import pause as pause
import menu as menu

def run(cleanscreen, VMDKPath, VMWorkstationPath, VMDKName, timestamp ):
	running=1
	while running ==1:
		menu.menu(cleanscreen)
		#print VMWorkstationPath
		print("Bitte Auswaehlen:")
		print("1) Snapshot erstellen")
		print("2) Snapshot wiederherstellen")
		print("3) Beenden")
		choice=raw_input("Auswahl (1/2/3): ")


		if choice =="3":
			running=0
			end.end()
		
		elif choice == "1":
			snapcreate.snapcreate(cleanscreen, VMDKPath, VMWorkstationPath, VMDKName, timestamp)

		elif choice == "2":
			snaprestore.snaprestore(VMWorkstationPath, cleanscreen)
	
		else:
			print("Bitte Auswahl treffen!")
			pause.pause()
