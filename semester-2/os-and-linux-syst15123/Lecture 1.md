# Linux
Linux is everywhere. Man, you wouldn't believe it.
- 71.93% of global operating system market share is taken by Android (also Linux)
- 54.2% of supercomputers run on Linux
- 90% of cloud workloads run on Linux
- Even fucking Steam runs on Linux
## History
Linux is a combination of software called GNU/Linux.
- In 1983, Richard Stallman announced the GNU Project
- GNU is the free software that provides open-source equivalents of many common UNIX commands.
- The goal of the GNU Project is to give computer users freedom and control in their use of their computers and computing devices by developing and publishing software for free.

After the GNU project, the story of Linux officially began with UNIX--an OS developed at AT&T Bell Labs in the 1970s. Linux development started in 1991 as a hobby project by Linus Torvalds.
> We're going to segue here a bit and say that Linux is NOT UNIX. UNIX was a proprietary software, but Linux was a built-from-scratch OS that looks and functions like UNIX. Also UNIX is dead lol.

Linus basically straight up made a UNIX ripoff except it's so much better. Of course back then, copyright wasn't a huge issue so he got away with it, and UNIX is pissed so they will never certify my boy.
## Linux Distributions (Distros)
A distribution is the collection of software that are bundled together:
- Linux Kernel
- GNU tools
- Suite of Applications
- Package Manager (app store lol)
- Installer

Every distro differs from each other simply by the elements within their collections. Ubuntu might have a bunch of bloated shit, Arch might have a bunch of acoustic shit, and Red Hat might have different hacker man shit. It's the freedom.

You can keep track of all the distros and their histories on [distrowatch.com](https://distrowatch.com)
## Why Ubuntu?
We're choosing Ubuntu because all the features provided are useful for our course (even though I fucking hate it). 
# Kernel 
A kernel is the central controller of everything that happens on the computer, it is a core of the Linux operating system. Imagine your computer is a house, the Kernel would be the housekeeper. Of course you own the house, but you only live in it, the Kernel takes care of everything.
# GUI and CLI
There are 2 basic types of interfaces that allow you to interact with the OS:
- GUI: Graphical User Interface
	- Has visual parts that you can see, resize, use, and interact
	- Easier to use for the user endpoint.
- CLI: Command Line Interface
	- Simple text based interface
	- Hard for users but good for developers
	- Direct access to kernel to do whatever you want
# Operating System (OS)
An operating system communicates user inputs to hardware.
## Microsoft Windows
Proprietary OS, does not run on either Linux or UNIX-derived OSes
- Offers both desktop and server versions
- Slow release cycle (3-5 years)
- Long maintanence cycle
- Emphasis on backward compatibility
- Runs a GUI + CLI
## Apple MacOS
- Runs on Apple hardware
- Server version adds stuff to the desktop version
- UNIX certified
- New major releases every 18-24 months
## Linux
- Runs on anything
- Open source
- Distros depending on use case
- Lifecycle varies
	- Most distros are run by volunteers so you can't demand anything from them.
	- Some distros have Long-term Support (LTS), 5+ years or 13years for SUSE LTS, thanks for company financing and support.
- Stability
	- Depends on distros and releases. Can choose between stable, LTS, or unstable (beta).
- Supports
	- Free distros BUT support depends.

# Major Linux Distros
## Red Hat
Enterprise distro, used for servers, run by the Red Hat Corporation. As you can probably guess, they have fuck-you money so they sponsor the Fedora Project (free and open-source personal desktop OS with latest software).

Famously known for Red Hat Enterprise Linux (RHEL) which is a commercial and stable distribution with long release cycles.

Also famously known for the "CentOS incident".

As you can also tell, being a corporation, these fuckers are not here for your good. They only want money. And you, my friend, are looking economical right now.

## SUSE
Derived from Slackware, contains proprietary code and is **sold** as a server product.

You're probably saying? Wtf? How? Isn't Linux open source?

Yes, but if you add something proprietary, it stops being open source. Again, fucking corpos.

## Debian
Community run distro that promotes use of open source software. (Hell yeah)

Ubuntu is the most popular derived distribution
- Desktop and Server Ubuntu
- Offers an LTS version
- RUN BY A FUCKING CORPORATION AAAAAAAAAAAA
## Android
Mobile platform :D

Google took this, took out the desktop portion of it, and it becomes a mobile OS. Which means it's technically not a Linux because it cannot be run on desktop--only Linux-derived.
## Others
### Raspbian
- Linux distro designed to run on Raspberry Pi hardware
### Linux From Scratch (LFS)
- Linux From Scratch (LFS) designed to teach you how to run your own distro.
# Major applications
Software generally fall into 1 of 3 categories:
- Server Apps: serve information to other computers, called clients
- Desktop Apps: web browsers, text editors, music players, etc.
- Tools: Software that makes it easier to manage computer systems.

Guess what? Linux has all those FOR FREE and THEY WORK AS WELL AS ENTERPRISE SHIT. I would know BECAUSE I RELY ON THEM because im poor teehee.

# Shell
The "shell" is the direct connection to the Linux Kernel. Everyone starts with [[Bourne Again SHell (bash)|bash]] before moving on the more specific ones for their tasks.

# Package Management
In Windows you'd double click a `.exe` or `.msi` file and boom, app installed. On MacOS is `.dmg`. On Linux? Good fucking luck lmao.

Every distro uses their own package management system (think of them like the Linux App Store). The 2 most popular managers are:
- Debian Package Management:
	- Used on Debian-based systems.
	- Packages are distributed as files ending in the `.deb` extension
	- Tools: `dpkg`, `apt-get`, `aptitude`, `Synaptic`, `Software Center`, and etc.
- Red Hat Package Manager (RPM):
	- Used on Red Hat systems
	- Ends in `.rpm`

Why do we have these instead of direct downloads? Well, a lot of times, a software **depends** on a lot of other software (aka **dependencies**). On Windows, this is usually pre-packaged. But on Linux? Sometimes it just doesn't do that.

That's why we have the front-end package manager! It would route all the dependencies for you to download and boom, you get all the files without the headache. BUT, this also means you lose out on the freedom of choosing what you want. 

# Open Source Licensing
When you purchase a license, generally you are not allowed to do things that violate their agreements. Kinda fucked eh?

End User License Agreement (EULA)
- Legal document that must be accepted before installing software
- You don't read these, do you?

## Free Software Foundation (FSF)
- Founded in 1985 with the goal of promoting free software, political, but not realistic
- Enforces copyleft: users who modify the free software are requried to share it
## Open Source Initiative (OSI)
- List of Open Source Licenses:

## FOSS/FLOSS
- Free and Open Source Software: Free to use but not free from restictions
- Free/Libre/Open Source Software: Free to use and free from any and all restrictions (within the legal limit of course)
## Creative Commons
- Licenses without copyleft are called permissive
	- Attribution: Must acknowledge the author
	- ShareAlike: Copyleft
	- No-Derivs: You may not change the content
	- NonCommercial: No commercial use
	- Combinations are allowed of course, i.e.: Attribution-No-Derivs-NonCommercial