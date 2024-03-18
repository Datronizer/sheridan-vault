# Security Group
A security group is basically a firewall, but a [[Stateful & Stateless Firewall#Stateful firewall|stateful]] one. Security groups are applied **to instances** (in contrast to [[NACL]] who applies it to the subnet.

A typical use case is to control the access to a group (duh, the name) of instances with common factors. 

Everything in AWS is an instance. It can be a massive VPC or a teeny tiny wittle container, these are all instances.
