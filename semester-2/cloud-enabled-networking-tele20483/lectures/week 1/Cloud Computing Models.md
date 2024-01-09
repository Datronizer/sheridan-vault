Cloud computing services are categorized in to three major models:
- **Platform** as a Service (PaaS)
	- Mostly used by developers who only need a platform to test or deploy their codes. 
- **Software** as a Service (SaaS)
	- Think emails and other online services. You don't need a software to send an email. Just go online and do it!
- **Infrastructure** as a Service (IaaS)
	- This is the main focus of the class. We can combine our server with firewalls, etc. Creating an entire **infrastructure**/environment, then redistributing to your developers for testing.

# Cloud Layered Model
The model is as such, from surface to core:
1. Applications
2. Data
3. Runtime
4. Middleware
5. OS
6. Virtual Infrastructure
7. Physicial Infrastructure

This model represents the major conceptual components needed to provide any computign service.

As you can see, at the bottom, we have a physical infrastructure where the software runs. This is the physical server--it could be a datacenter, some location, some service somewhere with some network equipment.

The cloud is a virtualization of resources on top of this physical infrastructure. To do this, you need a **hypervisor**. A hypervisor is like a "translator" that translates physical properties into a virtual platform.

The cloud supports many software processes. I want you to think of it like a "virtual computer". They can run OSes, middleware, and other runtime services.

## Cloud Service Offerings Model
Here is a very good image that shows what the cloud service offers based on service tiers.
![[Pasted image 20240108121716.png]]

As you can see SaaS only offers Applications for use. This is generally good enough for most users. 
Of course developers would require Data manipulation in addition to Applications. Thus, PaaS would be better for them.
IaaS allows for deeper virtualization. You can install your own OS for use case, etc. This is what we'll be using for class.
On-premises

# Software as a Service - SaaS
The model's objective is to deliver applications from a cloud
The SaaS cloud provider provides an application ready to use.
The applications are managed by the cloud vendors.
The client purchases the use of the application of the subscription.
The application allows for some level of customization.
Many of these apps run via web protocols. All that the customer needs is to have access to a web browser.
Typically, there is no need to install anything on the client side.

Examples: Zoom, Gmail, Office 365, Teams, Dropbox, SLATE, etc. It's all subscription based.

Originally these companies would sell the software and the license per software. Of course having that many licenses is annoying as shit to manage. Also there's a risk of piracy (not that I'm against it or anything). To minimize these losses and inconveniences, Microsoft started offering

# Platform as a Service - PaaS
Heroku, nuff said.

Jk. PaaS is basically IaaS but you don't get to control the host environment. You buy a "server", push your scripts there, run it, and that's it. No modifications, everything is automated. It kinda sucks honestly, since automation makes it harder to troubleshoot. But for most development use cases, this is good!

IaaS would be overkill for most developers unless your project is big. Else you can just self-host. Wait, is that a segue to the next header-

# Infrastructure as a Service - IaaS
IaaS is a virtualization of a computer network infrastructure inside a cloud datacenter. IaaS are typically clusters of datacenters that present a configuration interface to the clients.

The customers deal with the interface and they can create and maintain their own infrastructure.

So why do companies prefer IaaS to an on-premise datacenter? Two things: **elasticity** and **on-demand**. 

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
# Scaling
## Vertical scaling
Used for applications that need a lot of bandwidth. 
- **Scaling up** means adding more capacity to an existing resource. That or changing the instance type, exmaple: changing a server from **T**iny size to e**X**tra size.
- **Scaling down**: the reverse lol. Dropping capacity due to excess storage for example.
## Horizontal scaling
Web servers will use horizontal scaling because they don't need bandwidth, they need instances instead. Think microservices. You don't need a "bigger" CPU, you just need more instances to independently process requests.

AWS can usually do auto-scaling for your use case. They don't automatically vertically scale your server though. That has to be done manually.
