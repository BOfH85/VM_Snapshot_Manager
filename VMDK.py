#-------------------------------------------------------------------------------------------
# VM Snapshotwiederherstellung V 1.2
# based on the .BAT Script "VMSnapsphot.cmd" with Version VM Snapshotwiederherstellung V 1.1
# (c) of BAT-Script: 10.08.2019 Oliver Jung
#
#  V 1.1 12.12.2019: Umstellung auf 7Zip-Compress. @Oliver Jung 
#  V 1.2 10.01.2020: Umstellung und Umprogrammierung auf Python-Script @Oliver Jung
#-------------------------------------------------------------------------------------------

#Import-Files for Python
import os, time, platform
import run as run

#Declare Variables
VMWorkstationPath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
#VMWorkstationPath=os.path.dirname(os.path.realpath(__file__))
VMDKPath=""
VMDKName=""
for file in os.listdir(VMWorkstationPath):
	if file.endswith(".vmdk"):
		VMDKPath=(os.path.join(VMWorkstationPath, file))
		VMDKName=file
		VMDKName=VMDKName[0:-5]

timestamp=os.path.join(time.strftime("%Y%m%d"))+"_"+time.strftime("%H%M%S")		

#Determine Cleanscreen for Operating System
operating_system=platform.system()
cleanscreen="clear"
if (operating_system == "Windows"):
	cleanscreen="cls"
  #  ctypes.windll.kernel32.SetConsoleTitleW("VM Workstation Player Snapshotverwaltung V 1.2  (c)2020 Oliver Jung")


#Create Folder
if not os.path.exists(os.path.join(VMWorkstationPath, "snapshots")):
    os.mkdir(os.path.join(VMWorkstationPath, "snapshots"))	

run.run(cleanscreen, VMDKPath, VMWorkstationPath, VMDKName, timestamp)
 
