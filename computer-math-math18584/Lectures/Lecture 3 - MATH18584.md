# The Sign Bit
Since binary only run on 0s and 1s, how do we denote that a number is a positive or negative? Computer scientists have the answer to this: take the most significant bit and use that to denote whether a negative sign is present!

But how do we know if a number is an **unsigned** [[Binary|binary]] number, aka we do normal operations on it, or a **signed** number, one that takes the most significant digit and turn it negative?

To know whether a number is signed, we need to declare that it is signed, that's the only way to know. That or see what the professor chooses. Generally it's safer to assume the number is unsigned unless otherwise specified.

Let's do some conversion examples with signed binary:
- $1011bin= -8 + 0 + 2 + 1 = -5$ (signed)
- $1011bin= 8 + 0 + 2 + 1 = 11$ (unsigned)
	- We see that the most significant bit is converted to a negative equivalent and we sum them up like normal to get the decimal conversion
- $01110bin = 0 + 8 + 4 + 2 + 0 = 14$
	- If the most significant bit is a 0 => that's a positive number. 
- $11010bin = -16 + 8 + 0 + 2 + 0 = -6$
- $001111bin = 0 + 0 + 8 + 4 + 2 + 1 = 15$

There is an interesting situation happening if we duplicate the most significant bit for signed numbers. Suppose I have $1011bin$. If I add 1 to the front to get $11011bin$, the value doesn't really change. "What? That doesn't make sense". But it does, let me show you:
- $1011bin = -8 + 0 + 2 + 1 = -5$
- $11011bin = -16 + 8 + 0 + 2 + 1 = -8 + 2 + 1 = -5$
- $111011bin = -32 + 16 + 8 + 0 + 2 + 1 = -16 + 8 + 0 + 2 + 1 = -5$

That's weird isn't it! But it makes total sense when you think about it. Same applies for positive numbers so I won't rewrite them here.
## Bit Field Length
Thought problem: add +16 and +7
We have:
$$
\begin{align}
0\space10000\\
+\space0\space00111\\
---\\
0\space10111
\end{align}
$$
As you can see, we first write out the signed bit and the powers of 2 until we end up with a power large enough to express our number. If there isn't enough, we duplicate it. Now try this:
$$
\begin{align}
0\space10000\\
+\space0\space10000\\
---\\
1\space00000
\end{align}
$$
Hmm that's not right. +16 add +16 should make +32, but instead we got -32. This is called an **overflow**. Because the extra bit gotten from the sum flows over to the signed bit. This is a cool segue into-
## Overflow
$$
\begin{align}
0\space10111\\
+\space0\space10101\\
---\\
1\space01100
\end{align}
$$This is also an overflow. But what happens when we add 2 negative numbers?
$$
\begin{align}
1\space10111\\
+\space1\space00101\\
---\\
\cancel{1}0\space01100
\end{align}
$$
The extra bit is culled so we have a 0 as the most significant bit => Now it's positive so it's another overflow case.

What if we add a positive and a negative number? Well, in theory that's basically a subtraction! So it can happen, see here:
$$
\begin{align}
1\space1000\\
+\space0\space1101\\
---\\
\cancel{1}0\space0110
\end{align}
$$
We take out the extra bit (there's only 1 signed bit, discard the rest) and we get +6 as the answer, which is correct!! 

## Bit Field Extension
The greatest possible signed 4bit number is 0111, while the smallest possible 4bit number is in fact 1000. These are 7 and -8 respectively. So, how do I write a +8? I would have to pad a 0 to 1000 to turn -7 to a +8, thus making a 5bit number 01000. 

Okay, what if I hit 15 and I want 16? I have 0 1111. So to accommodate 16--a typical 5-bit number--we need to pad another 0 to make 0 10000 to make a 6-bit number that can accommodate a 16.

As we can see, this is a solution to our overflow issue in the +16 add +16 problem! We can pad an extra 0 in each +16 to get 
$$
\begin{align}
0\space010000\\
+\space0\space010000\\
-----\\
1\space100000
\end{align}
$$
And we fixed the overflow issue!! Now, let's try with negative numbers:
$$
\begin{align}
11\space1011\\
+\space11\space0101\\
-----\\
1110000
\end{align}
$$
Whenever we see signed numbers, it's usually a safe bet to duplicate the most significant bit and do the operation, just in case. We'll discard the extra bits anyways so we have nothing to worry about.
## One's Complement
Finding the one's complement of a signed binary number is quite simple. Just take a number and flip all the bits.
- $101110bin => 010001bin$
- $011101bin => 100010bin$
- $101000011bin => 010111100bin$
It's called a 1's complement because...
## Ten's Complement
It's easier to look at this in a comparative sense so here's a fancy table

Number | 10's complement | 9's complement
-- | -- | --
3 | 7 | 6
4 | 6 | 5
8 | 2 | 1

An $\text{x's complement}$ is the number you need to make a number $y$ reach $x$ such that $y + k = x$ for some $k$.
## Two's Complement
As you can see from the above example, the difference between 2 complements is the difference between their values. So to get a two's complement, you add 1 to a one's complement:
- $101110bin => 010001bin => 0100010bin$
- $011101bin => 100010bin => 100011bin$
- $101000011bin => 010111100bin => 010111101bin$

Converting something from a normal binary number to a two's complement is simple. You find its one's complement then add 1.
- $0011100 => 1100011 => 1100100$

Okay so why do we need this? Good question, check this out: 
$$ 
\begin{align}
+3dec &= 0011bin\\ 
&= 1100bin \space\text{(1's complement)}\\
&= 1101bin \space\text{(2's complement)}\\
&= -3dec
\end{align}
$$
Oh hohohoho. We found the negative equivalent of the number we started with! Pretty cool huh? But now (insert bit field length illustration), think closely about why we need to add 1 to get the mirror negative number. Hint, it has something to do with an extra number that is both negative and positive. Illustration for reference.

Practice:
3 - 4 = 3 + (-4)
$$
\begin{align}
0\space011& (3)\\
-\space0\space100& (-4)\\
-----\\
1\space011&(1's)\\
1\space100&(2's)\\
-----\\
0\space011& (3)\\
+\space1\space100&(2's)\\
-----\\
1\space111&(-1)
\end{align}
$$
