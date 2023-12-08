# Q1
## Question
List all the members of set A.  
$A = \{x \mid -1 ≤ x < 2, x \in \mathbb{Z}\}$

Write the power set of A.
## Answer
$$
\begin{align}
\mathcal{P}(A) = \{\emptyset, \{-1\},\{0\},\{1\},\{2\},\{-1, 0\},\{-1,1\},\{-1,2\}, \\\{0,1\},\{0,2\},\{1,2\},\{-1,0,1\},\{-1,0,2\},\{-1,1,2\},\{0,1,2\},\{-1, 0,1,2\}\}
\end{align}
$$
There are 16 elements in the power set of A.
# Q2
## Question
Let U = {0,1,2,3,4,5,6,7,8,9,10}, A = { 0, 4, 6, 8}, B= { 0, 1, 2, 3, 4} and C  = {4,5,6,9,10}  
Evaluate and show all your work.
$\overline{(A \cup B)}$ 
$\bar{A} \cap \bar{C}$
$B - C$
$A \cup (B \cap C)$
## Answer
$\overline{(A \cup B)} = \overline{\{0,1,2,3,4,6,8\}} = \{5,7,9,10\}$ 
$\bar{A} \cap \bar{C} = \{1,2,3,5,7,9,10\} \cap \{1,2,3,7,8\} = \{1,2,3,7\}$
$B - C = \{0,1,2,3\}$
$A \cup (B \cap C) = A \cup \{4\} = \{0,4,6,8\} = A$
# Q3
## Question & Answer
![[Pasted image 20231113225952.png]]
![[Pasted image 20231113221033.png]]
There are $16 + 5 + 21 = 42$ people who liked only 1 type of music.
There are $29+5+7 = 41$ people who liked exactly 2 types of music.
# Q4
## Question
State the domain and range for the following relation, and explain if it is a function.
$\{(−3, −4), (−1,2), (0,0), (−3,5), (2,4)\}$
## Answer
Domain $\mathcal{D}$: $\{-3,-1,0,2\}$
Range $\mathcal{R}$: $\{-4,0,2,4,5\}$

This is **not** a function because there exists an $x \in \mathcal{D}$ that maps to two $y$ values in $\mathcal{R}$. Example: $(-3,-4) \& (-3,5)$ are both $x = -3$ but they each map to a different $y$, thus violating the vertical line test.
# Q5
## Question
Determine the domain and range of each of the following functions. 
a) $\frac{1}{x + 4}$

b) $\sqrt{2x - 1}$

c) $-2x + 9$
## Answer
a) Domain: $\mathcal{D} = \{x \mid x \not= 4, x \in \mathbb{R}\}$
Range: $\mathcal{R} = \{y \mid y \not= 0, y \in \mathbb{R}\}$ 

b) Domain: $\mathcal{D} = \{x \mid x \ge \frac{1}{2}, x \in \mathbb{R} \}$ 
Range: $\mathcal{R} = \{y \mid y \ge 0, y \in \mathbb{R}\}$

c) Domain: $\mathcal{D} = \{x \mid x \in \mathbb{R} \}$ 
Range: $\mathcal{R} = \{y \mid y \in \mathbb{R}\}$
# Q6
## Question
List the first four terms of the following sequence, beginning with $n=0$.
$$A_n = \frac{(-1)^n}{(2n+1)!}$$
## Answer
$$A_0 = \frac{(-1)^0}{(2*0+1)!} = \frac{1}{1!} = 1$$
$$A_1 = \frac{(-1)^1}{(2*1+1)!}=\frac{-1}{3!} = -\frac{1}{6}$$
$$A_2 = \frac{(-1)^2}{(2*2+1)!}=\frac{1}{5!}=\frac{1}{120}$$
$$A_3 = \frac{(-1)^3}{(2*3+1)!}=\frac{-1}{7!}=-\frac{1}{5040}$$
# Q7
## Question
Evaluate:
$$
\sum^5_{n=1}(-1)^n(2n)
$$
## Answer
$$
\begin{align}
\sum^5_{n=1}(-1)^n(2n) &= (-1)^1(2*1) + (-1)^2(2*2) + (-1)^3(2*3)+(-1)^4(2*4)+(-1)^5(2*5) \\
&= (-1)(2) + (1)(4) + (-1)(6)+(1)(8)+(-1)(10) \\
&= -2 + 4 -6 + 8 -10 \\
&= -6
\end{align}
$$
# Q8
## Question
The North Telephone Co. charges a flat monthly fee of $25.00 for a telephone line and $0.20 per minute for long distance calls.  
a. Write an equation that will relate the total cost per month, C, to the number of minutes, m, of long distance calls that you make.   
b. If you make 30 minutes of long distance calls per month, what will it cost?
c. For an annual budget of $480, how many minutes of long distance calls per month can be done?
## Answer
a) $C(m) = 0.20m + 25.00$ or simply $C(m) = \frac{m}{5} + 25$
b) $C(30) = \frac{30}{5} + 25 = 6 + 25 = 31$
c) For an annual budget of 480, assuming we are using this amount evenly over every month, each month we'd get 
$$
\begin{align}
C(m) = \frac{m}{5} + 25 &= \frac{480}{12} \\
\frac{m}{5} + 25 &= 40 \\
\frac{m}{5} &= 15 \\
m &= 75
\end{align}
$$
# Q9
## Question
Using Graph Theory concepts, create your own application scenario (e.g. Netflix movie surfing, Facebook network etc.). Explain all the related concepts used in your application (e.g. degrees, multiplicity, type of graph etc.) and draw the graph.

## Answer
![[unnamed (2).jpg]]
This is a directed graph of how I technically know the Prime Minister of Vietnam through "6 degrees of connection." 
- The out-degree of vertex "Me" is equal to 3, because I'm classmates with a Scott Nguyen, best friends with one Anh, and I shook hands with the head of the department of Education a few times during our multiple school events.
- Technically, if we really want to be semantic about it, Me shaking hands with the Head of DOE is the same vice versa, meaning it's a 2 way path, meaning it is a **strongly connected graph**. In that case, yes, the multiplicity at "Me" is 2: shaking hands is 1 edge, interpretation at a conference is 1 more edge.
- Um... the name of the concept "6 degrees of connection" is technically wrong, in a mathematical sense? Since we are measuring degrees at the vertex, rather than the number of edges it takes to reach a coordinate. That would technically be a **path** of length 6 at max. In my case, it's 5.