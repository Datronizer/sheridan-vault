So we've kind of figured out how Subnet IDs work. But what we're doing is what a human would be doing. How would a machine do it?
# ANDing
ANDing is exactly what it sounds like. Yessir, we perform an [[Boolean Algebra#Boolean Operators|AND operation]] on an IP address using the Subnet Mask => new IP address. Provided is a simple table demonstrating how.

| IP     | 179 | 34  | 89  | 127 |
| ------ | --- | --- | --- | --- |
| SM     | 255 | 255 | 252 | 0   |
| Answer | 179 | 34  | x   | 0   |

We compute the easiest ones first: 255 is all 1s in [[Binary]] and 0 is all 0s. So ANDing/multiplying them should yield itself or zero. The x right there can be computed using the table method to get the binary value => decimal. Here's how:
1. Find block size.
2. Divide IP with block size using the [[method]] to get the right binary expansion.
3. Convert binary expansion back to decimals.

There is a way faster method:
1. Find block size
2. Divide IP by Block size
3. Take only the whole part of the answer
4. Multiply that by the block size
# TCP
- Reliable
- 3-way handshake
- Has a field for checksum
- Has a field for sequence and acknowledgement numbers
# UDP
- Fast, like zooooom
- Has a field for checksum
- Used when listening to a song on spotify

TCPs and UDPs have headers (duh). In TCPs, headers contain port numbers, sequence number, acknowledgement numbers, checksum, and padding if needed. 
UDPs only have port numbers and checksums.

- Port Number: Both TCP and UDP still want the right program.
- Checksum: TCP will resend if it's wrong, UDP discards.
- Sequenece Number: TCP wants to make sure the message arrives in the correct order, UDP does not care.
- ACK number: TCP wants to make sure that everything that is sent is received.
- SYN number:
# Three-way Handshake
Imagine your computer and server talking. Suppose all the numbers being sent are random unless specified. There are 3 steps:
1. Computer goes "Hey can I talk to you?" 
	- Flag: Synchronize (SYN)
	- Sequence #: 20
1. The server goes "Hm? Yes. Can I talk to you?" 
	- Flag: Synchronize (ACK, SYN)
	- Sequence #: 151 =>
	- Acknowledgement: #21
1. The computer then goes "Hm? Yes."
	- Flag: Synchronize (ACK)
	- Sequence #: 21 (random sequential number of 20.)
	- Acknowledgement number: 152

Imagine your computer and server ending the talk. Suppose all the numbers being sent are random unless specified. There are 3 steps:
1. Computer goes "Hey can I talk to you?" 
	- Flag: Synchronize (FIN)
	- Sequence #:  = X
1. The server goes "Hm? Yes. Can I talk to you?" 
	- Flag: Synchronize (ACK, FIN)
	- Sequence #: 151 =>
	- Acknowledgement: \x
1. The computer then goes "Hm? Yes."
	- Flag: (ACK) -
	- Sequence #: 21 (random sequential number of 20.)
	- Acknowledgement number: x + 1