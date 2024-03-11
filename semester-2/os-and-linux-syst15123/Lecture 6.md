# Flat file manipulation
`paste`
`join`
`sort`

`sort -t: -k4` sort by the 4th column (delimited using space), alphanumerically 

`sort -t: -k4 -n` sort by the 4th column, numerically 

`sort -t: -k4 -n -r` sort by the 4th column, numerically, and in reverse order

`cut`
Cuts a character or a specific field

Thought problem: What if the field has different lengths each line? We can't cut by length! We would either have to normalize the whole file OR... we find a different way.

The different way being cut using delimiters (assuming the file is delimited)

`cut -d: -f1,3` cuts at delimiters, fields 1 and 3. 
`cut -d: -f1,3-5` cuts at delimiters, fields 1 and 3 to 5 inclusive.

What if we want to send the file to a printer? We want it to look better! Then we use `pr`

`pr -n -h "Hello"`

`diff` can be used to compare files line by line
`cmp` can be used to compare files BYTE BY BYTE.
`comm` compares 2 **sorted files** (yes, MUST be sorted). It creates 3 columns:
- unique to file1
- unique to file2
- shared by both files
compared line by line ofc

 
# User Accounts
The /etc directory contains files which contain account data of users and groups on the system

The /etc/passwd file defines some account information for user accounts. You're probably thinking, oh that's where passwords are- 

NUH UH *INCORRECT it BUZZER SOUND*. Passwords are elsewhere. This USED to be the passwd folder but after they realized it's unsafe, they moved elsewhere (yes, shadow) and repurposed this directory.

To get user information in the passwd directory, do `getent` with the NAME of the database e.g getent passwd root to get root's info.

## System Accounts
System accounts are acocunts made by the system to run certain services. Sometimes services lliterally cannot access the user account necessary to run the service, so it's easier to just make an account for those services.

Users log in using regular accounts (UID > 1000)
System administrator, root account (UID = 0)
System accounts are used to run services on the system (UID 1-499)

In shadow, system accounts have a star on its 2nd column. 

## Group Accounts

## Get user information
`id` gets the current user information and their relations to the groups.
`uid` is user id
`gid` is group id.
`groups` show what groups this account is associated with.

groupadd creates a group. -g allows adding a custom id. -r adds a group but gives it an id 1 below the user range
## Modifying groups
groupmod can be used to change the name or ID of an existing group. If you change the name, Linux will automatically update items owned by that group to the new name (this is because they are linked by ID, not by name).

What will happen if we change the group's ID? Try it! Now when you check the file again, you'll realize that this file is no longer of any group, a.k.a. it is now **orphaned**.

You can confirm if a file is orphaned using find . -nogroup

deleting a group is done with groupdel. NOTE: deleting a group does not delete files it owns (yes, this will orphan them--jesus can't we come up with a better term???)

## Default Serrings for creating Users
Wehn we create users, we should verify the default values using the useradd command.

Do useradd -D to show all the defaults values for the useradd command.
Or do sudo nano /etc/default/useradd

The etc/skel file pre populates a new user home directory with a bunch of pre-specified files.

/etc/login.dfns

useradd -m to force creation of user folder

look up `usermod` on man
