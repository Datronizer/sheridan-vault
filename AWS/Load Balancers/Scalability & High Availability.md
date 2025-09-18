# Scalability
How much an application/system can handle greater loads by adapating. There are 2 kinds:
- Vertical
- Horizontal (Elasticity)

> [!important] 
> Scalability is linked but is different to High Availability

## Vertical Scalability
Often, this means increasing the physical size of the instance.

Example 1:
I work in a lumber mill, and I have my friend Steve, 4'2", who lifts 120 lbs at a time. Vertical scaling would be to replace Steve with Steve's brother, Alex, 6'5", who lifts 300 lbs at a time. 

Example 2:
Your application runs on a `t2.micro`. Scaling this vertically means you change to running it in, say `t2.large`.

This is actually very common for non-distributed systems such as a database. Realistically if you want a bigger database, you just literally vertically scale that shit up. Unfortunately, **there is a limit** on how much you can vertically scale (**hardware limit**).

[[RDS]], [[ElastiCache]] are services that can scale vertically.
## Horizontal Scalability
Increasing the **number** of instances/systems for the application rather than scaling hardware.

Example 1: 
Steve is working at the lumber mill and lifts 120 lbs. If I don't want to bring in Steve's brother, I can bring in Steve's friends, who all lift 120 lbs. In that case, we've horizontally scaled our operations by increasing the **number** of workers.

Horizontal scaling implies distributed systems. This is often used for web apps/modern apps. However, this is not a catch-all solution as some apps/systems cannot be horizontally scaled.

Technologically speaking, it is much easier to scale horizontally thanks to cloud offerings such as [[Elastic Compute Cloud (EC2)|Amazon EC2]].

# High Availability
Usually goes hand in hand with horizontal scaling (not always). It means running your app/system in at least 2 data centres (or availability zones). 

The goal is to survive a data centre loss. 

Example: I have 2 lumber mills, one in Alberta, one in Ontario. Suppose the big saw in Alberta breaks, then instead of operations completely halting, I still have the Ontario one supplying as a backup.

The high availability can be:
- Passive (e.g. [[RDS Multi AZ]])
- Active (e.g. Horizontal scaling -- multiple different AZs)

## For EC2
For EC2, for example, these terminologies mean:

Vertical scaling: Increase instance size (scale up/down)
- From `t2.nano` - 0.5G RAM, 1 vCPU
- To `u-12tb1.metal` - 12.3TB RAM, 448 vCPUs

Horizontal scaling: Increase number of instances (scale out/in)
- Can use [[AWS Auto-Scaling Group]]
- or [[AWS Elastic Load Balancer|Elastic Load Balancer]]

High Availability: Run instances for the same app across multiple AZs
- [[AWS Auto-Scaling Group]] will multi AZ enabled
- [[AWS Elastic Load Balancer|Elastic Load Balancer]] with multi AZ enabled