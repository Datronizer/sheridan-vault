# Overview
Thought problem: EBS volumes are [[Elastic Block Store#Network Drive?|network drives]]. They're good enough, but are limited. What would be a better alternative?

Answer: A physical drive. In our case, a high-performance hardware disk attached to the server called EC2 Instance Store.

This Instance Store has better I/O performance (like crazy better, easily 10x and more), but if you stop them, then the EC2 Instance Store loses their storage (ephemeral storage).

On top of that, in case the online server of the Instance Store fails, then you risk data loss. Backups and Replication are YOUR responsibility

Then what is it good for? Well... it's good for buffer / cache / scratch data / temp content. Basically non permanent data.
