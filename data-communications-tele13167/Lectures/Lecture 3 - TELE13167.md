Last week was quiz week - no lectures
# Hubs
## Thought problem
A wants to send a message to B in a system where A, B, C, D are hooked up to a hub. The message goes from A to the Hub. The Hub would relay to B right? **WRONG**. It goes to all B, C, D. C and D will see this and go "I have no idea what this is, I'm scrapping it." So at the end, only B really receives it.

Simple diagram: 
- D --> Hub
- Hub --> A, B, C
- A, C discards
## How it works
A hub is very unsecured.
A hub is transmits its message to all devices connected to it. It's up to the device to determine if the message is right.
# Transparent Bridges
## Thought problem
A wants to send a message to B in a system where A and B are connected through a hub, C and D are connected through another hub, these 2 hubs are hooked up to a bridge. The message goes from A to the Hub. The Hub would relay to B and the Bridge.

The bridge "learns" that A is on the left side (this is important) and forwards it to the next Hub to C, D who will discard it. Now suppose B sends a message to A. It goes through Hub 1, to bridge. Now the bridge will see that "oh! B is also on the left. I'll just not send this on because y'all are on the same side." So the message is discarded before it reaches Hub 2.

**Diagram:** 
A --> B
- A --> Hub 1
- Hub 1 --> Bridge, B
- Bridge adds A's MAC address (on the left)
- Bridge --> Hub 2
- Hub 2 --> C, D
- C, D discards, B receives message.

B --> A
- B --> Hub 1
- Hub 1 --> Bridge, B
- Bridge adds B's MAC address (on the left)
- Bridge discards
## How it works
The bridge has a table of what we will call "left" and "right". Every time a device sends a message to another device, it "learns" where this message is from and which side this device is on (it adds the device to the table). Then it forwards the message to the other side given that the destination is not already learned beforehand.

The more messages sent between the devices, the more table will be filled and we will have more optimized message forwarding. Traditional bridges are 2-way, there also exist 4-way and 8-way bridges but the switch swiftly took over.
# Switches
## Thought problem
A wants to send a message to B in a system where A, B, C, D are hooked up to a switch (deja vu eh?). The message goes from A to the Switch.

At this stage, a Hub would send the message to everyone, so will the Switch. The Switch, however, will learn where A is (which port A is connected to). Now if B sends to A, the Switch will already know where A is and will forward it directly to A. Switch learns based on inputs, rather than on left/right.

Simple diagram: 
- A --> Switch
- Switch adds A's MAC to table.
- Switch --> B, C, D
- B, C, D discards

Afterwards, if C --> A:
- C --> Switch
- Switch --> A
## How it works
A Switch is practically a Hub but it can learn so it can directly forward messages to the right address. 
# Routers
## How it works
Every device connected to a router has a unique IP address, thus using IP addresses, a router knows about ALL of the devices **directly connected to** it. Then how does it know where the other computers are.
## Thought problem
R1 - A, B
R2 - C, D, E

R2 **does not recognize** A, B, but it is connected to R1 which does. If we want to have it recognize, we use a **routing protocol** so that R2 learns about R1.

R2 will go through the interface of R1. R2 will be like "Hey, uh, you know a computer with this IP?" and R1 will be like "Oh ya, it's connected to me, go through interface m2."
## Routing protocol
### Static routing (0.0.0.0/0)
Sends all traffic in 1 direction. 

**Example:** 
m0 | Sheridan's router | m1
m0 here is the "in" interface for Sheridan's router, m1 is the "out" interface. Everything gets sent to the router through m0, then the router will forward this traffic to the appropriate device, else it sends it to a "catch-all" default routing.

**Human example:**
I want to send a message to 150.23.14.1. I send the message through to the router and say "Hey, uh you have anyone here with this address?" The router will check if this address is connected here and it goes "oh sorry eh, I don't see him. You know what? Let me forward this to my buddy. Hey 0.0.0.0/0 (static routing)! Got a message for ya!". This message goes to that router and it continues. Then it continues and continues until it reaches the server. This is near instant since our technology is insane.

# Signals
We've learned how data is transferred, but what does this look like physically? Enter, **signals**. There are 2 types: analog and digital. Typically our power supply is analog, but computers don't read analog (neither do zoomers), so all this signal goes through a **modem/DSL** to convert back to digital, then computers can read.

Usually they could do this in 2 ways. If it reads a lack of signal in 1 signal element => 0, else 1. Or if the signal is lower than a set frequency => 0, else 1. This "reading"/"broadcasting" speed is call "bit rate" (yes fellow streamers).
## Properties
### Attenuation
Simply put: as you go further away, the signal gets weaker.
### Amplifiers
Amplifies the signal, but if the signal is noisy, it also amplifies a noise.
### Repeaters
Amplifies the signal and corrects the noise, but distance is an issue (digital signals don't travel too far).
## Signal transfer properties
### Latency
The amount of time it takes for all the data of 1 packet to be transfered. Higher latency => laggy internet, delayed data transfer, rage mode.
### Throughput
How fast can I send data at once. Measured in Mbps. Higher throughput means higher data transfer speeds. Treat this as the water being poured. More throughput, more water being put through, may be limited by the bandwidth.
### Bandwidth
How much data can be handled at one time. Higher bandwidth means I can receive more data at the same time. Treat this as a pipe's width. More width, more water at one time.
### Jitter
Jitter is a variation in latency. In packet-switched networks, each packet travels independently. If one comes early and one comes late, the data will be mismatched and the computer rejects the one that comes early because it's waiting for the late one (which is supposed to be there first) => robot voice moment.
## Different ways to transfer signal
### Twisted Pair
Power being transmitted also creates electromagnetic waves, these waves interfere with signals (it "pushes the noise up") and causes noise to be amplified along the telephone/internet wire and you can't hear a damn thing at the end because there's so much noise.

But if you twist your wires, the "up" becomes a "down" and cancels each other out => no noise. Con: it's expensive, that's double the amount of wires.
### Coaxial cables
When a signal hits a Faraday Cage, it disperses the signal (only if the signal is high frequency). Using this property, we can create a coxial cable (braided shielding) for the wire which will destroy all outside noise. Con: even more expensive.
### Fiber Optic
Fast. Really fast. Literally speed of light. Works by bouncing light along a glass tube which carries information all the way to the end. Con: holy shit this is expensive, also really hard to repair.

