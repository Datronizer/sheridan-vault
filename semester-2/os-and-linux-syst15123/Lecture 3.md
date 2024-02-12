# Directory Structure
Think of the Linux file system as a hierarchical tree structure, but the tree is upside down.

At the top is the root directory, represented by the `/` (slash) character. (see? upside down tree)

## Home Directory
The home directory is a dedicated directory for a particular user where that user can store their personal data. 

In Linux, when you install the operating system, you are always asked to create an account (for security of course). This account will be provisioned a home directory. To get to your home directory, do `cd`.

What? That's literally it! It's just `cd`.  

Of course if you want to check for yourself, do `pwd` to Print Working Directory (PWD). Of course, as the name suggests, it **prints working directory** (the folder you're sitting in right now).
## Paths
Hey wait a minute this seems [[path|familiar]].
### Formal explanation
A path is a list of directories separated by the `/` character.
There are two types of paths: *absolute* and *relative*.

For example: `/home/oa-adminhome1/37/ivanovn` is an absolute path to the home directory of the `ivanovn` user.
### Laypeople explanation
Here's one way to understand paths. Imagine that every path of 1 parent directory are hotel rooms and they are all connected by a hallway outside the room. If I want to go from the room (directory) `home` to the room `var`, I need to first leave the room (go up a directory), then go down the hallway to `var`.
### Notable paths
- `~` represents the path relative to the `home` directory (basically `~` == `home`)
- `/` represents the root
- `./` represents the current working directory
- `../` represents the folder 1 level above the working directory
### Path traversal
You can traverse to a different directory using the absolute path (basically like giving someone directions to your hotel room, what floor, what hallway, what room etc.)
You can of course traverse to a different directory using the relative path. However! There are different ways, for example:
- `cd` sends you to `home`
- `cd .` sends you... back to your room. `.` (dot) literally means current folder. Changing current directory to current directory means you didn't go anywhere! 
- `cd ..` sends you up 1 level, meaning you just exited your room, walked through the hallway, to the lobby.

# `ls -l` Long list (details)
Run `ls -l` and look at the output, you'll probably see a ton of garbage. Each of these means something, so, I'll attempt to explain everything here. Starting with how to read what type the file is.
## How to read file type 
Pay attention to the  `dwrx--x-r-` blah blah thing. Okay, now only look at the 1st character. This character tells you what type the file is.
# Managing Files and Directories
## Globbing Characters (Wild cards)
Allows you to specify patterns by replacing a part/the whole name with wildcard characters. For the full list of wildcards, do `man 7 glob`

### Asterisk (`*`)
Represents any number of characters (zero or more). Examples:
- `*` represents any name
- `*d` name that **ends** with d
- `d*` name that **starts** with d
- `*d*` name contains a d somewhere in between
- `c*d` name that starts with c and ends with 
### Question mark (`?`)
Represents some character, can be used to specify specific file length equal to number of `?`. Examples:
- `????` represents any name 4 characters long
- `f.???` represents a name that starts with `f.` and ends with 3 characters
### Square brackets (`[]`)
Used to match a single character. This is called a set.
- `a[bc]d` starts with a, ends with d, middle character is either b or c
- `a[0-9]d` starts with a, ends with d, middle character includes all nums from 0 to 9 inclusive
- `1[a-z]2` starts with 1, ends with 2, middle character includes all chars from a to z inclusive
- `1[a-z,A-Z]2` middle character includes all chars from a-z inclusive, union with A-Z inclusive

Note: the range ONLY travels in 1 direction, the ordering follows the ASCII table. For example: reversing the search `[9-0]`, the query will then return everything from 9 to the end of the ASCII table, loops over to the beginning, returns everything from there to 0, and ignores everything between 0-9. 

We can use this to our advantage to exclude everything in the range. Or, we could just exclude them using a specific character
- `[bd]*` name starts with b or d
- `[!bd]*` names does not start with b nor d
- `[^bd]*` names does not start with b nor d (same thing, just old notation)

Of course chaining sets means find a name that matches:
- First char with first set
- Second char with second set
- etc.
### Curly braces (`{}`)
Finds all elements whose name matches that within the curly braces.
- `{dpkg,kern}.log` name starts with `dpkg` or `kern` and ends with `.log`

# Creating text files
You can use `touch [filename]` to create a new empty file. Of course doing `touch [fileA] [fileB] [fileC]` will create 3 empty files.

You can use `cat > [filename]` will wait for your input and do [[output redirection]] to that new file. `Ctrl+D` ends the input and boom, new file made.

# Create directories
Use `mkdir [dirName]` to create an empty directory. Chain multiple `[dirName]` to create multiple directories. 

Use `mkdir a` to create a directory `a` in an already directory existing `a`. Yes, `a` MUST EXIST.

If it doesn't exist you can:
- (manually) `mkdir a a/b` to create `a` first then create `b` in `b` now that `a` exists.
- (ideal) `mkdir -p a/b` to force Linux to create a directory if it doesn't exist and recursively go down levels until it hits the end of the requested path. `-p` means path, which means "attempt to mkdir until you reach that path"

Of course you can do all this with absolute paths, don't worry.
# Remove directories
`rmdir` removes EMPTY directories only. Else throw error.

What if I want to yeet an entire branch? I can't type out the path because it just removes the last directory in the branch. So, like earlier, I have manually to remove one directory at a time, innermost to outermost.

In that case how do I yeet the whole branch in one go? Then we throw a `-p` flag in there to tell it to obliterate the whole path. Here `-p` means "attempt to obliterate from the innermost dir until you hit the outermost dir"

Now, what if I have `a` containing `b` and `c`. If I do `rmdir -p a/b`, I will get an error that `a` isn't empty, but `b` still got obliterated.

This is why you should always triple check with `tree` to make sure what you want to remove is gone and what you want to save isn't blasted by accident.
# Remove file
`rm` removes FILES only.
- Add the `-r` to recursively remove everything matching the argument name. Example: `rm -r a` deletes everything with the name `a`
- Add the `-f` to forcefully remove things even if the system screams at you- 

> [!important] NEVER EVER do `rm -rf *` in ANY FOLDER OTHER THAN THE ONE YOU WANT TO WIPE. THIS WILL LITERALLY KILL YOUR COMPUTER.

Okay we continue:
- Add the `-i` flag to interactively remove things. It basically asks you at every step. It will yap. Yap example:
	- You wanna go into this folder? Okay
	- You wanna go into this inner folder? Okay
	- You wanna go into this inner inner folder? Okay
	- You wanna delete this file? Okay
	- You wanna move up a folder? Okay
	- You wanna delete the folder you just moved out of? Okay
	- You wanna delete this file in the current folder? Okay
	- You wanna delete this other file in the current folder? Okay
	- You wanna delete this other other file in the current folder? Okay
	- etc.
# Copying and Moving and Renaming files/directories
## Copying
`cp [option] SOURCE(S) DIRECTORY` to copy a number of files to 1 destination. 

The last argument is the destination, always. If you want to copy it multiple times, you have to call `cp` multiple times.
- `cp` also requires you to do `-r` to recursively copy directories.
## Moving
`mv [option] SOURCE(S) DIRECTORY`  to move a number of files/directories to 1 destination. 

**BE WARNED:** If you move files from A to B and both folders contain files with the same name, the files from A will OVERWRITE the ones from B.
- do `-n` for "no clobber", which means don't move the files that can overwrite, move everything else instead.

Moving directories will work the same way as moving files.
## Renaming
Renaming is with moving but the name changes at the end of the process. 
`mv a b` renames the file/directory from `a` to `b`
`mv a/hello.txt a/b/bye.txt` renames the file to `bye.txt` and moves it into `a/b`.

# Text editors
## nano 
Pretty primitive editor. Does simple stuff. Basically notepad but shit.

Do `nano` to open notepad. Saving file will create new file.
Do `nano [filename]` to open an existing file.

Top left tells you ur in nano
Middle tells you the name of the file, `New Buffer` means your file is new and thus is untitled.
Right tells you if you edited the file and forgot to save (it will say `Modified`)

I will not write down all the shortcuts here because they're all on the nano terminal by default.

`Ctrl+K` cuts, `Ctrl+U` pastes. Spamming `^K` multiple times in a block cuts that block by the number of lines you spammed. `^U` pastes all the lines you cut from that block.
## vim
Vim is a default editor for Linux. Way more popular and powerful but FUCKING HELL WHY IS IT SO HARD TO USE.

PLEASE JUST GO [HERE](https://openvim.com/) I CANT HELP YOU