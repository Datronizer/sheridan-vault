# Simple Storage Service (S3)
<small>Oh so that's what S3 stands for</small>

AWS allows storage of any amount of data from anywhere on the web. Think of it like a storage platform. It only takes flat files so folders are out of of the question. 

Of course this means if you want to retrieve and edit objects and data, this is a terrible solution, but for simple static sites, this will do just fine. This is called **object storage**.

The fundamental structure of S3 is a main folder called the **bucket**. And you can put directories and stuff in it (maybe I'm wrong above).

The storage system uses keys and values and details the hierarchy of the objects aforementioned.

You can have as many buckets as you want, but 1 bucket can only have a max of 5TB (what the fuck). There's also a limit on PUT requests (upload) size of 5 GB. 

Suppose you want to upload something over 100MB, you should use (by recommendation) Amazon's Multi Upload C(something something).
## Pricing
Pay per usage, billing based on the region of your bucket.
They might also charge when data is transferred, but that depends on cross-region transfers, etc etc.
## Availability
Again, this is the percentage of successful external connectivity. For AWS it's like 99.99% availability (what the fuck). That means 99.99% of the time, when you attempt to connect, it SHOULD work (in theory of course, cough cough Riot Games servers).

This 99.99% is computed by Amazon, so... if you want to make sure it's what you want, you should check out their Service Level Agreement (SLA).
## Reliability
By Amazon's definition: "the ability of a workload to perform its intended function correctly and consistently when it is expected to."

Some AWS services claim to have a reliability of 99.999999999% (the 11 9's rule) (yeah I don't know how this is calculated either, sounds bullshit).
# Provided Services
## S3 Standard
Default storage system. Designed to be replicated across 3 or more Availability Zones.
## S3 Infrequent Access
Used for data that requires less frequent access than the S3 standard, but when the data is needed, must be transferred quickly. Also deployed in 3 AZs.

Cheaper than S3 standard, but they charge per data retrieval.
## S3 One Zone Infrequent Access
Same as above but 1 AZ. Of course this means if that AZ dies, you're cooked. Hence it's the cheapest.
## S3 Intelligent Tiering
Uses AI to detect what part of your data is most frequently accessed and sends it to that region to save costs.
## Glacier
For long term data storage (haha, get it? Because the data is frozen?). If you use data though, they charge the fuck out of you.
## Glacier Deep Archive
Cheapest long term storage of data. Absolutely ridiculously long retrieval time.
## S3 Outpost
Remember [[semester-2/cloud-enabled-networking-tele20483/lectures/week 2/Lecture 2#AWS Outpost|this]]? Basically same thing, they just place an AWS tower on your premises.
# S3 locations
AWS has a commons service area (the AWS Public Zone), contains services available to all AWS customers
## Accessing S3 resources
Depends on your needs. Suppose you only want storage for your instances to use, then you don't need Internet access from S3. However, you do need to hook your EC2 instances to the IGW to access the S3 bucket.

If you want to keep your instances private, you can use a NAT gateway to give them access to the Internet while restricting access inwards. Or... use an **endpoint** (we'll talk about this later)

To access from the Internet, we need to switch the **Public Access** filter that blocks the address to **allow** instead. That and we might need a **security policy** (more on this later).

### Security Policy
A small JSON file that allows access to the S3 bucket. Can specify path and rights.
# Storage on S3
## Storage Services
There are a few types of storage offered by S3:
- Simple Storage Service S3 (as mentioned earlier)
- Elastic File System (I mean, the name kinda explains it)
- FSx (for Windows)
- Stirage Gateway (VM with IP, managed by AWS)
- AWS backup (centralized data backup)

# Cross Origin Resource Sharing (CORS)
<small>Oh so that's what CORS stands for (what the fuck am I talking about I already know this)</small>

Basically, think of it like a Security Group for a website. You want to allow traffic in from somewhere specific? You'll need to pass it through CORS.

INFO24178 -- next course in line with TELE