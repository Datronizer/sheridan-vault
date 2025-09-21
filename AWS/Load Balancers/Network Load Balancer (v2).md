These are Layer 4 load balancers and they allow you to :
- Forward TCP & UDP traffic to your instances
- Handle millions of requests per seconds
- Ultra-low latency

Only has 1 static IP per AZ, and supports assigning Elastic IP (helpful for whitelisting specific IP).

Used for extreme performance, accesses TCP & UDP.

# Target Groups
Can be:
- EC2 Instances
- IP Addresses (must be hard-coded private IPs, either of AWS EC2 instance or on-prem servers)
- Application Load Balancer (Forward NLB traffic to ALB)
- Health checks performed by NLBs support TCP, HTTP, and HTTPS protocols.