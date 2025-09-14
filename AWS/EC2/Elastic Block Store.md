---
aliases:
  - EBS
  - AWS EBS
  - EC2 EBS
  - EBS Volume
---
# Introduction
An Elastic Block Store (EBS) Volume is a *network drive* you can attach to your instances while they run. It allows your instances to persist data, even after terminination. 

In other words, you can terminate an instance, and mount the same EBS to a new instance you just spun up.

But, they can only be mounted to 1 instance at a time (at the CCP level)*.

> [!important]
> For all intents and purposes, **Certified Cloud Practitioners (CCP)** only needs to know that 1 EBS mounts to only 1 EC2 instance
> 
> In reality, for **Associate Levels** (Solutions Architect, Developer, SysOps), you can use the "[[#EBS Multi-Attach|multi-attach]]" feature for some EBS

EBS volumes are also locked to a specific availability zone. You cannot use an EBS Volume in `us-east-1a` to mount to an instance in `us-east-1b`. You can, however, move a volume using [[snapshots]], but we'll talk about that later.

EBS Volumes also have a provisioned capacity (size in GBs, IOPS). You get billed for this btw, and all future scaling of your volumes.

Now for some fun things you can do:
- You can mount 1 EBS to 1 EC2
- You can mount multiple EBS Volumes of different sizes to an EC2 instance
- You can even create EBS Volumes and leave them unattached (why the fuck would you do this?)
# Network Drive?
Earlier we mentioned that an EBS Volume is a network drive. So what is it?

A network drive, as the name suggests, is a virtual drive that uses the network to communicate with the instance. Basically the server pools all possible storage into a "mega-storage". Then it partitions it into small chunks and gives these chunks to instances. These "chunks" may or may not be contiguous data, we don't really care. Just know that it communicates via network.

And such, since it is network-based, there is some latency. But because it's virtual, you can detach it from one EC2 instance and attach to another one quickly.

# Delete on Termination
When you create new EBS Volumes, you will see a column that says "Delete on Termination". As the name suggests, this allows you to set the EBS Volume so that it deletes itself if the EC2 instance is terminated.

Note that the `root` volume is defaulted to delete on termination, but any other volumes you create will not. You will have to manually tick it.

An important use case here is that you can preserve storage data in volumes even after the EC2 instance is gone.

You can also automate this process through AWS console / AWS CLI. 

# EBS Snapshot
It is a backup (snapshot) of your EBS volume at a point in time. You don't have to detach volume to do snapshots but it is recommended.

You can also copy snapshots across AZs or Regions. This is actually how you can carry volumes between AZs and Regions (by "restoring" a volume from a snapshot).
## EBS Snapshot Archive
Moves a snapshot into an "archive tier" that is 75% cheaper. Takes 24-72hrs to restore archive.
## Recycle Bin for EBS Snapshots
Setup rules to retain deleted snapshots so you can recover them after accidental deletion. You can specify retention (how long the thing can stay in there before perma-wipe), from 1 day - 1 year.
## Fast Snapshot Restore (FSR)
Forces full initialization of snapshot to have no latency on first use. You can use this if you need to urgently fire up a snapshot with no wait time.

Yes of course this costs a shit ton.

# EBS Volume Types
EBS volumes come in 6 types.
- gp2 / gp3 (SSD): General purpose SSD volume that balances price & performance for a wide variety of workloads.
- io1 / io2 Block Express (SSD): Highest-performance SSD volume for mission-critical low-latency / high-throughput workloads
- st1 (HDD): Low cost HDD Volume designed for frequently accessed, throughput-intensive workloads
- sc1 (HDD): Lowest cost HDD volume designed for less frequently accessed workloads

EBS Volumes are characterized by Size | Throughput | IOPS. If you don't remember, read the docs. 

> [!important] 
> Only gp2/gp3 and io1/io2 Block Express can be used as boot volumes.

## General Purpose SSD
That's what gp in gp2/gp3 stands for btw. What are its attributes:
- Cost effective storage, low-latency
- Used for System boot volumes, Virtual desktops, Dev and test environments
- 1 GiB - 16 TiB
- gp3: newer gen
	- Baseline 3000 IOPS, throughput 125 MiB/s
	- Can increase up to 16000 IOPS, 1000 MiB/s independently
- gp2:
	- Small gp2 volumes can burst IOPS to 3000
	- Size of volume and IOPS are linked, max 16000 IOPS
	- 3 IOPS per GB => 5334 GB gives max IOPS

## Provisioned IOPS (PIOPS) SSD
This is what io1/io2 stands for btw.
- Used for critical business applications with sustained IOPS performance
- Or any apps that need more than 16000 IOPS
- Great for database workloads (sensitive to storage performance / consistency)
- io1 (4 GiB - 16 TiB)
	- Max PIOPS: 64000 for **Nitro EC2 instances**, 32000 for others
		- You need Nitro EC2 for this btw, else 32k max
	- Can increase PIOPS independently from storage size
- io2 Block Express (4 GiB - 64 TiB)
	- Sub-millisecond latency
	- Max PIOPS: 256,000 with IOPS:GiB ratio of 1000:1
- Supports EBS Multi-attach

## Hard Disk Drives (HDD)
- Can't be used as boot volumes
- 125 GiB - 16 TiB
- Throughput optimized HDD (st1)
	- Big Data, Data Warehouses, Log Processing
	- Max throughput 500 MiB/s, 500 IOPS
- Cold HDD (sc1)
	- For infrequently accessed data 
	- Scenarios where lowest cost is important
	- Max throughput 250 MiB/s, 250 IOPS

# EBS Multi-Attach
This ONLY APPLIES TO [[#Provisioned IOPS (PIOPS) SSD|io1/io2]] family. With this feature, you can attach the same EBS volume to multiple EC2 instances in the same AZ.

Each instance has full read/write perms to the high-performance volume. 

The use cases for this are kinda specific:
- Achieve higher app availability in clustered Linux apps (e.g. Teradata)
- Apps must manage concurrent write operations

Limitations:
- Instances must all be in the same AZ with io1/io2 volume
- Max 16 instances can be attached to 1 volume at a time
- Must use a file system that is cluster-aware (cannot use XFS, EXT4, etc.)