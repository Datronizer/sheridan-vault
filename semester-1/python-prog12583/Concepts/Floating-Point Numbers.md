Alright Einstein, guess why $12.778$ is a floating point number.

You guessed it! It's because the radix point "floats"! Let's talk about that.

We start with a question: how do we denote real numbers in computer language? One way is to return all these numbers to a common form. Take $3.14$ for example. How do we notate this in [[memory & compiler maps]]?

We can do what is colloquially known as "numeric gymnastics", specifically, we convert the decimal number into [[Scientific Notation]], then store its constituents in memory maps.
## Storage
Let's say we want to store Pi. Pi is $3.14$ and $3.14 * 10^2 = 314\equiv 314 * 10^-2 = 3.14$.

Let's take the whole part (mantissa) which is equal to $314$, and take the exponent, which is $-2$. Now store these two in a memory map. 

In class, we just store them as just stars because they're basically placeholders for the actual value. In real life, it's the above information with the mantissa and exponent.
## Encoding
Okay now let's pull this funny number and represent it. How do we do that?

Before we do anything, let's first get this out of the way. Let me make it a colored block of text too so it's crystal clear.

> [!important] Not all floats are stored and processed the same way. 
> This part only covers base-2 floats. Irrational numbers will not be discussed as they're special cases, and they're automatically handled by IEEE 745 encoding.

In general, a floating-point number is stored as such (numbering is done left to right):
- Bit 0: signed bit
- Bit 1-9: exponent bits (8 bits long)
- Bit 10-32: fraction bits (23 bits long)

The encoding is done as such: 
$$
(-1)^{bit0} \times 2^{exponentInDecimal} \times (1.fractionInDecimal)
$$
## IEEE 745
In computers, we use what is called **encoding IEEE 745** to encode data into bytes and send them to the memory for storage. We don't really need to know how it works, just consider it a "black box operation" that magically stacks your stuff neatly into the memory.

Unfortunately, since our number can only be stored in 4 bytes, chances are information will be lost upon encoding and decoding since the number would be chopped off. So, uh... yeah. **DON'T TEST FOR EQUALITY FOR FLOATING POINT NUMBERS WITHOUT AN ADDITIONAL ALGORITHM**.

**IEEE 745** is generally really good at storing data into the memory, but it is terrible at computation. this is when we rely on something called the [[#Math coprocessor]].