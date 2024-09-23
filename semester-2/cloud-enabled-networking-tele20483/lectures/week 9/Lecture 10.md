# Databases
Most modern apps use Database to store data, and the data can be MASSIVE. The complex structure allows for more complicated data storage. 

There are 2 main database formats:
- Relational
- Non-relational
## RDMBS (Relational Database Management System)
A relational database stroes data in pre-defined rows in a tabl.
Relational database are ruled by schemas--definition on how the data is structured

Example: 
User Object can have:
- ID#
- Name
- Last name
- Phone 
- Email
- etc.
But they can't have things like 
- Horsepower
- Fuel capacity
- Gears

Since all the data in a RDB are arranged in a strict manner, we can retrieve it easily with a key.

## SQL
[[Structured Query Language]] (SQL) is the language used to deal with Relational Databases. For more information, refer to literally anything in [[Database Design & Implementation - DBAS27198|here]].

## Why RDB?
Fast and frequent transactions, lots of read/write operations. In the case of a large database, fast and frequent operations demand high CPU and memory capacity.

## AWS Relational Database Service (RDS)
### Amazon Aurora
AWS version of MySQL. Highly efficient in the AWS cloud environment (because you know, it's designed for the hardware). Enterprise class, costs less than $1/day. Throughput is 5x MySQL, 3x PostgreSQL. 64TB auto-scaling SSD storage. Replication across 3 Availability Zones. Automatic monitoring. Failover under 30s.
### Amazon MySQL
MySQL community edition. Most used open-source database. Includes in Free Tier. Enables scaling of compute and storage capacity. Max 64 TiB. Similar to Aurora tbh, just different language.
## MariaDB
Also community edition, is a type of MySQL DB. Open source & Free tier. Same support as the previous ones.
### PostgreSQL
Open-source version to Oracle database. Reliable and stable, advanced features for high volume environments. Supports multiple extensions.
### Oracle
Includes Standard & Enterprise Edition. You'll need a license to use this.
### Microsoft SQL
Supported by Microsoft, license already included in cost of service.
# RDS Availability Options.
Multi-Availability Zone DB cluster--cluster of 3 DB instances. Each DB instance is deployed in a different AZ.
# Storage Input-output per second (IOPS)
An IOPS is either a write or read operation to the DB, not both.
One IOPS transfers 1 page of data, page size depends on the type of storage and the DB engine. 

MySQL and MariaDB have a page size of 16KB
Oracle, PostgreSQL and Microsoft SQL Server have a page size of 8KB.

Larger page size => less IOPS to transfer the same filesize

Formula
$$
insert math here
$$
The AWS Certified Solutions Architect uses base 10 for the units of KB, MB, GB, and TB (1000B, 1mil B, etc.)

# LAMP stack on AWS
LAMP is short for Linux, Apache2, MySQL, and PHP (ewwwww). 

Linux provides the OS
Apache2 provides the webserver service
MySQL provides the DB
PHP provides scripting logic.

This only applies to distros that support Apache2. For Ubuntu and Debian systems, it'll be LEMP instead, where E is from Nginx.

This is of course a monolith installation, which makes sense since it's a small project.

## LAMP highly available
To make your app highly available, place your LAMP servers on an auto scaling group and an ELB. All these instances will connect to a Database somewhere. 