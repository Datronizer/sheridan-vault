---
aliases:
  - SSL
  - SSL/TLS
  - Secure Sockets Layer
  - TLS
---
# Basics
An SSL Certificate allows traffic between your clients and your LB to be encrypted in transit (in-flight encryption)

SSL is short for Secure Sockets Layer, which is used to encrypt connections.
TLS is short for Transport Layer Security, which is a newer SSL.

Nowadays, TLS certificates are mainly used, but people still call it SSL, but it's TLS.

Public SSL certificates are used by Certificate Authorities (CA) e.g. Comodo, Symantec, GoDaddy, GlobalSign, Digicert, etc.

Using the SSL certificate, we can encrypt our connections between our clients and LBs.

SSL certs have an expiration date (set by you) and must be renewed regularly to ensure they're authentic.
# In terms of LBs
This diagram shows how it works behind the scenes

![[Pasted image 20250921021216.png]]

Notice that the traffic between LB and EC2 instance can be done with HTTP (unsecured), but is still safe as it is conducted over a private VPC.

Some important info:
- The LB uses an X.509 certificate (SSL/TLS server certificate)
- You can manage certs using ACM ([[AWS Certificate Manager]])
- You can create/upload your own certs alternatively
- HTTPS listener:
	- You must specify a default cert
	- You can add an optional list of certs to support multiple domains
	- Clients can use SNI (Server Name Indication) to specify the hostname they reach.
	- Ability to specify a security policy to support older version of SSL/TLS (legacy clients)

# Server Name Indication (SNI)
How do you load multiple SSL certificates onto 1 web server (EC2 instance) to serve mulitple websites?

Well, you can use SNI, because that's exactly what it does.

SNI is a "newer" protocol, and it requires the client tCloudFronto indicate the hostname of the target server in the initial SSL handshake. The server will find the correct cert or retruns the default one.

![[Pasted image 20250921021932.png]]

> [!note]
> Only works for [[ALB]] & [[NLB]] (newer generation) & [[CloudFront]]. Does NOT work for CLB.

# Relation to [[ELBs]]
- CLBs (v1)
	- Support only 1 SSL cert
	- Must use multiple CLB for multiple hostname with multiple SSL certs
- [[ALB]] (v2)
	- Supports multiple listeners with multiple SSL certs
	- Uses SNI to make it work
- [[NLB]] (v2)
	- Supports multiple listeners with multiple SSL certs
	- Uses SNI to make it work