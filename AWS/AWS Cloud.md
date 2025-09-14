# History
Launched internally in 2002 at amazon.com, bc they thought that their IT tech can be externalized. They thought that their infrastructure is one of their core strengths, so obviously, send that shit to the market! Surely people would love this (they did).

They launched with only SQS, then they re-launched publicly with SQS, S3, EC2 in 2006, then 2007 they launched in Europe.

Right now, AWS is the leader for Cloud provision services, pulling in $90B in annual revenue, accounting for 31% of the market, leader for 13 fucking years in a row. Microsoft is close 2nd at 25%. 

# Use cases
Build sophisticated, scalable applications, that are applicable to a diverse set of industries. Can be used for Backup, Enterprise IT, mobile apps, storage, run a game server lmao.

# AWS Global Infrastructure
EDIT: There used to be a [map](https://infrastructure.aws/) that shows where they are but they took that shit down lmao.
EDIT 2: THE MAP CAME BACK, BUT ITS NOT 3D WAAAAAAAAH
## AWS Regions
### Definition
Regions are all around the world. They have names like `us-east-1`, `eu-west-3`. Basically it is a **cluster of data centers**. Most AWS services are **region-scoped**. This means that if you make 42 EC2 instances in `us-east-1`, and you open `us-west-2`, you bet your ass that shit will be empty.
### Choosing the right Region
The answer to what Region you should choose to launch your new application is that: "**It depends**". There are a lot of things to determine prior to selecting a Region. For example, the **CPAP** checklist:
- **Compliance**: following local data governance and legal requirements (data will never leave a Region without your explicit permission).
- **Proximity**: reduce latency for customers (EU -> Asia is better than EU -> Australia).
- **Available Services**: new services aren't available in every Region
- **Pricing**: pricing varies between regions, but is transparent in the service pricing page.
## AWS Availability Zones (AZ)
This is a subunit of a [[AWS Cloud#AWS Regions|Region]]. Each Region has many AZ's (usually 3, min. 3 and max. 6). Example for the Sydney region:
- `ap-southeast-2` will contain
	- `ap-southeast-2a`
	- `ap-southeast-2b`
	- `ap-southeast-2c`

Every AZ is one or more discrete data centers with redundant power, networking, and connectivity. These AZ are separate from each other by design to isolate each of them from disasters. These AZs are connected with high bandwidth, ultra-low latency networking.
## AWS Data Centers
Bro did not talk about this one
## AWS Edge Locations / Points of Presence
There are 400+ PoP (400+ Edge Locations & 10+ Regional Caches) in 90+ cities across 40+ countries. This really wide distribution allows content to be delivered to end users with lower latency

# AWS Console
This is where all your AWS actions and information are. It's literally the Dashboard of AWS per se. Ignore the fuckin UI, it'll change like twice a year. Just know the main concepts

A very quick verbal walkthrough, top down, left to right, on April 2025:
- On the top bar:
	- Services: Tells you what services there are, sorted by alphabetical order.
	- Search bar: Finds services, articles, guides, etc. that are relevant to your search (usually you'd use this to find services)
	- [[#AWS Regions|Regions]]: This will say the current region you're logged in. If a service is global, it will say `Global`
	- Your root ID: This is your account. Click to expand options or to go to account dashboard.
- Left pane: 
	- Glossary of all the features in the current service.
	- If you're not in a service, shows you the list of all services.
- Middle screen:
	- Main screen: all your operations, clicky buttons, and settings for your services are in here. This is where you'll spend most of your time.
- Right pane: 
	- Additional info, definitions, or guides on current services. Doesn't matter that much.

AWS does have a few global services that can override that pesky AWS Region restriction. These include:
- Identity and Access Management (IAM)
- Route 53 (DNS Service)
- CloudFront (Content Delivery Network)
- WAF (Web Application Firewall)

Most AWS services are unfortunately [[AWS Cloud#AWS Regions|Region]]-scoped:
- Amazon EC2 ([[concepts/compsci/cloud/Cloud Computing Models#Infrastructure as a Service - IaaS|IaaS]])
- Elastic Beanstalk ([[concepts/compsci/cloud/Cloud Computing Models#Platform as a Service - PaaS|PaaS]])
- Lambda (Function as a Service - [[FaaS]])
- Rekognition ([[concepts/compsci/cloud/Cloud Computing Models#Software as a Service - SaaS|SaaS]])

If you want to know if a service is available in a region, use [Amazon's Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) tool.
# Common Questions for this Section
1. If you need to launch a new application, where would you do it?
	- It depends.