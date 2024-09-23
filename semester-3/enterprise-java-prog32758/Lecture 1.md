# Client-Server Architecture
## History
It all started with Mainframe Programming where we used punch cards to tell computers what to do. It was basic but it worked. As time goes on, we developed the terminal to work with our CPU and Memory. How does the terminal work?

Answer: Character Coding. We type something on the typewriter, and the character "codes" into the mainframe. But how does this work? Say hello to [[ASCII|encoding]], where we turn binary into a sequence to represent 1 character.

As technology develops, we increased computer power and terminals can finally do the encoding itself. But what if we expanded this further? We use this terminal to communicate with another computer, thus the idea of the [[Client]] was born.

With all these computers communicating with each other, humanity finally created a [[Lecture 1 - TELE13167#Network|computer network]]. And to facilitate these conversations, we made [[Lecture 1 - TELE13167#Data communication|protocols]], the first of which being [[TCP|TCP/IP]].

Then one leads to another, we have [[packets]], [[routing]], etc.

Anyways, going back to the topic at hand. Some tasks we want to keep private and only send the results to the user. Some tasks we would prefer being done on the user's device so it doesn't clog ours. This exact design architecture is called the [[#Client-Server Architecture]].
## Description
The definitions are pretty straightforward, but how an application is designed to fit this box is a realm of its own, mostly because it depends greatly on use case + developers' discretion.
### Web Client
A web application (oftentimes a [[browser]]) that runs on the client is a Client App. The client's roles and duties depend heavily on the developers' discretion.  
#### Roles
- Generate a well-structured [[HTTP#Request|Request Object]]
- Communicate that Request Object to the server
- Receive and process the [[HTTP#Response|Response Object]], generally displaying the server-side render.
### Web Server
A web application that runs on the server is a Server App. Popular web servers (underlying software running on some sort of hardware) are Apache-Tomcat, NGINX, etc.
#### Roles
Some popular server roles include:
- Receive and analyze the Request Object 
- Process the Request Object 
- Generate a well-structured Response Object
- Communicate that Response Object to the client 

# Web Pages and Web Applications
## Web Apps
Client-Server Architecture
Communication between client and server through protocols and request/response model.
## Web pages
Content:
- Static content
	- Unchanging content, often hardcoded into HTML.
- Dynamic content
	- Content that changes based on up-to-date data, organised by a template, is main focus of the course.

Look and feel (CSS)
- Not main focus for this course.

For this class, we will be using Template Engine to handle templates that will house dynamic content. ThymeLeaf will also help.

Web App Development follows a 2-stage process: Development and Deployment.
# Object-Oriented Programming
hhhehaheahehaehahehehehehehehehehehe
![[Pasted image 20240904134126.png]]

^^^ Sienna is losing her shit

everywhere i go i see his face ^^^^^
