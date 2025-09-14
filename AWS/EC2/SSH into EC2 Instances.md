# General information
For more information about [[Secure Shell]], check out the relevant document. For our case, all we need to know when it comes to device-specific connections is this

| --            | SSH | PuTTY | EC2 Instance Connect |
| ------------- | --- | ----- | -------------------- |
| Mac           | Y   | N     | Y                    |
| Linux         | Y   | N     | Y                    |
| Windows < 10  | N   | Y     | Y                    |
| Windows >= 10 | Y   | Y     | Y                    |
EC2 Instance Connect is a proprietary way to connect to EC2 instances, but the instance must be running Amazon Linux 2 or higher.

# Connecting to your instance
## The traditional way
To connect to your instance, do `ssh ec2-user@xxx.xxx.xxx.xxx -i yourKey.pem`. For this command:
- `ec2-user`: Default EC2 user account for the instance (this is the root account)
- `@`: Delimiter between user account and the address
- `xxx.xxx.xxx.xxx`: IP address of device (instance) you wish to connect
- `-i`: (argument) include identity file a.k.a. key file
- `yourKey.pem`: your key file

## The convenient way
You can connect to an instance without using SSH or a terminal!
1. On your AWS Management Console, go to EC2 -> Instances -> Select your instance.
2. If your instance is running, click Connect
3. Choose EC2 Instance Connect

In that menu, you can make whatever changes you want but the default is fine too. When using EC2 instance connect, AWS generates a temporary SSH key for you and allows you to connect to your instance using an browser terminal.

EC2 Instance Connect does get affected by [[EC2 Security Group|SG]] SSH settings. If you don't allow access, it will fail.

# What can you do?
Well, since you're in an EC2 instance with AWS CLI pre-installed (if you use AMI 2023), then you can execute AWS commands.

## What could possibly go wrong?
You will probably try to do something like `aws iam list-users` and the thing will immediately shit itself. It will not let you do that and ask you to use `aws configure`.

DO NOT USE `aws configure`!!!

Using this on an instance that may be accessible by other users that have your key is like surrendering all your AWS access to them. They can access your AWS API key and do malicious stuff. 

## What should we do?
We should use [[AWS CLI & IAM#IAM Roles for Services|IAM Roles]] to access features without surrendering any information. Recall that IAM roles allows services to assume certain roles and perms attached to said role to do tasks. 

Make a role that allows ReadOnly access. Go to EC2 Instances -> Click on desired instance -> Actions -> Modify IAM Role. Then add the role you just made.

Double check in the instance's security tab if it contains the role we made. If yes, your SSH should work now.