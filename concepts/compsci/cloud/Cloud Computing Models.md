# The 3 cloud computing models
Cloud computing services are categorized in to three major models:
- **Platform** as a Service (PaaS)
	- Mostly used by developers who only need a platform to test or deploy their codes. 
- **Software** as a Service (SaaS)
	- Think emails and other online services. You don't need a software to send an email. Just go online and do it!
- **Infrastructure** as a Service (IaaS)
	- This is the main focus of the class. We can combine our server with firewalls, etc. Creating an entire **infrastructure**/environment, then redistributing to your developers for testing.
## Software as a Service - SaaS
The model's objective is to deliver applications from a cloud.

The SaaS cloud provider provides an application ready to use--managed by the provider, of course. The client would purchase the use of the application through subscription.

The application allows for some level of customization, and many of these apps run via web protocols. All the customer needs is access to a web browser. Typically, there is no need to install anything on the client side.

Think: Zoom, Gmail, Office 365, Teams, Dropbox, SLATE, etc. It's all subscription based. Almost no downloads needed.

Originally these companies would sell the software and the license per software. Of course having that many licenses is annoying as shit to manage. Also there's a risk of piracy (not that I'm against it or anything). To minimize these losses and inconveniences, Microsoft started offering a new tier: [[#Platform as a Service - PaaS]]
## Platform as a Service - PaaS
Heroku, nuff said.

Jk. PaaS is basically IaaS but you don't get to control the host environment. You buy a "server", push your scripts there, run it, and that's it. No modifications, everything is automated. It kinda sucks honestly, since automation makes it harder to troubleshoot. But for most development use cases, this is good!

Heroku, as foreshadowed earlier, is a service that provides you with a platform to deploy your apps. There might not be any customization, nor are there storage options, but at least for simple websites, this should be good enough!

[[#Infrastructure as a Service - IaaS|IaaS]] would be overkill for most developers unless your project is big. Else you can just self-host. 
## Infrastructure as a Service - IaaS
IaaS is a virtualization of a computer network infrastructure inside a cloud datacenter. IaaS are typically clusters of datacenters that present a configuration interface to the clients.

The customers deal with the interface and they can create and maintain their own infrastructure.

So why do companies prefer IaaS to an on-premise datacenter? Two keywords: **elasticity** and **on-demand**. 

You don't have to run it if you want to. Meanwhile on-premise datacenters need to run constantly. Also elasticity allows for server scaling based on your needs. If you don't need a lot of VMs today, you can just reduce the plan **dynamically**. Easy peasy.

Historically, to deploy something new, developers have to:
1. Design new application to run on servers
2. Plan and purchase more devices based on estimated usage
	- This will take months in advance and tons of money.
3. When the application is ready, deploy. Now 3 things can happen:
	- Correct estimation: Everything runs well
	- Underestimation: Server overloads and dies
	- Overestimation: Waste of resources

As you can see, all this can be resolved using IaaS because you can avoid all this and leave it to conglomerates to worry about the buying and upgrading.


