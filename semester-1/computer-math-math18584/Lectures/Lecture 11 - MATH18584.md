# Sequences
A sequence is simply a list of numbers that follow a pattern. For example: the list of all integers is in fact a sequence. The list of all even numbers greater than 0 is a sequence. 

Sequences can be represented as
$$
\begin{align}
s &= a_i, a_{i+1},... \\
&\text{where} \\
a_{n+1} &= f(a_{n}) \space\space(\forall{n},\exists f : a_n\rightarrow a_{n+1} )
\end{align}
$$
Basically this means in a sequence, there always exists a function of some sort that will give us the next number in the sequence.

Example: 
- $1,4,9,16,25,...$ is a sequence of the equation $s = a_i^2$.
- $1,2,3,4,5,6,...$ is a sequence of the equation $s = a_i$
# Series
## Definition
A series is, simply put, the sum of a sequence.

Of course, being a computation that relies on a sequence, it also has 2 types: finite and infinite. A finite series would be a **summation** of all values $k$ for some $k$ starting from an arbitrary $i$ to some arbitrary limit $n$. This is notated with a $\Sigma$ symbol.

For example, given $x_1 = -1, x_2 = 3, x_3 = 7$:
$$
\sum_{i=1}^{3}(x_i)^2 = (x_1)^2 + (x_2)^2 + (x_3)^2 = 1 + 9 + 49 = 59
$$
## Series Expansion
Some functions or constants are often computable once converted into a series form. But we can't compute this series because, you know, it's infinite! However, you can still plug the first few values into this series and compute the value of the equation through these substitutions

This is called **series expansion**, because you expand the series by plugging in the first few values for ease of computations. The more you substitute, the more accurate the value gets.

This is actually how computers compute certain functions!

Example:
$$
e^x = \sum \frac{1}{n!} x^n = \frac{1}{0!}x^0 + \frac{1}{1!}x^1 + \frac{1}{2!}x^2 + \space...
$$
Here the summation without any notation is used as a shorthand for infinite series, typically from 0 to infinity.

Typically series expansions are more commonly seen in [[Calculus 2]] or [[Partial Differential Equations]]. We often use these to approximate values of weird graphs that don't have a straightforward answer. 