# Advanced Bash scripting
## read command
`read` allows the user to input data into a running script. Basically it prompts the user to input.
## command line args
Suppose you are writing your own command, and you want the user to enter args. To read their args, follow this table:

| Readonly Bash ENV | Definition         |
| ----------------- | ------------------ |
| $0                | Name of program    |
| $1-$9             | Values of args     |
| $*                | Values of all args |
| $#                | Number of args     |
## shift command
`shift` "promotes" your command line args. What does this mean? 
Suppose you have 3 args:
	a = 1; b = 2; c = 1984
If I use `shift`, I would then get:
	a = 2; b = 1984; c = 

It "shifts" every args up and pops the first one.

## Exit status
Sometimes you just can't trust a command output as an indication of a fail or not. Hence, you rely on exit statuses instead!

Do `$?` to check the most recent exit status of the most recent command. Here are the most common errors:
- 0: Success
- 127: Command not found
- 1-126: Some sort of error (refer to individual `man` pages for more details)
## Conditionals
| Operators          | Meaning          |
| ------------------ | ---------------- |
| string             | True if not null |
| string1 = string2  | True if same     |
| string1 != string2 | True if diff     |
|                    |                  |
|                    |                  |
## Logical operators
AND: && or -a
OR: || or -o
NOT: !
## If statements
Syntax:
```
	if test-condition
	then
		commands
	elif test-condition
		commands
	else
		commands
	fi    
#   ^^
#    yes, this is "if" spelled backwards
```

For test-conditions, please do either `test $word1 = $word2` or `[ "$word1" = "$word2" ]`, and no, the spaces are NOT optional.

Using `-f` on an if statement (`if test -f $path`) will return true if `$path` is a file. Similarly, with `d` for directories.

## case statement
RAAAAAHHHH SWITCH CASE STATEMENTS

```
case "$answer" in
	[aA])
		date
		;;
	[bB])
		who
		;;
	[cC])
		pwd
		;;
	*)
		echo "Wrong input: $answer"
		;;
esac
```
## for loop
### Fixed counter for loop
Based on a counter 
```
for ((i=100;i<=105;i+=1))
do
	echo $i
	sleep 1
done
```
### For-each loop
Based on a collection
```
fruits = "apple pear banana kiwi"

for fruit in $fruits
do
	echo $fruit
done
```
## while loop
```
while [ $number <= 5]
do
	echo "$i"
	$i+=1
done
```
### until loop
```
until [ $number -gt 5]
do
	echo $i
	let i+=1
done
```
### break and continue
Does the same thing as other languages, syntaxes are the same also.
## Array processing
No array size limit, array elements will automatically be created and won't crash if creating one element beyond the array size.

Arrays are written as such in Linux: `fruit=(apple pear orange banana kiwi mango)`
To access them, do so:
- `echo ${fruit[2]}     # print third element of array`
- `echo ${#fruit}       # print size of the first element (in bytes)`
- `echo ${#fruit[1]}    # print size of the second element (in bytes)`
- `echo ${#fruit[*]}    # print size of the whole array (No of elements)`
- `echo ${fruit[*]}     # print the whole array`
## Functions
A set of commands, blah blah, you've heard this [[Functions (Computer Science)|already]]. 
### Syntax
```
#!/bin/bash
function f1() {
	echo "this is function 1"
}

f2() {
	echo "this is function 2"
}

# Now we call these functions casually
f1
f1
f2
f2


> this is function 1
> this is function 1
> this is function 2
> this is function 2
```
### Variable scope
Global variables are variables that can be accessed from anywhere. In Bash, every variable is global by default. To specifically define a local variable, say it specifically, for example: `local variable1='C'`

Piggybacking off this, the easiest way to return a value is to simply map it to a global variable.
### Passing args
Since we're in Bash, we literally don't need to specify arguments for function since all variables are global. Then we can just extract the input args and do `someFuction $varA $varB` and boom. 

# `man`
## man page locations
All the standard installed commands are in `/usr/share/man/man[1-8]`

But if you want to write your own, write it in `/usr/local/man`. Make a new folder, say `man1`, and add a text file there.

You'll probably realize very quickly that your man page is not formatted! That can be done using the Troff formatting macros.

A demo script will be included in this folder.
# Networking
## Definitions
- Device: Network adapter in the system
- Link: Used by command line tool, refers to the connection of device to network
- Address: UP address assigned to a device
- Braodcast: Refers to broadcast address of a network
- Route: Path that the IP packet takes to go from source to destination
- Packet: Small segments of larger message, often split up when sent.
These are already covered in [[Introduction to Data Communications and Networking - TELE13167]]

Look up google.com's ip address. Now try going through that address. You'll quickly realize that your browser blocked that access for your safety, that is because the security certificate SSL is bound to DNS names rather than IP addresses. Anyways, if you ignore the protection you'll still get to google just fine.

## ifconfig
Similar to Window's ipconfig. Being phased out by `ip`
What does everything mean?

flags: shows the properties of your network card:
- UP: runs on boot
- RUNNING: currently active
- BOARDCAST/MULTICAST: can broadcast/multicast

default via is the default gateway (0.0.0.0/0), it's stored as the address the router shows to the local network. In reality everything that goes through there getss routed through to the Internet with public addresses.

networkd allows manual editing of network interfaces. You can also use NetworkManager.
To save networking edits, you need to edit `/etc/netplan/`

## ping
## host
Reverse name resolution. Basically looks up the IP of the DNS name.
## dig
Suppose I'm pinging google and I received an IP address. What if I want to know the DNS server that provided me with that info? Then I'd use `dig`. For `dig`, there is an ANSWER and QUESTION part. ANSWER means endpoint is reached, else you won't see it.
## ss
## ssh


When you attempt to ssh into a device, you can see a fingerprint, something like `SHA256:kasdh_@J123kjsad` whatever right? This fingerprint is uniquely defined and can almost never be the same between any 2 devices. Once you confirm this fingerprint is the correct one, you can then hit `yes`. This fingerprint will now be stored in `/.ssh/known_hosts`.
## scp
Secure copy. Lol you already know this you bozos.
## sftp
Same concept as scp. Secure File Transfer Protocol. Do sftp source. Now you should be in the sftp shell. Do get filename to snatch the file. Do put to upload and edit the file.
## rsync
Synchronization. Suppose you have 2 computers and you do work on both. Uh oh, you've done so much work on your laptop and you want to sync it with the desktop. What do you do?

rsync duh!

Do `rsync -av a b` 

## Postnote
For the rest of this section, please refer to the attached powerpoint. Notes will not be taken as they are irrelevant to the exam contents.

