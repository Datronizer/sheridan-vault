# Foreword
Functions is my favorite topic in mathematics, mainly because it is so often glossed over and underplayed by many fields while being their greatest building block.

Here I will attempt to explain functions in a technical sense in hopes that my explanation is clearer that that of the materials provided.

Below are two different approaches to explaining functions, I dub them the "technical approach" and the "laypeople approach." The definition will remain consistent between the two, however, only the way I explain and demonstrate will be different.
# Laypeople approach
## Thought problem
Suppose I want to create a machine that adds 1 apple to my basket every time I push a button. Let's  assume my basket is infinitely deep so I can add any many apples as I want. Now, answer yes or no to these 3 questions.
1. Suppose my basket has 19 apples, and I push the button. I should expect the machine to add 1 and return 20 apples right?
2. Suppose my basket has 19 apples, and I push the the button. If the machine straight up takes my basket and not returning any apples, can I safely assume that it isn't functioning correctly?
3. Suppose my basket has 19 apples, and I push the the button. If I receive 20 apples total one time, while I get 25 another time, can I assume it isn't functioning correctly?

If your answer is yes to the above 3 questions, you have grasped the 3 fundamental concepts of a function!
## Definition
A function is simply an equation or a set of equations that when I plug an argument in, I should expect something to be returned. For 2 identical functions with identical starting arguments, we should expect the same return value for both (because these two functions are technically the same).  
# Technical approach
The technical approach will skip the thought problem entirely because the motivation to define what a function is, is in fact the definition of the function itself: we wish to map something from $X$ to $Y$, and we want to define what we are doing.
## Definition
A function from the set $S$ to the set $T$ is an [[Mapping|assignment]] of each element $x \in S$ to some unique $y \in T$.

We express this information as such:
$$
\begin{align}
f: S &\rightarrow T \\
x &\rightarrow f(x)
\end{align}
$$
# Relevance to Computer Science
Functions is an important aspect of computer science. You can read more about the history of when the idea of functions was added %% I was too lazy to add it here %%.

Now functions is an irreplaceable part of computer science. For more information, refer to [[Functions (Computer Science)]]
# Sources:
[AbstractAlgebra.pdf (berkeley.edu)](https://math.berkeley.edu/~apaulin/AbstractAlgebra.pdf)
