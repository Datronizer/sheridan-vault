# Identity & Access Management (IAM)
## Introduction
IAM is a global service as we have discussed in the [[AWS Cloud|previous chapter]]. When we create an AWS account, we made a root account. The root user for all your AWS usage is created by default, and shouldn't be used or shared (duh).

> You should only use the root account to make 1 single account for your AWS usage, and then never touch it again. It's unsafe to let someone else play around with your AWS account, especially when they can create a thousand dollar burden for you to handle.

Moving on to some definitions:
## Users & Groups
A **User** is a person in your organization, and can be grouped. 
A **Group** contains users. A Group cannot contain other Groups.

> [!note] 
> A User does NOT have to belong to a group. A User can also belong in multiple groups.

> Example: A, B, C, D, E, F are all employees in your company, say Bucket Hat Studios. A, B, C are devs, E, F are sales, and D is just there. In our case, we can group A, B, C together into a Group called Developers; E, F into one called Sales. We have 2 groups now, plus D who is not in a group. 
> 
> Now, if we assume C and F are also auditors, we can add them to an Auditor group. At the end we'll have A,B,C in Dev; E,F in sales; D with no Groups; C and F in Auditor on top of their original groups.

## Policies
### Introduction
**Users** and **Groups** can be assigned JSON documents called *Policies.*

An example of such file is here:
![[Pasted image 20250427145034.png]]

We can see that for this JSON, there is an array of statements. For the first statment, for example, we **Allow** the user to use the **Describe** function in the **EC2 service**, and so on. 

These policies define the permissions of the users. It can prevent new users from bombing your cloud service with a bunch of services outside the scope of your budget. 

In AWS, you apply the **least privilege principle**: meaning you don't give more permissions than a user needs. Similar to Linux. This is also called the zero-trust policy.

