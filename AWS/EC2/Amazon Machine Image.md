---
aliases:
  - AMI
  - AWS AMI
  - EC2 AMI
---
# Overview
Amazon Machine Images (AMI) are a customization of an [[Elastic Compute Cloud (EC2)|EC2]] instance. 
- You add your own software, config, OS, monitoring, etc.
- Faster boot/config time because all your software is pre-packaged

AMIs are built for a specific region and can be copied across regions.
You can launch EC2 instances from:
- Public AMIs: AWS-provided, we've been using this
- Custom AMIs: Make and maintain by yourself
- AWS Marketplace AMI: made by someone else (for possibly a price)

# The process
Creating your own AMI is easy as pie. There are 4 steps.
1. Start EC2 instance and customize it
2. Stop the instance (for data integrity)
3. Build an AMI - this will also create EBS snapshots
4. Launch instances from other AMIs

