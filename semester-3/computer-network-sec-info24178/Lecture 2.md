# Attacks Using Malware
## Malware
Software that enters a computer system without the user's knowledge or consent and then performs an unwanted and harmful action. Malware continuously evolves to avoid detection by improved security measures.

One attempt at classifying malware is to examine the primary action that the malware performs.
### Imprison
Some types of malware attempt to take away the freedom of the user to do what they want, e.g Ransomware and Cryptomalware
#### Ransomware
Prevents the user's endpoint device from properly and fully functioning until a fee is paid. Some pretend to be from a law enforcement agency. Others pretend to come from a software vendor and display a fictitious warning that a license has expired
#### Cryptomalware
Imprisons users by encrypting all files on the device so that none of them can be opened. The cost to unlock increases every few hours or days, usually extorted through cryptocurrency to prevent tracing. New variants encrypt all files on the network or attached device connected to that computer.
### Launch
Infects a computer to launch attacks on other computes. Includes virus, worm, and bot.
#### Virus
There are 2 types: file-based virus and fileless virus.
##### File-based virus
Malicious code attached to a file that reproduces itself on the same computer without any human intervention
- Armored file-based virus: Goes to great lengths to avoid detection, using techniques like *split infection* (splits randomly and attack different files) and *mutation* (changes file signature to avoid detection)
- Virus first unloads a payload to perform a malicious action, then the virus replicates itself by inserting its code into another file on the same computer.

Appender infection: Appends a malicious segment of code at the end of a program code, adds a "jump" segment at the top of the program code to skip straight to the malicious segment. 

You can actually find malware for free on [malware bazaar](https://bazaar.abuse.ch/browse).
##### Fileless Virus
Does not attach itself to a file but instead takes advantage of native services and processes that are part of the OS to carry out attacks.
- Does not infect a file, the code is loaded directly in the computer's RAM.

Advantages:
- Easy to infect
- Extensive control of machine
- Persistent
- Difficult to detect
- Difficult to defend against

This is because Antivirus usually are only allowed to scan the RAM segments allocated by the OS to it. Meaning the virus can evade detection by just sitting in another segment.

This is also why whenever your update your computer, you're asked to restart. The restart basically allows the OS to clean its system files before it loads, meaning if a virus is hiding somewhere it gets wiped.
### Worm
A worm is a malicious program that uses a computer network to replicate (also called a network virus). Designed to enter a computer through the network then takes advantage of a vulnerability in an app or the OS on the host computer.

Today's worms can leave behind a payload on the infected systems and cause harm. Their actions include deleting files on the computer or allowing the computer to be remotely controlled by the attacker.
### Bot
Malware that allows the infected computer to be placed under the remote control of the attack for the purpose of launching attacks. The infector robot computer is known as a robot or zombie.

When hundreds or millions of bot computers are gathered into a logical computer network they create a botnet under the control of a bot herder. Infected bot computers receive instructions through a command and control (C&C) structure from the bot herders.
### Snooping
Two common types are spyware and keyloggers

**Spyware**:
Tracking software deployed without consent or control of the user.

**Keylogger**:
Captures and stores each keystroke that a user types on the computer's keyboard. Threat actor can search the captured text for useful information such as password, credit card, etc. This can be done through a software program or a small piece of hardware.
### Deceive
Deceives user and hides their true intentions. Examples: Potentially Unwanted Programs (PUPs), Trojans, and remote access Trojans (RATs)
#### PUP
Software that user does not want on their computer (duh, it's in the name). Mostly obstructs content or interferes with daily use. Annoying as shit.
Examples:
- Search engine hijacking
- Pop ups
- Homepage hijacking
-  etc.
#### Trojan
Executable program that masquerades as a benign activity but does sth malicious.
#### RATs
Basically a Trojan but gives threat agents unauthorised remote access to your computer by using specially configured communication protocols.
### Evade
Attempts to help malware or attacks evade detection. Includes backdoor, logic bomb, and rootkit.

**Backdoor**
Gives access to computer/program/service that circumvents security protections

**Logic bomb**
Added to legitimate program but lies dormant and evades detection until a specific event invokes it

**Rootkit**
Enables threat actors to access a computer without security authorisation
## Application Attacks
Looks for vulnerability in apps or manipulate apps in order to compromise them. Most common target are [[semester-3/enterprise-java-prog32758/Lecture 1#Web Server|Web Servers]]. A web server provides services that are implemented as "web apps" through software apps running on the server.
### Scripting
In a cross-site scripting (XSS) attack, a website accepts user input without validating it and the input can be exploited. An attacker can take advantage in an XSS attack by tricking a valid website into feeding a malicious script to another user's web browser.
### Injection
Attacks called injections introduce new input to exploit a vulnerability. One of the most common injection attacks is [[Structured Query Language|SQL]] injection, where the attacker inserts statements to manipulate a database server.
### Request Forgery
Fabricates a request. There are 2 types: Cross-site Request Forgery (CSRF) and a Server-site Request Forgery (SSRF).
#### CSRF
Takes advantage of an authentication token that a website sends to a user's web browser. If a user is currently authenticated on a website and is then tricked into loading another webpage, the new page inherits the identity and privileges of the victim, who my perform an undesired function on the attacker's behalf.
### SSRF
An SSRF takes advantage of a trusting relationship between web servers. They exploit how a web server processes external information received from another server.

Some web apps are desigend to read information from or write from ...
### Replay
Most comonly used against digital identities. After intercepting and copying data, the threat actor retransmits selected and edited portions of the copied communications later to impersonate the legitimate user. Mostly between the user and the auth server.
## Attacks on Software
Focuses on vulnerabilities on software applications, including: exploiting memory vulnerabilities, improper exception/error handling, external software components.

**Memory Vulnerabilities** 
- Resource Exhaustion: Deplete parts of memory and interfere with normal operation of program in RAM
- Manipulate memory contents such as buffer [[overflow]] attacks and integer overflow attacks
- Buffer overflow: Attempts to store data in RAM beyond the boundaries of a fixed-length storage buffer => overflow data into adjacent memory segments
- Integer overflow: Changes value of a variable to something outside the range the programmer intended.
**Improper Exception Handling**
Inputs malicious data to cause software to crash due to improper validation/exception handling.

**Attacks on External Software Components**
Target external components, e.g. [[Application Program Interface|APIs]], Device Drivers, [[Dynamic-Link Library]] (DLL)
## AI and ML
A subset of [[Artificial Intelligence]] is [[Machine Learning]] (ML): teaching a technology device to learn by itself without the continual instructions of a computer programmer.

ML involves learning through repeated experience. If something attempted doesn't work, then it determines how it could be changed to make it work.
### Uses in Cybersecurity
Cybersecurity AI allows orgs to detect, predict, and respond to cyber threats in real time using ML. Virutally all email systems use some types of AI to block phishing attacks. The prime advatage is the continual learning and greater speed in response => AI can predict and prevent future attacks.

One in five cybersecurity companies use AI in their field.
### Risks in Using AI and ML in Cybersecurity
These risks are called **adversarial artificial intelligence**. 
1. Security of ML algorithms: These could be attacked and compromised to allow threat actors to alter algorithms to ignore attacks.
2. Tainted training data: Alter to training data to produce false negatives to cloak themselves.