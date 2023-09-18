#lecture
Most numbers we use in daily life are formed from 10 numbers: 0, 1, 2,...,9. And we would arrange these numbers in a system called [[Decimals]].  Deci- being 10, -mal being system => Base 10 system.

Each of these individual numbers are called [[#Digits|digits]] and these digits make up bigger and more complex numbers by taking up [[#Placevalues|placevalues]].

In a decimal system, the placevalues are 10, 100, 1000, etc.

Yet, computers only understand [[Binary|the binary system]], 0's and 1's. That is because unlike us, they communicate using "on" and "off", switches of electricity through semiconductors to communicate numbers. In a binary system, their placevalues are instead 2, 4, 8, 16, equivalent to 2^1, 2^2, 2^3,...

Each of these digits are called "**Bi**nary dig**its**" => hence, "**bits**"
# Number systems
## Decimal
## Binary

# Digits
# Placevalues
Placevalues are powers of a system of which a digit can multiply with in order to occupy a *place* in a number. 

Common placevalues in number systems:
- Binary: $$2^0, 2^1, 2^2, 2^3,... = 1, 2, 4, 8,... $$
- Decimal: $$10^0, 10^1, 10^2, 10^3,... = 10, 100, 1000, 10000,...$$
- Hexadecimal: $$16^0, 16^1, 16^2,... = 1, 16, 256,...$$
# Counting numbers
We often count numbers, but we never really stopped to consider why we do certain things. Here's a thought problem. Try counting decimal numbers!

Decimal numbers start off easy, you start from 0, 1, 2,..., to 9. But when you hit 9, the ones placevalue cannot go any higher, so 9 resets to 0, and 1 is added to the tens column.

As you hit 19, this occurs again. 9 loops back to 0, and 1 gets added to the tens place and 1+1=2. So this becomes 20.

Keep doing this until you hit 99, and this happens again to replace the 1st 9 with a 0, add 1 to the tens column so 9 + 1 => 9 becomes 0 and 1 carries over to the hundreds column => 100.

We see that as we count, this often occurs whenever we hit a "limit" of how much a column can take and it "overflows" back to 0, and we carry the "overflow" (which is usually +1) to the column to the left. This is really easy to see in binary numbers.

Start with 0 -> 1. Now add 1 to 1. The limit is 1 so 1 + 1 = 0, carry 1 over to the left => 1 + 1 = 10.
Do this again. 10 + 1 = 11 => 11 + 1 = 12. 2 is an overflow of 0, 1 so 2 becomes 0, carry one over. 12 becomes 20. 2 becomes 0 again, carry 1 over. 20 = 100. 

> [!important] Keep in mind these are **binary** not **decimals**. The numbers are only representative and they DO NOT mean the same thing they mean in decimal values.

Same things with hexadecimals btw, but I'm too lazy to write them all out. Refer to [this link](https://www.tutorialspoint.com/computer_logical_organization/hexadecimal_arithmetic.htm).

We see that as we hit the limit of a column, the max permutations within that limit is always the same as the power of the [[#Placevalues|placevalue]] of the limit you're trying to reach.
# Number conversions
## Convert to Decimal
For the sake of clarity, we can use the **expanded notation** to convert numbers to different systems. Convert each digit of other system into the equivalent in decimal and use the relavant power.

Example: 
$$123dec =  1 * 10^2 + 2 * 10^1 + 3 * 10^0 = 100 + 20 + 3$$
$$11001bin = 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0 = 16 + 8 + 0 + 0 + 1 = 25$$$$3AChex = 256 * 3 +16 * 10 + 12 * 1 = 940$$$$1Fhex = 16 * 1 + 1 * 15 = 31$$
## Decimal to Binary
Use the remainder method. Example:
> What is 252dec = ???bin
> 
> Start by dividing 252 by 2 to get a quotient of 126, 0 remainder.
> Repeat to get 63R0
> 31R1.
> 
> Now that we have R1, we have a remainder. Take 1 of 31 and keep dividing.
> We get 15R1 -> 7R1 -> 3R1 -> 1R1 -> 0R1
> 
> Now look at all the remainders, sort them backwards. So if we got 00111111, it is now 11111100.

Another example:
> 152 -> 76R0 -> 38R0 -> 19R0 -> 9R1 -> 4R1 -> 2R0 -> 1R0 -> 0R1
> Write that backwards to get 10011000

Another method is the **place method**
Example, to convert 47dec to binary:
$$
\begin{aligned}
47 &= 32 + 15 \\ 
&= 32 + 16*0 + 8 + 7 \\
&= 32 + 16*0 + 8 + 4 + 3 \\
&= 32 + 16*0 + 8 + 4 + 2 + 1 \\
&= 2^6 + 2^5*0 + 2^4 + 2^2 + 2^1 + 2^0 \\
&= 101111 \text{(16 missing so it's 0)} \\
\end{aligned}
$$
This works better if you draw this out.
## Decimal to Hexadecimal
Use the remainder method also. Example:
> What is 555dec = ???hex
> 
> Start by dividing 555 by 16 to get 34R11.
> Repeat to get 2R2
> We have 2 / 16 which is 0R2 
> 
> Now look at all the remainders, sort them backwards. So if we got 11-2-2, it is now 2-2-11 = 22B.

## Binary to Hexadecimal
In the binary system, the number 16 can be represented with 4 bits. In other words, every 4 bits can be converted to 1 hexit. Using this property, we can convert binary to hexadecimal using the following method.

There are 3 steps:
1. Start with the right-most (least significant) bit and group into sets of four bits.
2. If the last group has less than 4 bits, pad to the left with zeros until the group has four bits.
3. Convert each groups of 4 bits to its hex equivalent.

Example:
> 1011001000011111011bin = ???hex
> ***0***101 1001 0000 1111 1011 (group into sets of 4 bits + padding)
>    5       9       0       F       B
> 590FB is my new number

## Hexadecimal to Binary
This is simpler than the other way around. All you need to do is write the 4bit equivalent for each hexit e.g. 14hex = 1110bin

Example:
> (A1E7)hex = ???bin
>    A     1        E       7
>   10     1       14      7
> 1010 0001 1110 0111
> This is my new number ^^^

