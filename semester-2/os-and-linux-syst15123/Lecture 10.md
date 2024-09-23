# UID, PID, and PPID
# Priorities
In a computer, the CPU will attempt to process processes based on their priorities. Assuming all the tasks have the same priority, the CPU will spend 1 quantum of time to process 1 task, then it moves to the next task, and the next, etc. then loops back to the first task, until the task completes.

When a higher priority task (lower priority value = higher priority ranking) appears, the CPI will attempt to finish that task first, then it'll figure out the rest.

The lowest priority number you should, but not recommended to get to, is 20. This is the OS priority. Any lower than this will hang the OS and crash it. 

## Changing priority
You can change your priority up or down, but a non root user can only lower their priority. Yes, if you edit your priority to lower, you literally cannot undo it. 
### Nice values
You can also add and minus -20 to +19 priority values, which is equivalent to 60 to 99. This changeable value it called the Nice number (I have no fucking clue why).

To change prio with nice, do `renice +19 [PID]`. Reusing the command does NOT add on top of previous Nice value, but rather, overwrites it. 

Entering a value higher than 19 or lower than 20 will cause the system to ignore your input and use the largest/smallest value possible which is +19/-20.
# Jobs
Signals

# Kill
`kill` and `killall` are used to kill a single/multiple processes. Killing depends on the kill signal. You should remember a few of them for class. But irl, `-9` is the only kill signal you really need to know. It will obliterate whatever running process mentioned.
# `/proc` directory
Pseudo-directory. Yes, it DOES NOT exist on the hard drive. This is your "RAM folder". Volatile and dangerous. If you move its contents to your hard drive your PC will be slow as shit bc it runs at the speed of a hard drive.

This directory literally only exists to keep track of resources requested by your processes. If the process is killed, that resource is gone.

# Process Hierachy
The first process to run will get the PID of 1. Every process afterwards increments the previous PID number by 1

# `top`
Similar to task manager, can show you CPU load 5, 10, and 15 mins ago. The load average of the CPU is based on your core count.