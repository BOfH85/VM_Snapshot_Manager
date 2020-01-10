# VM_Snapshot_Manager
 Manager for VM Snapshots of vmdk or vdi files used by VM Workstation or Virtualbox


## Overview
This Package contains a python-program which can be copied on any windows, linux or mac computer to create Snapshots of vdi or vmdk files using high compression of 7zip


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
  * The Program is written in German only. If I get feedback and contribution that this tool should also be available in english just contact me:
  <wilfred85@protonmail.com>


So long and thanks for all the fish!
