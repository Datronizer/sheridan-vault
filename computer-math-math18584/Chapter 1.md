Most numbers we use in daily life are formed from 10 numbers: 0, 1, 2,...,9. And we would arrange these numbers in a system called [[Decimal numbers]].  Deci- being 10, -mal being system => Base 10 system.

Each of these individual numbers are called [[digits]] and these digits make up bigger and more complex numbers by taking up [[placevalues]].

In a decimal system, the placevalues are 10, 100, 1000, etc.

Yet, computers only understand [[Chapter 1#Binary|the binary system]], 0's and 1's. That is because unlike us, they communicate using "on" and "off", switches of electricity through semiconductors to communicate numbers. In a binary system, their placevalues are instead 2, 4, 8, 16, equivalent to 2^1, 2^2, 2^3,...

Each of these digits are called "**Bi**nary dig**its**" => hence, "**bits**"
# Placevalues
Placevalues are powers of a system of which a digit can multiply with in order to occupy a *place* in a number. 

Common placevalues in number systems:
- Binary: 2^0, 2^1, 2^2, 2^3 = 1, 2, 4, 8, etc.
- Decimal: 10^0, 10^1, 10^2, 10^3 = 10, 100, 1000, 10000, etc.
- Hexadecimal: 16^0, 16^1, 16^2,... = 1, 16, 256, etc.

# Counting numbers
We often count numbers, but we never really stopped to consider why we do certain things. Here's a thought problem. Try counting decimal numbers!

Decimal numbers start off easy, you start from 0, 1, 2,..., to 9. But when you hit 9, the ones placevalue cannot go any higher, so 9 resets to 0, and 1 is added to the tens column.

As you hit 19, this occurs again. 9 loops back to 0, and 1 gets added to the tens place and 1+1=2. So this becomes 20.

Keep doing this until you hit 99, and this happens again to replace the 1st 9 with a 0, add 1 to the tens column so 9 + 1 => 9 becomes 0 and 1 carries over to the hundreds column => 100.

We see that as we count, this often occurs whenever we hit a "limit" of how much a column can take and it "overflows" back to 0, and we carry the "overflow" (which is usually +1) to the column to the left. This is really easy to see in binary numbers.

Start with 0 -> 1. Now add 1 to 1. The limit is 1 so 1 + 1 = 0, carry 1 over to the left => 1 + 1 = 10.
Do this again. 10 + 1 = 11 => 11 + 1 = 12. 2 is an overflow of 0, 1 so 2 becomes 0, carry one over. 12 becomes 20. 2 becomes 0 again, carry 1 over. 20 = 100. 

> [!important] Keep in mind these are **binary** not **decimals**. The numbers are only representative and they DO NOT mean the same thing they mean in decimal values.

Same things with hexadecimals btw, but I'm too lazy to write them all out. Refer to <a href="https://www.tutorialspoint.com/computer_logical_organization/hexadecimal_arithmetic.htm">this link</a>.

We see that as we hit the limit of a column, the max permutations within that limit is always the same as the power of the [[#Placevalues|placevalue]] of the limit you're trying to reach.

# Number conversions
## Convert to Decimal
For the sake of clarity, we can use the **expanded notation** to convert numbers to different systems. Convert each digit of other system into the equivalent in decimal and use the relavant power.

Example: 
- 123dec =  1 * 10^2 + 2 * 10^1 + 3 * 10^0 = 100 + 20 + 3
- 11001bin = 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0 = 16 + 8 + 0 + 0 + 1 = 25
- 3AChex = 256 * 3 +16 * 10 + 12 * 1 = 940
- 1Fhex = 16 * 1 + 1 * 15 = 31
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
Example:
> 47dec to binary
> 47 
> = 32 + 15 
> = 32 + 8 + 7 
> = 32 + 8 + 4 + 3 
> = 32 + 8 + 4 + 2 + 1 
> = 2^6 + 0 + 2^4 + 2^2 + 2^1 + 2^0
> = 101111 (16 missing so it's 0)
> This works better if you draw this out.

