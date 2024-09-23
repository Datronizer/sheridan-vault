# What is InfoSec
## Security
Definition of security:
- To be free from danger
- Any process to achieve aforementioned freedom
As security increases => convenience decreases
- Basically, the stronger the security, the more annoying the service is to use (Sienna accessing her Gmail)
## Information Security (InfoSec)
Basically describes the task of securing digital information wherever it is, such as:
- Manipulated by a microprocessor
- Storage device
- Transmitted over the network
3 types of information protection (CIA triad) (what the fuck is this term)
1. Confidentiality
	- Only approved individuals can access this info (Checks user)
2. Integrity
	- Ensures this info is correct and unaltered (Checks data)
3. Availability
	- Ensures this info is accessible to authorised users (Let user access after check)

For context, refer to Figure 1-2 in the textbook 
![[Pasted image 20240904093509.png]]

The triad is transmitted/processed/stored through the use of hardware and software aka **products**. The **people** then uses the products under the guidelines of **policies and procedures**.

The problem lies in the people in this case (most of the time). When people don't follow procedures and policies, it opens up avenues for attack by threat actors such as social engineering, getting your ID swiped, etc.
# Threat Actors
A threat actor is an individual/entity/organisation responsible for cyber incidents against the technology equipment of enterprises and users. We also call them **attackers**.

Financial crime is often divided into 3 categories based on targets:
- Individual users
- Enterprises
- Governments (WOOOOOO)

There are 3 types of hackers:
- Black hat hackers
- White hat hackers
- Gray hat hackers
## Script Kiddies
Dickheads that want to perform attacks without any technical knowledge. They use freely available automated attack software such as scripts. These guys are fuckin losers.
## Hacktivists
Hackers motivated by ideology. They often break into websites and change its contents as a means of a political statement. Sometimes attacks are retaliatory aka attacking a bank that blocks donations made to their groups (Anonymous)
## State Actors
Government-sponsored attackers deployed against said governments' foes. Unlimited money and resources to hack thanks to sponsorship so they are incredibly dangerous.

Example: New York's dam got hacked to flood the state.

There's a new class of attacks called **advanced persistent threat (APT)**, which are multiyear intrusion campaigns targeting sensitive economic, proprietary, national security info.

Go to [this site](https://cybermap.kaspersky.com) to see all live attacks right now.
## Insiders
Employees, contractors, business partners can pose an insider threat of manipulating data from the position of a trusted employee. Harder to detect since they're from the inside. 6/10 enterprises reported being a victim of at least one insider attack during 2019. 

Main focus:
- Intellectual property theft: 43%
- Sabotage: 41%
- Espionage: 32%
## Other threat actors
Competitors: Competing corporations attacking
Criminal Syndicates: Online criminal networks 
Shadow IT: Employees frustrated with corporate bullshit installing their own stuff to speed up their work and infecting the network by accident 
Brokers: Stealing data and selling them
Cyber-terrorists: Attack nations' system to cause panic
# Vulnerabilities and Attacks
One of the most successful types of attack is social engineering (they don't even  need to exploit tech vulnerabilities). 
## Vulnerabilities
A vulnerability is the state of being exposed to the possibility of being attacked or harmed. These can be categorised into platforms, configurations, 3rd parties, patches, and zero-day vulnerabilities.
### Platforms
A platform is a system that consists of the hardware and an OS that runs software. 
All platforms have some degree of vulnerability, some have serious vulnerabilities, including:
- Legacy platforms
- On-premise platforms
- Cloud platforms
### Configurations
Improper privileges, weak passwords, weak configs, etc.
### 3rd-Party Vulnerabilities
Almost all businesses use external entities known as 3rd-parties. Examples include: outsourced code development, data storage facilities, etc.

Vendor management is the process organizations use to monitor and manage the interactions with all of their external third parties. 

Connectivity between the org and the 3rd-party is known as **system integration**. One of the major security risks with system integration is the **principle of the weakest link**.
### Patches
Patches, though important, can create vulnerabilities:
- Difficulty patching firmware
- Few patches for application software
- Delays in patching OSes
### Zero Day
Vulnerabilities can be exploited by attackers before anyone even knows it exists. This type of vulnerability is called a zero-day because it provides zero days of warning. Zero-day vulnerabilities are extremely serious.
## Attack Vectors
A pathway or method used by a threat actor to penetrate a system. They can be grouped into the following general categories:
- Social Engineering
### Social Engineering
Eliciting information by using the weaknesses of individuals. Sway attention, sympathy, can be used on social media, etc. 
#### Psychological principles
They can use psychological principles to gain trust:
- Provide a reason
- Project confidence
- Use evasion and diversion
- Make them laugh
#### Impersonation
They can also use **impersonation** to pretend to be a fictitious character and elicit information from there. 
#### Phishing
They can also utilise **phishing** by sending an dupe email/web announcement to trick the user into surrendering private information or taking action. There are some variations such as:
- Spear phising
	- Mass email to users and attempt to exploit information
- Whaling
	- Targeted towards wealthy and powerful people
- Vishing
	- Manipulate the victim through phone calls (VOICE PHISHING WAHT???)
- Smishing (who the fuck named these)
	- Same thing but through SMS (OHHHH SMS PHISHING THATS SUCH A STUPID FUCKING NAME)
#### Redirection
Directs a user to a fake lookalike site filled with ads for which the attacker receives money for the traffic to the site.
- Typo Squatting: Buying a domain name similarly spelt to real site
- Pharming: Exploit how a URL is converted to corresponding IP address 
#### Spam
Unsolicited email to large number of recipients
- Text based spam can be filtered
- Image spam cannot be filtered
- Spim: Spamming through IM (I swear IT mfs need to stop naming things)
#### Hoaxes
False warnings coming from the "IT dept".
#### Watering hole attack
Targeting smaller group of specific individuals through fake sites etc.
### Physical Procedures
Take advantage of user actions. Three main ways:
1. Dumpster Diving: Digging through trash for info that might be useful. 
	- Digital dumpster diving is exploiting someone sharing a Google Drive link willy-nilly
	- Calendar exploit: Figuring when employee is out of town
	- Stealing USB
	- Organisational charts: Spot individuals who are positions of authority
	- Phone directories: Find targets to impersonate
	- Policy manual: Reveal true level of security within the organisation
	- System manual
2. Tailgating: Follow an authorised person through a door and pretend to be a staff
3. Shoulder Surfing: Looking at the victim's typing over their shoulder and steal data.

## Impacts of Attacks
### Data impact
- Data Lost: Destroys data so it can't be recovered. 
- Data Exfiltration: Steal data and selling to a competitor
- Data Breach: Steal credit card info
- Identity Theft: Steal user personal info to impersonate
### Effects on Enterprise
- Availability lost: Can't access systems
	- Financial lost: Can't access => can't work => money loss
- Reputation: Affect public perception of the enterprise