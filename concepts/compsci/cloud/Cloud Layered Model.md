# Definition
The model is as such, from surface (all the way top) to core (all the way down):
1. Applications
2. Data
3. Runtime
4. Middleware
5. OS
6. Virtual Infrastructure
7. Physical Infrastructure

This model represents the major conceptual components needed to provide any computing service.

As you can see, at the bottom, we have a physical infrastructure where the software runs. This is the physical server--it could be a datacenter, some location, some service somewhere with some network equipment. 

The cloud is a [[virtualization]] of resources on top of this physical infrastructure. To do this, you need a **hypervisor**. A hypervisor is like a "translator" that translates physical properties into a virtual platform.

The cloud supports many software processes. I want you to think of it like a "virtual computer". They can run OSes, middleware, and other runtime services.

## Cloud Service Offerings Model
Cloud services are offered based on service tiers. This is how they make money by the way. 

The cloud providers provide services from the bottom up (physical layer -> virtualization -> applications). The customer access services from the top down (based on your service tier). The demarcation point for these services determines what service tier you're on.

Here is a very good image that shows what the cloud service offers based on service tiers.
![[Pasted image 20240108121716 1.png]]

- As you can see SaaS only offers Applications for use. This is generally good enough for most users. 
- Of course developers would require Data manipulation in addition to Applications. Thus, PaaS would be better for them.
- IaaS allows for deeper virtualization. You can install your own OS for use case, etc. This is what we'll be using for class.
- On-premises is for when you need the entire service, all the way down the the physical aspects. Most people don't need this unless you're a really big company/you need security.
