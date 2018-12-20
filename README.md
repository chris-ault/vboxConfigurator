# vboxConfigurator

Problem
-----------
Virtualbox does not allow you to migrate your snapshots to a new location and requires manual modification of the xml files.


Solution
---------
The vboxConfigurator allows you to migrate your VM, snapshots and virtual disks to a new drive or directory and automatically updates xml config files to reflect the changes.

Requires
---------
Requires 
python 2.7, xmltodict
python -m pip install xmltodict