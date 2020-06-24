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
  * Download and unpack the project in a folder which is in the same directory where your VMDK or VDI File is stored. Don't extract the project files in the same directory like the VMDK or VDI File, make sure they are in a sub-folder in this directory like "C:\Users\User\Documents\Virtualox\Virtualmachine\VM_Snapshot_Manager" - if "Virtualmachine" is the directory where your VDMK or VDI File is stored

#### 2. VMDK or VDI?
  * If you use VDI-Files: Open the "VM_Snapshot_Manager.py" File with a Text editor and edit the value of the variable "VirtualDevice" to ".vdi" (Line 15)
  * Save the file and exit the text editor

#### 3. Install 7Zip
  * Make sure you can run the normal "7z"-Command from your console.
  * On Windows you should install 7zip (not the portable Version) and try if you can execute "7z" from your cmd-Shell
  * On Mac you first need to install Homebrew and than install p7zip with it. It's well described here: https://superuser.com/questions/548349/how-can-i-install-7zip-so-i-can-run-it-from-terminal-on-os-x
  * On Linux there are many ways to go, as an example which will fit most users, if you have a ubuntu or ubuntu-flavored Linux running like Linux Mint, Kubuntu, elementary etc. you can look up here: https://wiki.ubuntuusers.de/7z/

#### 4. Install Python
  * If you don't already have it on your system you now have to download and install python: https://www.python.org/downloads/

### Usage
  * Just run the VM_Snapshot_Manager.py file - it's the main part of the program, you can run the script on mac with the command "python [/path/to/program/]VMDK.py - or on linux and windows with "py" instead of "python" as command in the terminal.
  * On Linux: If you make the file executable it should be able to open with double-click, I also suggest you create a .desktop Starter File for it
  * On Windows: Program should be executable with double-click, I also suggest you create a Shortcut for it
  * The Program is written in German only. If I get feedback and contribution that this tool should also be available in english just contact me:
  <wilfred85@protonmail.com>


So long and thanks for all the fish!
