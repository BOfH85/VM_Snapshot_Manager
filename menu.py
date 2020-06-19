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
def menu(cleanscreen):
	os.system(cleanscreen)
	print("################################################################################")
	print("################### ________________________________________ ###################")
	print("##################^|VM Workstation Player Snapshotverwaltung^|##################")
	print("##################^|                 V. 1.3                 ^|##################")
	print("##################^|            (c)2020 Oliver Jung         ^|##################")
	print("##################^|________________________________________^|##################")
	print("###################                                          ###################")
	print("################################################################################")