> [!Hands-on] 
> There is a practice lab that entails the creation of an IAM user such that future use of your AWS account will not be done through `root` for safety. Please refer to video 12-13 on [Udemy](https://www.udemy.com/course/aws-certified-developer-associate-dva-c01/learn/lecture/26100730#overview).
### Policy Inheritance
Assume I have 3 people, A, B, C in a Dev [[#Users & Groups|Group]], and D, E in an Operations Group. If I provide a policy to the Dev Group, this policy will be **inherited** by all members of that Group. Same thing applies to the Operations Group.

Now, what if you have employee F, who does not belong to any group, but you still want to provide them with certain policies? You definitely can! A policy that is **provided directly** to the User is called an **Inline Policy**.

Now, what if C and D are in an Audit Team Group? In this case, whatever policy you assign to Audit Team will automatically by inherited by C and D, on top of the policies they already have.

You're probably wondering about the hierarchy of the policies? If a [[#Users & Groups|User]] has 2 policies from 2 different groups, what is the hierarchy for them to activate?
### IAM Policies Structure
Here is a sample:
![[Pasted image 20250427182224.png]]

This JSON consists of:
- `Version`: policy language version, always include "2012-10-17" (apparently this is like the go-to policy date, might change in the future, but for now, this works for all) (*REQUIRED*)
- `Id`: identifier for the policy (*optional*)
- `Statement`: nonempty array of individual statements (*REQUIRED*)

For `Statement`, each individual statement consists of:
- `Sid`: an identifier for the statement (*optional*)
- `Effect`: whether the statement allows/denies access (`"Allow" | "Deny"`)
- `Principal`: account/user/role to which this policy applies to
- `Action`: array of actions this policy allows or denies
- `Resource`: array of ARN the above action applies to
- `Condition`: conditions for when this policy is in effect (*optional*)
### Password Policy
In order to protect your [[#Users & Groups]] from being compromised. Certain security measures should be set up to prevent attacks. One of these ways is to define a Password Policy.

Obviously we know that stronger passwords = higher security. Thus in AWS, you can set up a password policy:
- Set minimum password length
- Require specific character types
	- uppercase
	- lowercase
	- numbers
	- non-alphanumeric characters
- Allow all IAM Users to change their own passwords
- Require users to change their password after some time (password expiration)
- Prevent password re-use
## Multi Factor Authentication - MFA
### Definition
Users have access to your account and can possibly change configs or delete resources in your AWS account. So yes, you WANT to protect your Root Accounts and IAM Users.

You can use MFA in this case, which can be understood as a combination of a password that *you* know + security device that *you own*. This guarantees that only the device owner can use the account. 

> [!important]
> If a password is stolen or hacked, the account is not compromised.
### MFA devices options in AWS
#### Virtual MFA Device
- Support for multiple tokens on a single device
	- Google Authenticator (phone only)
	- Authy (phone only)
#### Universal 2nd Factor (U2F) Security Key
A physical security key called a **YubiKey** by a 3rd party company called **Yubico**. This is a physical key that you can throw on your key fob. Supports multiple root and IAM users using a single security key.
#### Hardware Key Fob MFA Device
Example would be a key fob from an AWS partner like **Gemalto**.
#### Hardware Key Fob MFA Device for AWS GovCloud (US)
Same as previous, but is provided by **SurePassID**. This is just in case you're a US Gov employee who's utilizing AWS on top of government on-prem servers.

## IAM Roles for Services
Some AWS Services will need to perform actions on our behalf. To authorize this, we will assign **permissions** to AWS Services with **IAM Roles**.

Example:
We have an EC2 Instance that may want to do some actions on AWS. To let this EC2 do this, we provide it an IAM Role, and if the access roles are correct, it should be able to perform said task.

Common Roles:
- EC2 Instance Roles
- Lambda Function Roles
- Roles for CloudFormation

## IAM Security Tools
### IAM Credentials Report (Account-level)
This is a report that lists all your accounts' users and the status of their various credentials. This can be found in IAM -> Access reports (dropdown) -> Credential report.
### IAM Access Advisor (User-level)
UPDATE: This is now called Last Accessed. Different name, same functions.

Access Advisor shows the service perms granted to a user and when those **services were last accessed**. This can be found in Users -> Click on the user you want to see -> Last Access tab.

# AWS CLI
## Accessing AWS
There are 3 options:
- AWS Management Console (protected by password + MFA)
- AWS CLI: protected by access keys
- AWS SDK - for code: protected by access keys.

Okay so where do we get access keys? We can generate them through the AWS Console. [[#Users & Groups|Users]] manage their own access keys.

> [!warning]
> Access Keys are secret just like passwords. DO NOT SHARE THEM.

Once you have your Access Keys, you can use the Access Key ID and the corresponding Secret Access Key to use AWS through the Command Line Interface.
## AWS CLI
A tool that enables you to interact with AWS services using commands in your command-line shell. You get direct access to the public APIs of AWS services.

Use of AWS CLI is free and open source. You can get it at [https://github.com/aws/aws-cli](https://github.com/aws/aws-cli)

To aid you, you can develop scripts to manage your resources. 
## AWS SDK
Language specific APIs (libraries) that enable you to access and manage AWS services programmatically. It's embedded within your application and supports a wide variety of popular languages (SDKs, Mobile, IoT Devices SDKs).

For example: the AWS CLI itself is built on the AWS SDK for Python, and it is called [[boto]].
## AWS CloudShell
An alternative to a command line interface is the AWS CloudShell. Like the name suggests, it is a cloud shell that is built similar to AWS CLI. 

Files that are uploaded or created in CloudShell.

You can literally issue the same commands as AWS CLI, so I'll just ignore notes for this section since it's redundant.

# IAM Best Practices
- Don't use root account except for AWS account setup
- One physical user = One AWS [[#Users & Groups|user]]
- Assign users to [[#Users & Groups|groups]] and assign permissions to groups
- Create a strong password policy
- Use and **enforce the use** of MFA
- Create and use [[Roles]] for giving permissions to AWS services
- Use Access Keys for Programmatic Access (CLI/SDK)
- Audit permissions of your account using IAM Credentials Report & IAM Access Advisor
- **NEVER SHARE IAM USERS OR ACCESS KEYS**

# Shared Responsibility Model for IAM
For the AWS exam, they will ask about Shared Responsibility. Basically, you have to know what AWS is responsible for, and what you (the User) is responsible for.

| AWS                                      | You                                                       |
| ---------------------------------------- | --------------------------------------------------------- |
| Infrastructure (global network security) | Users, Groups, Roles, Policies, management and monitoring |
| Configuration & Vulnerability Analysis   | Enable MFA on all accounts                                |
| Compliance Validation                    | Rotate keys often                                         |
|                                          | Use IAM tools to apply appropriate permissions            |
|                                          | Analyze access patterns & review permissions              |
Simply put, AWS is only responsible for providing the infrastructure and the well-maintenance of it. YOU are responsible for whatever you're doing on their infrastructure