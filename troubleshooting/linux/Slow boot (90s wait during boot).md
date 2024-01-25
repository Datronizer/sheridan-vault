# Symptoms
So you fucked up huh? 

Chances are you're here because
- Your device takes longer to boot than usual (90s wait during boot)
- You're getting the infamous `No arrays found in config file or automatically`
- You're getting complaints during `sudo apt update/upgrade`
# Causes
This error probably occurred during one of the following:
- Failed partition
- Installation of a new drive
- Accidentally removed a drive during installation/partition
- Newly installed RAID
# Solution
Well, here's a fix: [AskUbuntu](https://askubuntu.com/questions/711016/slow-boot-a-start-job-is-running-for-dev-disk-by)
%% tl;dr the fix  %%
# Explanation
## tl;dr
This bug is actually occurring due to a mismatch between actual drive UUID and stored UUID. 
## Full explanation
Typically Linux stores the drive UUID in `/etc/mdadm/mdadm.conf`. It would use this stored UUID to initialize the drive during boot. Of course during this causes some issues.

Mainly, it doesn't account for the fact that the user is bad at Linux (me), and would fuck up a partition which would change the UUID of the drive but not the UUID in  `mdadm.conf`.

This would cause a mismatch and causes the system to search frantically for the missing drive and even wait 90s for it to properly boot in case it wasn't detected the first time. 

Of course the solution is simple: Check all the drive values to see what's mismatched, fix it, and reboot. Now you're all good.
