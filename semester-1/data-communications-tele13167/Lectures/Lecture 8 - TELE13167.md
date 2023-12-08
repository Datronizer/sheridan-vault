# IEEE 802.11

## Basic Service Set (Home Network)
Ad hoc network: You don't need a router to connect 2 computers within the same area. Share data without router.

Access point: Connects wired and wireless connections. Basically: Computer => through wireless => Router => through wired => To Internet.

Infrastructure mode: Lets wireless networks connect to the Internet.
## Extended Service Set
Imagine Oakville vs Brampton campus. Okay cool, these two use the same network. That's Extended Service Set.
## Issues Impacting Wireless Signals
1. Attenuation
2. Mobility
3. Reach
4. Collision Avoidance
5. Multipath Interference
## CSMA/CD (cont'd)
This doesn't work with Wi-fi. Assume I have a computer A,B,C. B and C are outside each other's range. A in the middle of both. Okay, how will CSMA/CD work? It can't tell everyone to pause bc it doesn't even see all devices at once.

### RTS/CTS/ACK:
Request to send (RTS): 1011
Clear to send (CTS): 1100
Acknowledgement (ACK): 1101

A RTS B
B CTS A
A sends
B ACK A.
:thumbsup:


