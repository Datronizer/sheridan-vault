# Super user account - root user
Root account is the most powerful account in a system. You can literally do anything as a superuser. You SHOULD NOT be using the ROOT ACCOUNT for day-to-day things. BE REALLY CAREFUL.

## Switch user
Use `su` to switch to a different user on the same system.
Use `sudo su` to switch to the superuser account.
## Executing privileged commands
The `sudo` command also allows users to execute commands as another user.
This can be used in distros that do not allow root user login.
Running `sudo` will prompt the user for their own password rather than that of the root user.

>[!note] For security reasons, running `sudo` automatically results in an entry placed in a log file for accountability and reduces risk associated with using root.

# Linux boot process
6 stages:
- BIOS: **B**asic **I**nput/**O**utput **S**ystem. This executes MBR
	- Part of the motherboard, yes, literally embedded in the mb.
	- Performs system integrity check (checks that all hardware parts are working)
	- Searches, loads, and executes the Boot Loader Program.
	- You can interrupt this process by hitting a button 
		- This is different for every manufacturer. I don't know why, this is fucking stupid.
		- Do this to change the boot sequence.
- MBR: Master Boot Record
	- Located in the 1st sector of the disk--first thing to load right after BIOS
	- Less than 512 bytes in size
	- Contains information about the boot loader (GRUB, LILO for Linux)
- Boot loader
	- GRUB: Grand Unified Bootloader
	- If you have multiple kernel images, you can choose which one will be executed by grub.
- Kernel
	- Mounts the root file system
	- Executes the `/sbin/init` program
		- It is the first program to be executed by Linux, so it has the process ID (PID) of 1.
- `init`/`systemd`
	- These are both init daemons but it is better to use `systemd` since it is commonly used in recent Linux Distros.
		- Systemd is a system and service manager for Linux
	- Designed to be backwards-compatible with SysV init scripts and used by many popular distros like Debian 8+, Ubuntu 15.04+, Fedora, Redhat 7+, Arch, OpenSUSE, etc.
- Run levels & System targets
	- In SysVinit systems, you have a defined but configurable set of runlevels numbered from 0 -> 6.
		- 0: Shutdown
		- 1: Rescue: configures a rescue shell session
		- 2: Multi-user target: CLI, no network
		- 3: Multi-user target: CLI, w/ network
		- 4: Multi-user target: "customizable" (this is really not clear according to Nikolai)
		- 5: Graphical target: GUI, w/ network
		- 6: Reboot. 
	- Do `init [level]` to go to the level that you want.
	- Do `systemctl get-default` to show current system target.
# File system
A file system is an organization of data 

## Journal
File system recovery feature. 
Let's say you want to save a file to the hard drive. Let's say the system crashes half way through the writing operation. Now your file is unstable and you have no clue where it is in the drive.

Introducing Journal. When you begin to write the file in the hard drive, Journal writes down where this file is in hard drive. If the system crashes, the journal entry will stay in the journal so the machine and recover the file system after the file system crashes. Else, it just deletes the entry!

## FAT
File Allocation Table.
This is a file system developed for personal computers and was the default filesystem for MS-DOS and Windows 9x OSes.
FAT uses a table that centralizaes the information about which areas belong to files, are free or possibly unusable, and where each file stored on the disk.
Super slow, super small storage (2TB tops, 4GB max file size).

New Technology File System (NTFS). Proprietary journaling file system for Windows
Massive storage and super high speed.

Extended File System EXT. Made for Linux kernel.
Can only handle up to 2GB per file

EXT2 (Second Extended File System)
Bigger but no jounal

EXT3
Now there's a Journal :D

EXT4
Current file system. Super secure, fast, and huge file sizes.

## FHS
Filesystem Hierarchy Standard

Do `ls -a` in `root`. Go on. Tell me what you see. You see a bunch of directories, but what do each of them do? Well, all these directories actually follow the FHS.

The FHS is an agreed upon standard for file names an directories. 
%% Take the table from the powerpoint. It's too much and I can't type that fast  %%

## Partitioning
Oh god

Partitioning is a way to divide a hard drive into many logical drives. Each of these partitions act like an independent drive and refers to a contiguous set of blocks on the drive.

And yes, saying each of these act like an independent drive is the same as saying each of these have their own filesystem.

Anyways, back to what I was saying:
- Take a disk, split that thing into pizza slices. 
- Each slice gets slices up even smaller. 
- Each of these itty bitty slices are called sectors. 
	- Each sector is 512 bytes. 
	- Each data block is a combination of a bunch of sectors. These two ARE NOT THE SAME
		- A data block could be 512B to 64kB, default is 4kB

Okay now let's do some real examples:

Let's say I have a 3kB file. If I choose a 64kB data block size to store this 3kB file, the other 61KB is wasted. You literally cannot use it. You cannot change it. You cannot fix it. The only way is to take this drive, reformat it, then reinstall it. 
This is called **Internal fragmentation**

Now let's say I have a 1MB file and a 4KB data block. Obviously I can't fit that into 1 block so I'll need to chop this file up a bunch and fit them into a bunch of data blocks. Of course chopping shit up and patching it together takes a long time, so we're better off using a 64KB block size for this case.

HOWEVER, THIS ONLY AFFECTS HDD, NOT SSD. This is because the HDD needs to spin the **plate** and the **reader** to the right segment, read it, edit it, whatever. Do that a thousand times, and the latency between each read mounts up exponentially. Shit takes a long time.

## Fragmentation
Fragmentation is a term used in reference to having "holes" on a disk.
Example:
Each of these numbers are a file segment.

| 1 | 1 | 2 | 2 | 2 |
| ---- | ---- | ---- | ---- | ---- |
| 3 | 3 | 4 | 4 |  |
Now if I delete file 3. I'll get:

|1|1|2|2|2|
|---|---|---|---|---|
| | |4|4||
Okay now if I add file 5, 3 segments long, watch what happens

| 1 | 1 | 2 | 2 | 2 |
| ---- | ---- | ---- | ---- | ---- |
| 5 | 5 | 4 | 4 | 5 |
5 is now a non-continuous file. This is called an **external fragmentation**. This is bad because it will slow down file processing and more. 
%% Fill this with PPTX information %%

fdisk for partition
mkfs makes filesystems
sudo mkfs -t ext4 [partitionName]
df -h shows filesystem and disk sizes, if ur disk is not there, it's probably not mounted (what's mounting? mounting is literally turning a directory into a hard drive. It's crazy. I love Linux)

Do sudo mkdir /media/vdb{1,2,3,4} to create 4 directories for your 4 drives. Due to FHS, we should put our drives into /media/ or /mnt/ for clarity.

To attach, do:
`sudo mount -t ext4 /dev/vdb1 /media/vdb1`
-t for type

Repeat that previous step 4 times for all 4 of your partitions

Mounting is temporary. If you reboot the system these mounts are gone.

Now let's do `ls -l /etc/fstab`. This opens the mounting table. Any partitions mounted here will be mounted permanently. Be warned. Don't mess with anything else in the file. Failure to mount your drives can cause crashes with your system.

DONT TOUCH THE FIRST 2 LINES PLEASE

Okay, now add your "mount points". Do `/dev/vdb1 /media/vdb1 ext4 defaults`
- Partition name
- Directory to mount to
- Filesystem type
- Mount as: readonly? Read+Write? etc?
- Dump. 0 means no backup if system utilities run. 1 is yes.
- System check order: Order in which it's checked. The first 2 lines are already 0 and 1 so naturally yours is 2+. They can all be the same btw.
- 
Now you can either reboot to mount (I recommend it) or just do `mount -a` to remount all your drives on `fstab`.

# Logical Volume Management (LVM)
Let's say the largest drive you can purchase is 24TB. Now think about Google or AWS. HOW THE FUCK DO THEY HAVE INFINITE STORAGE SPACE??

The answer is LVM. It pulls storage from every drive and grows the storage to a near infinite size. It can allocate storage/backup/scale up and down, etc.

There are 3 components:
- Physical volumes (PV)
	- Actual hard drives -> Split into partitions -> Mark partitions as physical volumes.
- Volume groups (VG)
	- Combines your PVs into volume groups. 
- Logical volumes (LV)
	- Splits the VG into logical volumes. You can now mount each of these into their own drives. You can literally turn 2 hard drives into "15" (quote unquote).