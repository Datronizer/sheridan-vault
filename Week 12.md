# Systemd
systemd is a service and system manager for Linux, designed to be backwards compatible with the outdated SysV. `systemctl` is the command that is used to access/control systemd

To check version of your systemd, do `systemd --version` or `systemctl --version`.

Systemd can be used to start, stop, restart services, and also allows auto-start services at boot time. You can check service status and more. 

Example:
`systemctl status ssh`

Starting a service:
`systemctl start [servicename]`

Check if service is enabled:
`systemctl is-enabled [servicename]`

Prevent service from starting up at boot time
`systemctl disable [servicename]`

Stop a service
`systemctl stop [servicename]`

# Run levels and System Targets
In SysVinit systems, you have a defined but configurable set of runlevels numbered from 0 to 6.
But in systemd, we now call them targets (these directly correspond to the SysVinit runlevels by the way).

We actually talked about this before:
Run levels & System targets
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

Of course a target isn't just the target alone, when it boots, it boots with ALL its dependencies, which by the way is a fuckton.

To switch to a target, let's say `multi-user.target` using systemd, do `systemctl isolate multi-user.target`