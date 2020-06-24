#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.3
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#  V 1.3 19.06.2020: Einfuegen von Loeschoption fuer Snaps @Oliver Jung
#-------------------------------------------------------------------------------------------

import end as end
import snapcreate as snapcreate
import snaprestore as snaprestore
import snapdelete as snapdelete
import pause as pause
import menu as menu

def run(cleanscreen, VMDKPath, VMWorkstationPath, VMDKName, timestamp, version):
	running=1
	while running ==1:
		menu.menu(cleanscreen)
		#print VMWorkstationPath
		print("Please select:")
		print("1) Create Snapshot")
		print("2) Restore Snapshot")
		print("3) Delete Snapshot")
		print("4) Close")
		if version < "3":
                        choice=raw_input("Select (1/2/3/4): ")
		else:
                        choice=input("Select (1/2/3/4): ")

		if choice =="4":
			running=0
			end.end()

		elif choice == "1":
			snapcreate.snapcreate(cleanscreen, VMDKPath, VMWorkstationPath, VMDKName, timestamp, version)

		elif choice == "2":
			snaprestore.snaprestore(VMWorkstationPath, cleanscreen, version)

		elif choice == "3":
			snapdelete.snapdelete(VMWorkstationPath, cleanscreen, version)

		else:
			print("Please make a selection!")
			pause.pause(version)
