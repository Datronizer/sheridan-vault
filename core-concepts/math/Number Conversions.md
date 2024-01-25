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