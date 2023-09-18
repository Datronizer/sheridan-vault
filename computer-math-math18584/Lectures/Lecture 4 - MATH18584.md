# Boolean Algebra
## Boolean Statements
## Boolean Operators
We can combine Boolean statements together with logical operators.

| A   | B   | A AND B | A OR B | A XOR B | NOT A | NOT B |
| --- | --- | ------- | ------ | ------- | ----- | ----- |
| 0   | 0   | 0       | 0      | 0       | 1     | 1     |
| 0   | 1   | 0       | 1      | 1       | 1     | 0     |
| 1   | 0   | 0       | 1      | 1       | 0     | 1     |
| 1   | 1   | 1       | 1      | 0       | 0     | 0     |

Other notations: 
- AND: $A \cdot B$, $A * B$, $AB$, $A \wedge B$
- OR: $A + B$, $A \vee B$
- XOR:  $A \oplus B$, "basically as long as A != B it's true"
- NOT: $\sim A$ or $\neg B$

There are 2 extra operators: conditional and biconditional. Simply put: **conditional** is **if A then B** ($A \implies B$), not the other way around. But **biconditional** means **A if and only if B** ($A \iff B$).

| A   | B   | A -> B | A <-> B |
| --- | --- | ------ | ------- |
| 0   | 0   | 1      | 1       |
| 0   | 1   | 1      | 0       |
| 1   | 0   | 0      | 0       |
| 1   | 1   | 1      | 1       | 

If you've already noticed, you'll probably see that $A \iff B$ is the opposite of $A \oplus B$. The tables we are using to demonstrate these are called **truth tables** and brother, you'll wish you have them to help out.
## Order of Operations
Booleans are evaluated in the following order:
1. Brackets
2. NOT
3. AND
4. OR/XOR (left to right)
5. If - then
6. Biconditional
Example: 
$$
\begin{align}
(A \cdot B \cdot C) + [A \cdot \sim(B \cdot C)]&\space\text{where A = 1, B = 0, C = 1} \\
(A \cdot B \cdot C) + [A \cdot \sim(B \cdot C)] &= (1 \cdot 0 \cdot 1) + [1 \cdot \sim(0 \cdot 1)] \\
&= (1\cdot0\cdot1) + [1 \cdot\sim(0)] \\
&= (1\cdot0\cdot1) + 1 \\
&= 0 + 1 \\
&= 1
\end{align}
$$
## Negation
Negation of a compound operation can be done using De'Morgan's Theorem (make sure to say you're using that theorem to negate in quizzes and papers). The theorem allows you to flip boolean operators given that they are negation of brackets.
$$
\begin{align}
&\sim(A \cdot B) \\
&\sim A + \sim B \space\space\space\space\text{De'Morgan's Theorem}
\end{align}
$$
Just like that
## Boolean Algebra Laws and Theorems
![[Pasted image 20230918085535.png]]
## Lifehack
It can be hard to imagine the truth table off the top of your head. I know mine is hard because my brain doesn't work that way. So here's a way to memorize.

Let P be a true statement and Q be something ambiguous. We can formulate a simple logic with this. Suppose I say 
- P: Today is Monday
- Q: This is math class
Then, we can say, A * B is Today is Monday AND this is math class. A -> B: Today is monday, which implies this is math class (assume I only 1 class on monday and that being math), etc.