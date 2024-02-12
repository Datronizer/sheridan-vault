# Ownership, Permissions, and ACL
## Ownership
In Linux, everything is stored in files. A file is a file and a directory is also a file (that stores other files). Every file and folder in Linux is owned by a user and a group account.
- By default: users own the files they created
- By default, primary group of user who creates the files will be the owner of that account.

To check your id, do `id`. You should see something like this
```
uid=1000(trueongod) gid=1000(trueongod) groups=1000(trueongod),27(sudo) ...
```

Here `uid` is the account ID, `gid` is group ID. Now make a new file, do `touch f.txt`. Do `ls -la f.txt` to view who owns the file:
```
trueongod@phoenix-one:~$ ls -la f.txt 
-rw-r--r-- 1 trueongod trueongod 0 Feb  8 15:09 f.txt
```

Here it says user `trueongod` owns this file and users of group `trueongod` can access this. 

Doing sudo before making the file will say that the user and group are `root` and `root`.

`chown` changes the ownership of a file/directory to a different user/group. Doing `sudo chown root:root f.txt` should change the user to `root` and group to `root`.
- Doing `chown :trueongod f.txt` will transfer ownership to the group `trueongod`
- Doing `chown trueongod f.txt` will transfer ownership to the user `trueongod`

>[!note] Having owner ONLY gives you rights to GRANT PERMISSIONS.
>
>Having owner ONLY means you can decide what other users do to the file. It doesn't necessarily allow you to change it. You need to grant yourself permissions.

## File Types
Do `ls -l`. You should see some `-rwxr---w-` thing. The first character shows the following information.
- -: regular file (hard link)
- d: directory
- l: symbolic link
- c: character device file
- b: block device file (drive)
- s: socket file (network connections)
## Permissions
The 9 characters right after the first one are permissions. They are divided as such:
- First 3: user owner permissions
- Second 3: Group owner permissions
- Last 3: Others permissions

In each group, there are 3 permissions:
- `r`: read--Can view file content/contents within a directory
- `w`: write--Can edit, create, rename, delete files and subdirectories in a directory.
- `x`: execute--Can execute a file AND allows `cd` to the directory
## Understanding permissions
Let's say I check a file's permission. How do I know if I can access it?
%% ls -l file  and  id %%
%% cross reference  %%
## Changing permissions
Use `chmod` to change permissions. You can do this 2 ways:
- Symbolic mode: using characters
- Numeric mode: using octal numbers (hallelujah I know this)
Please don't combine methods, it doesn't work that way.
### Symbolic method
#### Specifiers
User types:
- u: user owner
- g: group owner
- o: others
- a: all (u + g + o)
All these can be combined. `ugo` is the same as `a`; `ug`, `uo`, `og`, etc.

Permissions:
- r: read
- w: write
- x: execute
These can also be combined

Operators:
- + add new peermissions on top of existing permissions
- - remove permission from existing permissions
- = replace permissions with new permissions
#### Syntax
`chmod [option]... mode `

Example:
`chmod a=- f.txt` replaces all permissions from all users with null.
`chmod u+r f.txt` gives user read permissions
`chmod u+w f.txt` gives user write permissions
`chmod u+x f.txt` gives user write permissions
`chmod u+rw,g=r,o-x f.txt` gives user read-write, group read, takes away others execute.

### Numeric method
The numeric method employs a 3 digit number.
- 1st digit: user
- 2nd digit: group
- 3rd digit: others

