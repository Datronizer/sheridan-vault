---
aliases:
  - AWS EFS
  - EFS
  - Amazon EFS
---
An Elastic File System (EFS) is a managed Network File System (NFS) that can be mounted on many EC2 instances. Each of these EC2 instances can be in different AZs.

Highly available, scalable, and highly expensive (3x more than a gp2 volume), and it's pay per use.

Example: You have 3 EC2 instances, each in AZs `a, b, c` separately of region `us-east-1`. All of these instances can connect to an EFS, protected by a [[EC2 Security Group|Security Group]]. This allows instances from different AZs to share and manipulate the same files in the EFS.

Some use cases include:
- Content management
- Web serving
- Data sharing
- Wordpress

EFS uses NFSv4.1 protocol, and it uses a Security group to control access.
It is also only compatible with Linux-based AMIs, and uses encryption at rest using [[Key Management Software|KMS]].

POSIX file system (~Linux) that has a standard file API. 
File system scaled automatically, pay per use, and no capacity planning
# Performance and Storage Classes
## Performance Classes
### EFS Scale
- 1000s of concurrent NFS clients, 10 GB+/s throughput
- Grow to Petabyte-scale NFS automatically
### Performance Mode
This must be set at EFS creation time.
- General Purpose (default) - latency-sensitive use cases (web server, CMS, etc.)
- Max I/O - higher latency, but higher throughput, highly parallel (big data, media processing, etc.)
### Throughput Mode
- Bursting - 1 TB = 50 MiB/s + burst of up to 100 MiB/s
- Provisioned - set throughput regardless of storage size, e.g. 1 GiB/s for 1TB storage
- Elastic - auto scale throughput up and down based on workloads
	- Up to 3 GiB/s for reads, 1GiB/s for writes
	- Used for unpredictable workloads

## Storage Classes
### Storage Tiers 
(Includes lifecycle management feature--move file after N days)
- Standard: for frequently accessed files
- Infrequent Access (EFS-IA): costs money to retrieve files, lower storage costs
- Archive: rarely accessed data (few times each year), 50% cheaper

You can implement lifecycle policies to move files between storage tiers.
### Availability and Durability
- Standard: Multi-AZ, great for prod
- One Zone: One AZ, great for dev, backup enabled by default, compat with IA (EFS One Zone-IA)

> [!note]
> Remember that One Zone locks your EFS to just 1 AZ, meaning if that AZ goes down, your data is completely inaccessible until it comes back on.
> 
>Use One Zone only for Dev environments. For Prod, use Regional. 

By using the correct classes, you can get up to 90% in cost savings.

# EBS vs EFS
EBS Volumes:
- Attached to 1 instance only (except [[Elastic Block Store#EBS Multi-Attach|multi-attach]] for io1/io2)
- Locked at the AZ level
- gp2: IO increases if disk size increases
- gp3 & io1: can increase IO independently

Migrating EBS volumes across AZs:
1. Take a snapshot
2. Restore snapshots in another AZ
3. EBS backups use IO and shouldn't be run while application is handling a lot of traffic

Root EBS Volumes of instances get terminated by default if EC2 instance is terminated (feature can be disabled)


EFS:
- Mounts 100s of instances across AZ
- EFS share website files (WordPress)
- Only for Linux instances (POSIX)
- Higher price point than EBS
- Can leverage [[#Storage Tiers]] for cost savings

Don't confuse EBS v. EFS v. Instance Store