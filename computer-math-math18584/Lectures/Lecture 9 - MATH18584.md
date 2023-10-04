# Solving linear equations

# Solving modulus equations
## Single modulus equation
Suppose I have $x \space mod \space 3 = 2$. What would be the answer? Clearly 5 is the answer right? Because $5/3=1R2$. However, let's think about this. Does 8 also work? Yes right? 11? 14? 17? etc. What about 2? 2/3 = 0R2, so that works also!

Then, to accurately state all the solutions of a modulus equation, we should find the remainder and add the quotient over and over to get a sequence of solutions to a modulus equation.

A simple representation of all single modulus equations of the type $x \space mod \space k = y$ is the sequence $y + kn$ for all $n \in \mathbb{N}$
## Set of modulus equations
Suppose I have $x \space mod \space 3 = 2$ and $x \space mod \space 4 = 1$. How will I get the sequence of all solutions for this set? Well, let's start simple and find the first sequence:
$$x \space mod \space 3 = 2 \therefore x = \{2, 5, 8, 11, 14, 17, 20, 23,etc.\}$$
The second sequence:
$$x \space mod \space 4 = 1 \therefore x = \{1, 5, 9, 13, 17, 21, 25, 29,etc.\}$$
We see that there are some overlaps between these 2 solution sets at $5, 17, 29, etc.$ These are actually the solutions for our set of equations. In fact, if we multiply 3 and 4 together we get 12, which is the coefficient $k$ we are looking for. The first common solution here would be the remainder $y$. 

Thus we have our equation.