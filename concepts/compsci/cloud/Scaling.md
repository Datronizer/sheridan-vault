# Introduction
Scaling is an important topic in cloud (as well as anything corporation related). As your product becomes more popular, more things will need to be done to expand the capacity of your services. Often times this means upscaling infrastructure. But, how do we do that?
# Vertical scaling
Used for applications that need a lot of bandwidth. 
- **Scaling up** means adding more capacity to an existing resource. That or changing the instance type, exmaple: changing a server from **T**iny size to e**X**tra size.
- **Scaling down**: the reverse lol. Dropping capacity due to excess storage for example.
# Horizontal scaling
Web servers will use horizontal scaling because they don't need bandwidth, they need instances instead. Think microservices. You don't need a "bigger" CPU, you just need more instances to independently process requests.

An example of this would be an [[Airport Metaphor|airline]]. More flyers means the airline must upscale to provide these services right? But do we *always* have to upgrade the whole fleet to accommodate more flyers? Like if we have more than 300 flyers, do we *need* a bigger plane? Or can we just buy another smaller plane for much cheaper?

AWS can usually do auto-scaling for your use case. They don't automatically vertically scale your server though. That has to be done manually, because, you know, it requires physical hardware??