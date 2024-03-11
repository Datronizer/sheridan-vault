# Truth tables
## Generate truth tables from functions
As you know, we can deduct logic using [[concepts/math/Boolean Algebra|Boolean algebra]] and manipulate our variables using [[concepts/math/Boolean Algebra#Boolean Algebra Laws and Theorems|laws and theorems]]. Today we're talking about Truth Tables--a powerful tool that helps us extract logic values.

Consider this: let there be a function $F(x,y) = \sim x * y$. What are the boolean values? Of course one can simply sit and compute everything individually but there's a faster way. We can graph a table like so:

| x   | y   | NOT x | F   |
| --- | --- | ----- | --- |
| 0   | 0   | 1     | 0   |
| 0   | 1   | 1     | 1   |
| 1   | 0   | 0     | 0   |
| 1   | 1   | 0     | 0   |

Using this table, we can compute the logic from left to right, column by column. Doing this one by ones allows us to map out all possible values of x and y with respect to the F function. 

In details, we have the values of x, y and the value of NOT x graphed directly right of the y. This allows us to compute $\sim x * y$ with ease since we have them side by side. 

Now try computing for $F(x,y,z)=x*y \space+\sim z$.

| x   | y   | z   | NOT z | x * y | F   |
| --- | --- | --- | ----- | ----- | --- |
| 0   | 0   | 0   | **1**     | **0**     | **1**   |
| 0   | 0   | 1   | **0**     | **0**     | **0**   |
| 0   | 1   | 0   | **1**     | **0**     | **1**   |
| 0   | 1   | 1   | **0**     | **0**     | **0**   |
| 1   | 0   | 0   | **1**     | **0**     | **1**   |
| 1   | 0   | 1   | **0**     | **0**     | **0**   |
| 1   | 1   | 0   | **1**     | **1**     | **1**   |
| 1   | 1   | 1   | **0**     | **1**     | **1**   | 

You could also remove all the zeros for ease of computation. Doing this allows the ones to shoot straight across and your eyes will meet the values much easier. Like in the following example $F(x,y,z)=x*(y*z+\sim y * \sim z)$

| x   | y   | z   | NOT y | NOT z | NOT y * NOT z | y * z | NOT y * NOT z + y * z | F   |
| --- | --- | --- | ----- | ----- | ------------- | ----- | --------------------- | --- |
| 0   | 0   | 0   | 1     | 1     | 1             |       | 1                     |     |
| 0   | 0   | 1   | 1     |       |               |       |                       |     |
| 0   | 1   | 0   |       | 1     |               |       |                       |     |
| 0   | 1   | 1   |       |       |               | 1     | 1                     |     |
| 1   | 0   | 0   | 1     | 1     | 1             |       | 1                     | 1   |
| 1   | 0   | 1   | 1     |       |               |       |                       |     |
| 1   | 1   | 0   |       | 1     |               |       |                       |     | 
| 1   | 1   | 1   |       |       |               | 1     | 1                     | 1   |

### Practice question: 
$$F(x,y) = \sim x(y+ \sim x) * \sim y$$
## Generate functions from truth tables
Individual variables are called **literals**. Multiplying (AND) literals such that the result is 1 yields a [[minterm]], the minterm here is a function in which multiplying the literals yield true.

Example:

| x   | y   | F                                                                  |
| --- | --- | ------------------------------------------------------------------ |
| 0   | 0   | 0                                                                  |
| 0   | 1   | 0                                                                  |
| 1   | 0   | 0                                                                  |
| 1   | 1   | 1  (this is the only 1, only true when x * y => minterm is x * y ) |

What happens if there are 2 trues in the same table? Well let's see:

| x   | y   | F             |
| --- | --- | ------------- |
| 0   | 0   | 0             |
| 0   | 1   | 1 (NOT x * y) |
| 1   | 0   | 0             |
| 1   | 1   | 1  (x * y)    | 

Then our function is $(\sim x \cdot y) + (x \cdot y)$. Because it's only true IF $(\sim x \cdot y)$ OR $(x \cdot y)$, ahaaa makes sense, no? This form is called the **Sum of Products** or (SOP). This also works with regular Boolean expressions. Try this with $F(x,y,z) = (x + z) \cdot y$:

| x   | y   | z   | (x + z) | F                 |
| --- | --- | --- | ------- | ----------------- |
| 0   | 0   | 0   |         |                   |
| 0   | 0   | 1   | 1       |                   |
| 0   | 1   | 0   |         |                   |
| 0   | 1   | 1   | 1       | 1 (NOT x * y * z) |
| 1   | 0   | 0   | 1       |                   |
| 1   | 0   | 1   | 1       |                   |
| 1   | 1   | 0   | 1       | 1 (x * y * NOT z) |
| 1   | 1   | 1   | 1       | 1 (x * y * z)     | 

Then the SOP of the function $F(x,y,z) = (x + z) \cdot y = xyz + xy \sim z + \sim x yz$. And they are called **logically equivalent statements**.
# Definitions
## Logical equivalence
Two functions are considered logically equivalent **if and only if** their literals are the same on the truth table. The best example is through [[concepts/math/Boolean Algebra#Boolean Algebra Laws and Theorems|DeMorgan's Law]]. We can see that the LHS is equivalent to the RHS. Thus they are logically equivalent. 
## Tautology
If a statement yields true for all possible truth values of its compound variables, it is a **tautology**.
Example: $P + \sim P$ is a tautology because it yields true no matter what its variables' values are.
## Contradiction
Contradiction is the opposite of tautology. If a statement yields false for all possible truth values of its compound variables, it is a **contradiction**.
Example: $Q * \sim Q$ is a contradiction since it always yields false.