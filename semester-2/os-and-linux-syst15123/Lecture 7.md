`exec` replaces the current working shell with a new shell. Running a new bash shell with this on top of the starting one will overwrite it and gives it an entirely new bash shell.

`ps` lists all processes currently running under the working shell tree.

# Shells
This is not even close to all the shells that exist out there. Remember that shells can just be created by virtually anyone. There's probably millions out there. Here are only the most popular ones
## C Shell (csh)
Made by Bill Joy at UC Berkeley. 
Has aliases and command history. 
Useful for C development
## Bourne Shell (sh)
The original UNIX shell. Written by Steven Bourne at AT&T Bell Labs. 
Faster but lacks any interactive features like history. 
Default for Solaris OS.
## Korn Shell (ksh)
Superset of Bourne shell. Written by David Korn at Bell Labs (why the fuck are there so many Bell Labs devs).
Includes everything in Bourne shell, has interactive features.
## Bourne-Again shell (bash)
Includes features from Korn and Bourne shell. Compatible with Bourne shell. 
Full path name is /bin/bash
## Common features of Shells
Command line history
Inline editing
Scripting
Aliases
Variables.

# Variables
A variable allows the user or the shell to store data in memory.
Variables are given names and stored temporarily in memory.
There are two types of variables used in the Bash shell (local and environment).

Local variables: lowercase
Environment variables: uppercase

Assigning a value to a variable must be done without space and without dollar sign
But calling a variable is done with a dollar sign

To unset a variable, do... `unset`. I mean... it's Linux, it's as straightforward as can be.
## Environment Variables
Also known as global variables. Denoted in all caps.

Any changes to environment variables (env) will be reset on new session. They can only be permanently stored in the config files.

# Alias
Aliases are shortnames for longer commands. Do `alias='command_you_wish_to_run` to generate a shortcut for the command.

Do `unalias [command]` to remove the alias.
# Shell Environment Variable
Used to customize the environment in which the shell runs
Used to pass information between commands and subprocesses as well as control some shell behaviors.
When a program or command is executed, receives an array of key-value pairs of commands
## $PS1
Controls the appearance of the command line prompt (usually `name@address:~$ `)
## $PATH
This is a so-called "search path". Think of functions. What is a function? 

A function is a set of instructions, right? That means that these instructions is stored somewhere on the computer. Probably in an executable file somewhere. This "somewhere" is what we call the "path", or technically, "one of the paths".

Do `echo $PATH`. You'll see an array of paths, separated with `:`. These are paths to directories where Linux would go into to search for a command. Example: `cal` is stored in `usr/bin/cal`, so if I run `cal`, it would tell Linux to go into the `$PATH` environment variable, pick the first path, look for the directory in that path, and if it doesn't find it, moves onto the next path. 

`echo` however will still work even when you remove `$PATH`. This is because `echo` is a built in command. See figure below:
![[Pasted image 20240314155431.png]]

## Read-only Environment Variables
`$0`: Name of program
`$1-9`: Value of command line args, in order
`$*`: Values of all command line args
`$#`: Number of args
`$?`: Most recent exit code of most recent command
	- 0 is ok
	- 1 is minor error
	- 2 is major error
	- 127 is command not found/not properly installed

# `declare`
Declares a variable as an environment variable. Syntax:
`declare -x VARNAME=somethingHere`
To remove this variable
`declare +x VARNAME`

# `export`
Turns a local variable into an environment variable
# `set`/`unset`
`set` will set whatever argument you enter into a read-only environment variable (`$1-9`). 
`set -k` will turn a local variable into an environment variable. BUT PLEASE DONT USE THIS.
# `env`
Can be used to alter env variables before executing a command. Only works within the scope of that command, does not actually store the variable.
# Shell scripting
A shell script is a text file that contains executable commands and other instructions. When a script runs, commands and instructions in it are executed. 

Very useful in automating tedious parts of your work.

Scripts are NOT compiled, but interpreted. Your bash file will be executed line by line.

## Creating a script
Make a new `.sh` file. The first line is called a **shebang**. The syntax is `#!/bin/bash`. This line means "execute this script using the **bash shell**, stored in this directory."

Then write the rest of your script.
```
#!/bin/bash

echo "my first script"
date
```
## Running a script
Depending on your umask, you might not be able to execute the script on the fly. You might need to `chmod +x [filename]` to make that executable. Then you can run `./[filename]`.

But you can also directly call the bash shell and pass the script as an argument, like so `/bin/bash [filename]`.

Or you can run `. [filename]` which is equivalent to the above.

Or you can concatenate this file's path to the `$PATH` env variable and it should allow you to call the filename directly.
> [!important] It is NOT advisable to do this as it is a huge security risk.

> [!note] It is, however, more advisable to add your scripts into the bin folder in your home directory as this is already in `$PATH`
# Bash quirks
## Everything is a string
Bash has some funny quirks. For example, it treats everything as a string. Look at the following figure
![[Pasted image 20240314164443.png]]

It even considers the concatenation syntax as a string. So we should do this instead.
![[Pasted image 20240314164606.png]]
This clones a and b and turns them into integers. Then sums them and converts that sum into an integer. Then passes it into c. 

Or you know, do this:
![[Pasted image 20240314164713.png]]

You can actually use a function specifically made for computations, called `expr`. Add space in between your terms to prevent it from being interpreted as a string
![[Pasted image 20240314164925.png]]

But it will not work with multiplication, because the `*` will be interpreted as a wildcard. Use an escape sequence to turn it into a multiplication sign.
![[Pasted image 20240314165041.png]]

Yes this applies also to comparison, no I won't provide examples.

## `declare`
You can avoid all the headaches above by using `declare -i [args]` instead of `set [args]`. BUT IT'S NOT ADVISABLE.

User inputs could be faulty and any mistakes will crash your script. Just do them manually to save yourself from the trouble.

## Floating-Point Arithmetic
Please be warned that this does not work on bash by default.

Use `bc` to compute floats (bc stands for bash calculator). `bc -q` to enter interactive mode. Use `scale=[float_accuracy]` to print decimal points.

# printf
Works the same way as every other printf lol.
