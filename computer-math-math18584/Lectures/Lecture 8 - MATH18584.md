I missed last lecture, go write that down
# Modulus
Suppose I have a clock. Lets say I want to add 24 hours to this clock. Since the clock has only 12 numbers, it would make sense that the needle would travel all 12 hours, loop back to 0 or 12, then goes another 12 hours to loop back to 0 or 12. 

What happens now if I add 27 hours? Following the previous logic, we would loop twice over 12 and go 3 steps to 3 o'clock. Do you see how all the values that are divisible by 12 got overlapped and are gone, leaving only the remainder behind?

This is called the **modulus**. Refer to [[Modulo]] for extra information and abstract explanation.

Notation is simple, you can treat it like an operator:
$$
3496\space mod \space 25 = 21
$$
And we refer to the set of numbers that are modulus of $m$ as $\mathbb{Z}_{m}$ where $\mathbb{Z}_{m} = \{0, 1, 2,...,m-1\}$.