Each digit is in the range of 0 to 7 (haha, get it? Octal? There's 8 of them?)
- 4: read
- 2: write
- 1: execute
- 0: no perms

You can add numbers to do the same as chaining perms:
- 3 = 1 + 2: `-wx`
- 5 = 1 + 4: `r-x`
- 7 = 1 + 2 + 4: `rwx`
- etc.
#### Syntax
`chmod [option]... mode`

Example:
`chmod 000 f.txt` removes all rights from everyone
`chmod 755 f.txt` grants all rights to user, read execute to group, read execute to others.

## Special permissions
There are 3 more special perms:
### `setuid` (SUID)
So every password on Linux is stored on a while called shadow. Keep this in mind, we'll come back to it.

To change passwords, you use `passwd`. This command is a file in `/usr/bin/passwd`. Now check perms for this file. You should see `-rwsr-xr-x`. What is `s`? Don't worry about it yet.

Well let's go back to the shadow file. Do `ls -l` on that file, what do you see? Do you see `-rw-r-----`, with owner being `root`? It would make sense right? It's a file that stores everyone's passwords, a normal user should not even be allowed to access, let alone edit or execute a file. 

In that case, when you change your password, as a normal user, how does you password get written in `shadow` with no perms? The answer is that `s`: the `setuid` permission.

`s` here is `setuid`, set being past tense of set, meaning it has already been set. What does this mean? It means the current user is temporarily allowed to execute a file **as the owner of the file**. Typically, a normal user, when executing a file, does so as their own role. Which means, some files simply won't let you execute since they are owned by `root`. 

To circumvent this, you are granted temporary perms to execute the file as the owner, then after the execution finishes, you're back to your uid.

HOWEVER, the `s` in the first triplet applies ONLY to suid. The 2nd triplet is explained right after this.
### `setgid` (SGID)
Remember `setuid`? Yeah well this is for the group instead. Recall that `wall` (write all) is used to broadcast a message to all CLI users currently logged in.

%% fill in missing info  %%

### Sticky bits
%% users deleting each other's stuff  %%

Sticky bits basically says ONLY OWNERS can delete a file in a folder despite the perms carrying over from the dir.
### Setting special permissions
SUID:
- chmod u+s file OR chmod 4xxx file
- chmod u-s file OR chmod 0xxx file
GUID:
- chmod g+s file OR chmod 2xxx file
- chmod g-s file OR chmod 0xxx file
Sticky Bit:
- chmod o+t file OR chmod 1xxx file
- chmod uo-t file OR chmod 0xxx file

Yes you can chain the number up by summing them.

## System default permissions
When a file is created, the default permissions are set on that file. The `UserMask` reduces the maximum possible permissions to give us the default ones:
- Max perms on file: 666
- Max perms on dir: 777

To check the `UserMask` do `umask`. You should probably see `0002`. Ignore the first number. Now:
- Max perms on file: 666
- UserMask: 002
- Max perms for user: 666 - 002 = 664 (`rw-rw-r--`, ahaaaaaaa, makes sense no?)

# ACL
Access Control List (HEY WAIT A MINUTE I'VE SEEN YOU [[NACL|BEFORE]]). 

The ACL provides an additional, more flexible permission mechanism for file systems.

## `setfacl` and `getfacl`
Set is used to setup ACL, get is used to show ACL

# File System, Names, Inodes, Symbolic Links'
When you create a file, its name is added to the names table on the hard drive, and its metadata goes into the i-nodes table. The i-node tells you exactly where this file is stored on the hard drive (which block is it in).

Here's how it works:
6KB file, 4KB block, needs to be broken in half and stored in multiple blocks.. File created -> Name stored -> Name references i-node -> i-node points to 1st block of the file -> The block right after it points to the 2nd block wherever it is -> Encounters a 0 = end.

`ls -li` shows the inode number of a file

%% Please look this shit up bro I can't type as fast as he explains  %%

Hanging link

Hard link must remain within its own file system
Symbolic link doesn't have to

Hard link cannot link directories
Symbolic link can

# Searching, archiving, and compressing
## Finding commands and Documentations
Do `whereis` to seach for the executable files, source files, and man pages
Do `man` to pull up the manual
## `locate`
If you've ever search for a file, you'll realize shit takes a long time. But if you want to speed this up, you can do an "index search". An index search looks at a database of names and returns exactly the file matching that name. 

Of course because it only searches for names, it returns EVERYTHING MATCHING THAT NAME. But we can tweak it somewhat.

Do `locate linux`. Boom, a ton of entries were found. Some have `linux` in the names, some have `linux` in the paths. What if we just want name search?

Do `1ocate -b linux` for base search. Now you should see much less.
Do `locate -c linux` to count how many hits matching the specified name and filters.
## `find`
If `locate` doesn't work for you, do `find`. Find is used to search for files in a directory hierarchy rather than index. This is slow as shit. BUT it is way more accurate. You can specify the folder to start searching, apply filters, etc.

Example:
- Find single file by name: `find /-name "Foo.txt"`
- Find single file by approximate name (using wildcards): `find /-name "?oo.*"`
- And way more, just look up `man` bro
## Compression
Compression makes files smaller
2 types of compression:
- Lossless: No info is removed
- Lossy: Some information is removed (mostly used for media files).
### `gzip` and `bzip2`
Gzip:
- Fast, low compression
Bzip:
- Slow, CPU intensive, maximum compression

`gzip file`
`gunzip file`

`bzip2 file`
`bunzip2 file`
## Archiving
Archiving save a copy of the file into the archive, like a backup.
### `tar` and `zip/unzip`
`tar` has a ton of options so I will go ahead and ignore all of them and tell you to READ THE FUCKING MANUAL.

-c create
-v verbose
-f rename

-t
-v
-f

-x extract
`tar [OPTIONS] archiveName filesToBeAdded[]...`

`zip` literally works just like 7zip. syntax: `zip zipName filesToBeZipped[]...`