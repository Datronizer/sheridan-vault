# Arithmetic Operations
## Binary Addition
$$ 
\begin{align}
0 + 0 &= 0\\
0 + 1 &= 1\\
1 + 0 &= 1\\
1 + 1 &= 0 \text{ carry } 1\\
1 + 1 + 1 &= 1 \text{ carry } 1\\
\end{align}
$$
Example 1: 
$$ 
\begin{align}
&1011 \\
+ &1110 \\
--&-- \\
1&1001
\end{align}
$$
## Hexadecimal Addition
Example 2: 
$$ 
\begin{align}
&28 \\
+ &43 \\
--&-- \\
&6B
\end{align}
$$
Example 3:
$$ 
\begin{align}
&2E1 \\
+ &85A \\
--&-- \\
&B3B
\end{align}
$$
Example 3 shows that $1 + A = B$ so it's left alone, but $E = 14$, $14 + 5 = 19$ which is more than $16$. Then it overflows into $3$, carry $1$ to the left. $2 + 8 + 1 = 11 = B.$

It might be hard to think of the operations off the top of your head. A cheatsheet for hexadecimal addition has been made for ease of reference.
![Hexadecimal addition table](https://www.tutorialspoint.com/computer_logical_organization/images/hexadecimal_addition_table.jpg)
## Hexadecimal subtraction
Example 4 (no borrowing): 
$$ 
\begin{align}
&9A \\
+ &43 \\
--&-- \\
&57
\end{align}
$$
Example 5:
$$ 
\begin{align}
&F4C \\
+ &85A \\
--&-- \\
&6F2
\end{align}
$$
# Floating point
Expanded notion of binary numbers with a fixed binary point
What is 1001.00101 as a decimal number?
%%TODO: Note incomplete, refer to class powerpoint to fill this with information.