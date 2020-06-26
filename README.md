# VM_Snapshot_Manager
 Manager for VM Snapshots of vmdk or vdi files used by VM Workstation or Virtualbox


## Overview
This Package contains a python-program which can be copied on any windows, linux or mac computer to create Snapshots of vdi or vmdk files using high compression of 7zip


## Purpose of this Project
Why using this project instead of the build in Snapshot-Manager of Virtualbox?

Well, first of all, this program was developed as a quick and dirty solution for VM Workstation Player which doesn't even have the option to create Snapshots.

But furthermore I discovered that even with Virtualbox it is better if you store your snapshots as 7Zip-compressed 1:1 copies of your full vdi or vmdk File. Virtualbox splits the data in a complex manner if you create snapshots there which makes it quick to create one but takes also a long time to restore. And you always need the whole tree of snapshots if you want to clone or move your VM - you can't just take your .vdi File, ignore all the Snapshot-Files and mount it in a new machine as Hard Drive - the data won't be the same as your last working point in the old machine.

But if you don't do snapshots with the programm at all und use this tool instead, you always keep your vdi or vmdk File 100% comnplete and movable.

Plus, my snapshots are high compressed with 7Zip which can lead up to 50% less storage needed for them. Yes it takes longer to create them and also longer to restore - but you will always be on the save site with this tool instead of using the complex and storage intense snapshot-tree-solution of virtualbox.



### Installation
#### 1. Download
  * Download and unpack the project in a folder which is in the same directory where your VMDK or VDI File is stored. Don't extract the project files in the same directory like the VMDK or VDI File, make sure they are in a sub-folder in this directory like "C:\Users\User\Documents\Virtualox\Virtualmachine\VM_Snapshot_Manager" - if "Virtualmachine" is the directory where your VDMK or VDI File is stored

#### 2. VMDK or VDI?
  * If you use VDI-Files: Open the "VM_Snapshot_Manager.py" File with a Text editor and edit the value of the variable "VirtualDevice" to ".vdi" (Line 15)
  * Save the file and exit the text editor

#### 3. Install 7Zip
  * On Linux there are many ways to go, as an example which will fit most users, if you have a ubuntu or ubuntu-flavored Linux running like Linux Mint, Kubuntu, elementary etc. you can look up here: https://wiki.ubuntuusers.de/7z/
  * On Mac you first need to install Homebrew (https://brew.sh/) and than install p7zip with it. It's well described here: https://superuser.com/questions/548349/how-can-i-install-7zip-so-i-can-run-it-from-terminal-on-os-x
  * On Windows you should install 7zip (!not the portable Version!) from here: https://www.7-zip.org

#### 4. Install Python
  * Installation Instructions for Linux Users: https://wiki.ubuntuusers.de/Python/
  * Windows Users just download and install the newest version from here: https://www.python.org/downloads/
  * Mac already has Python on Board but if you want you can download the newest Version too from the Link above. In that case you can run the program with the Python Launcher, otherwise if you use the default python version which comes with macOS see Instructions in Section "Usage" below.

### 5. Environment Variables
  * On Windows you also need to add 7Zip and Python  to your PATH Environment Variables. For this just:
     * Open C:\Users\\[User]\AppData\Local\Programs\Python\  - Replace "[User]" with your current User
     * Copy the Folder within (Either "Python38" or newer) to C:\ (Means you copy for Example C:\Users\\[User]\AppData\Local\Programs\Python\Python38 to C:\Python38 )
     * Sart the Run box and enter sysdm.cpl
     * This should open up the System Properties window. Go to the Advanced tab and click the Environment Variables button
     * In the System variable window, find the Path variable and click Edit
     * Add a new Entry: C:\Python38
     * Add a new Entry: C:\Program Files\7-Zip
     * Restart

### Usage
To Start the program you need to run the "VM_Snapshot_Manager.py" file - it's the main part of the program.

  * On Windows: Program should be executable with double-click out of the box, I  suggest you simple create a Shortcut for it - this is not necessarry but gives you more options like setting a profile on terminal size, colours etc.
  * On Linux and Mac: There exists a file called "VM_Snapshot_Manager_starter.sh" with the following content:
  ```
  #!/bin/bash
  BASEDIR=$(dirname "$0")
  python $BASEDIR/VM_Snapshot_Manager.py
  ```
  To make it executable just run the command
  ```
  chmod +x /path/to/VM_Snapshot_Manager_starter.sh

  ```
    * Special for Linux: For more comfort I suggest you also create a `.destkop` file to execute the program - this is not necessarry but gives you more options like setting a profile on terminal size, colours etc. It's the equivalent of a Shortcut in Windows. The File could look like the following:
  ```
   [Desktop Entry]
   Name=VM Snapshot Manager
   Exec=python /path/to/VM_Snapshot_Manager.py
   Terminal=true
   Type=Application
  ```

    * On Mac: If you also want to start the program via double-click like on Linux or Windows, just rename the `VM_Snapshot_Manager_starter.sh` File to `VM_Snapshot_Manager_starter.command`. You than can make an alias vor it which is the same lika a shortcut in Windows.


Of course beside these methods you always can run the script via
  ```
  python /path/to/VM_Snapshot_Manager.py
  ```
from any console (cmd.exe on windows or a normal terminal console in Linux or Mac)




So long and thanks for all the fish!
