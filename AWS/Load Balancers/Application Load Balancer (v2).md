---
aliases:
  - ALB
  - AWS ALB
  - Amazon ALB
---
Application Load Balancers (ALB) is [[Layer 7]] (HTTP only) and they load balance:
- multiple HTTP apps across machines (target groups).
- multiple apps on the same machine (containers)

ALBs support HTTP/2 and WebSocket, and they support redirects (from HTTP to HTTPS for example).

Routing tables to different target groups:
- Routing based on path in URL (`example.com/users` & `example.com/posts`)
- Routing based on hostname in URL (`one.example.com` & `other.example.com`)
- Routing based on Query String, Headers (`example.com/users?id=123&order=false`)

ALBs are great for microservices & container-based applications (e.g. Docker & Amazon ECS). 
- Because it has a port mapping feature, it can redirect to a dynamic port in ECS.
- In comparison, we'd need multiple CLBs per application.

# Target groups
There are certain things you can group together into **target groups** for ALB to route to.
- ECS instances (can be managed by an ASG) - HTTP
- ECS tasks (managed by ECS itself) - HTTP
- Lambda functions  - HTTP requests is translated into a JSON event
- IP addresses - must be private

ALB can route to multiple TGs and health checks are at the TG level.
# Good-to-knows
- You have a fixed hostname (`xxx.region.elb.amazonaws.com`)
- Application servers don't see the IP of the client directly
	- The true IP of the client is inserted in the header `X-Forwarded-For`
	- We can also get port (`X-Forwarded-Port`) and protocol use (`X-Forwarded-Proto`)

![[Pasted image 20250917200522.png]]

