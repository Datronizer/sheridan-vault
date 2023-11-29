# Client server
Imagine a webpage being hosted on a server => that's a client server.
- Pros
	- Secure (works with most applications)
	- One server hosts a webpage 24/7
- Cons:
	- Expensive, has to run 24/7
	- Too many clients will crash a server
# Peer to Peer
- Pros
	- More users => Speed increases
	- Quite inexpensive
- Cons:
	- Few users => Speed quite low
	- Security issues
	- Can't be used for everything
- Example:
	- Good example is Torrent
	- Windows uses P2P to deliver update packages
	- Online games use P2P to download games
	- Crypto uses blockchain P2P
# Comparison
| Client server | P2P |
| ------------- | --- |
|               |     |
|               |     |

# Web Browser
A web browser is an application that allows you to acccess a website. It usually stores certain data in a server cache to prevent unnecessary API calls.
# Cookies
Data created by a website stored locally. Tracks activities on a website. Can be used to make web use easier and faster.
# URL
www.example.com/public/documents/example.htm
^         ^                 ^                             ^ 
host     domain       path                         file
# WWW: HTTP
HTTP is the protocol used to retrieve web documents stored on web servers and displays them on your screen
There are 2 modes for HTTP:
- Persistent
	- Constant connection
- Non-persistent
	- Connection only on request, made to work around old technology issues regarding dial-up

HTTP will use command GET to display the web page (the URL specifies the exact document the user wants).
The source port will be an ephemeral port and the destination (at the server) will be port 80.
The main issue with HTTP is it is not secure: it can be run over SSL tho.

HTTP Commands:
- GET
- PUT
- POST
- HEAD
- etc.
# WWW: FTP
File transfer protocol
FTP is used to download/upload file.
- GET is used to download
- PUT is used to upload
Port 20 is used on the server, Ephemeral port is used on the client.
Control is established first and remains active for the entire connection
# Email Architecture
There are 3 components to Email.
- User Agent (UA)
- Message Transfer Agent (MTA)
- Message Access Agent (MAA)
User Agent is a program/software that can be used to read/write/access your email.

There are 2 parts to an email: local name and domain name. You can probably guess what this means: johndoe@email.com.
## MTA: STMP: Email Pusher
Refer to powerpoint
Basically this is an email "pusher". It takes in information and pushes the email to the recipient based on what information it sees.
## MTA: POP3: Email Puller
Post Office Protocol 3 is a very basic email retriever.
Requests a username, a password, then POP3 downloads the email to the device and deletes it from the server (by default)
You cannot preview your email
You cannot view the email on multiple devices
There is a setting that allows you to "keep the email" on the server tho (I imagine this is added later on)
## MTA: IMAP4: Modern Email Puller
Think of all the POP3 downsides. Cool IMAP4 is the opposite, have fun.
## Web-based Email
Most cases we would connect using HTTP to a web server. Then the web server uses SMTP and POP3/IMAP4 for us.
# TELNET
TErminaL NETwork (I know this acronym fucking sucks). It is a remote access application. Think Teamviewer but only with text based. Unfortunately it sucks more than its acronym and sends passwords in plaintext.
# SSH: Secure Shell: Remote Logging
Now that's a good acronym.
It's a replacement for TELNET.
One of the main applications is port forwarding: SSH makes a secure tunnel [fill in the blank here from powerpoint]
# NVT: Network Virtual Terminal
Translates input from different OS'es across networks.
# MIME
Enables you to send non ASCII characters over email.