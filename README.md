# VM_Snapshot_Manager
 Manager for VM Snapshots of vmdk or vdi files used by VM Workstation or Virtualbox


## Overview
This Package contains a python-program which can be copied on any windows, linux or mac computer to create Snapshots of vdi or vmdk files using high compression of 7zip


## Purpose of this Project
Why using this project instead of the build in Snapshot-Manager of Virtualbox?

Well, first of all, this program was developed as a quick and dirty solution for VM Workstation Player which doesn't even have the option to create Snapshots.

But furthermore I discovered that even with Virtualbox it is better if you store your snapshots as 7Zip-compressed 1:1 copies of your full vdi or vmdk File. Virtualbox splits the data in a complex manner if you create snapshots there which makes it quick to create one but takes also a long time to restore. And you always need the whole tree of snapshots if you want to clone or move your VM - you can't just take your .vdi File, ignore all the Snapshot-Files and mount it in a new machine as Hard Drive - the data won't be the same as your last working point in the old machine.

But if you don't do snapshots with the programm at all und use this tool instead, you always keep your min vdi or vmdk File 100% comnplete and movable.

Plus, my snapshots are high compressed with 7Zip which can lead up to 50% less storage needed for them. Yes it takes longer to create them and also longer to restore - but you will always be on the save site with this tool instead of using the complex and storage intense snapshot-tree-solution of virtualbox.



### Installation
#### 1. Download
Download and unpack the project

#### 2. Batch or Python
Decide weather you want to go with the original batch-script which only works on windows but has a nice terminal design - or if you want the python-version on linux and mac systems.

#### 3. For Batch-User only
* Only if you want to use the Batch-File Solution  
* Copy the "VMSnapshot.cmd" File in the Folder where your VMDK or VDI File of your virtual machine is stored.
* if you use VDI-Files: Open the .cmd File with a text editor and search and replace all ".vmdk" mentions with ".vdi"

#### 4. For Linux or Mac:
  * If you use Linux or Mac or if you want to use the python-version of VM Snapshot Manager also in windows
  * Create a Folder "VM_Snpapshot_Manager" in the Folder where your VMDK or VDI File of your virtual machine is stored
  * Copy all the Files of this repository into this new Folder
  * if you use VDI-Files: Open the "VMDK.py" File with a Text editor and edit the value of the variable "VirtualDevice" to ".vdi" (Line 15)

#### 5. Install 7Zip
* For the Batch-Version copy the portable Version of 7Zip into the Folder with your VMDK or VDI File and rename it to "7z". This is only for the Batch-Version for Python-Use you need to install 7zip fully in Windows
* For the Python-Version: Make sure you can run the normal "7z"-Command from your console.
  * On Windows you should install 7zip normal (not the portable Version) and try if you can execute it from your cmd-Shell
  * On Mac you first need to install Homebrew and than install p7zip with it. It's well described here: https://superuser.com/questions/548349/how-can-i-install-7zip-so-i-can-run-it-from-terminal-on-os-x
  * On Linux - well there are also many ways to go, as an example which will fit most users, if you have a ubuntu or ubuntu-flavored Linux running like Linux Mint, Kubuntu, elementary etc. you can look up here: https://wiki.ubuntuusers.de/7z/

#### 6. Install Python
  * If you don't go with the Batch-Solution but with the Python-Programm on Mac or Linux, you now have to download and install python: https://www.python.org/downloads/

### Usage
  * For the Batch-Version: Just run the Batch-File.
  * For the Python-Version: Just run the VMDK.py file in a terminal console, it's the main part of the program, you can run the script on mac with the command "python [/path/to/program/]VMDK.py - or on linux and windows with "py" instead of "python" as command in the terminal.
  * The Program is written in German only. If I get feedback and contribution that this tool should also be available in english just contact me:
  <wilfred85@protonmail.com>


So long and thanks for all the fish!
