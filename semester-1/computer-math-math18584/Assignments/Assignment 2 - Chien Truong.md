# Question 1:
## Solution:
$$
\begin{align}
\frac{3}{2} - \frac{7x}{4} &= \frac{-3(x+2)}{8} \\
\frac{12}{8} - \frac{14x}{8} &= \frac{-3(x+2)}{8} \\
12 - 14x &= -3(x+2) \\
12 - 14x &= -3x-6 \\
-11x &= -18 \\
x &= \frac{18}{11}
\end{align}
$$
# Question 2:
Jamie needs to lease a car. At Big City Nissan (BSN), Jamie can lease an Altima for $3,000 down plus $420 per month. Big City will also give her the first two months of her lease free. At Rye Town Nissan (RTN), they offer her the same car for $3960 down plus $400 per month. Rye Town will give her the first four months free. After how many months would both deals cost the same?

## Solution:
Let $m$ be the number of months
Then BSN's deal is $3000 + 420(m-2)$ (2 free months subtracted)
And RTN's deal is $3960 + 400(m - 4)$ (4 free months subtracted)

Then:
$$
\begin{align}
	420(m - 2)  + 3000 &= 400(m - 4) + 3960 \\
	420m - 840 + 3000 &= 400m - 1600 + 3960 \\
	420m + 2160 &= 400m + 2360 \\
	420m - 400m &= 2360 - 2160 \\
	20m &= 200 \\
	m &= 10  \\
\end{align}
$$
# Question 3:
## Solution:
$$
\begin{align}
2(x + 3) &= 3(x + 1) \\
2x + 6 &= 3x + 3 \\
2x - 3x &= 3 - 6 \\
-x &= -3 \\
x &= 3
\end{align}
$$
# Question 4:
## Solution:
![[unnamed (1).jpg]]
# Question 5:
## Solution:
Let the number of dimes be $d$ and the number of quarters be $q$.
We have
$$
\begin{cases}
	q + 6 &= d \\
	25q &= 10d
\end{cases}
$$
Substitute $d$ into $25q = 10d$ to get
$$
\begin{align}
25q &= 10(q + 6) \\
25q &= 10q + 60 \\
15q &= 60 \\
q &= 4 \\
\\
\therefore q=4&, d=10
\end{align}
$$
# Question 6:
## Solution:
$$
\begin{align}
	\begin{cases}
		-x -7y = 14 \\
		-4x - 14y = 28 \\
	\end{cases}
	\\\\
	\begin{cases}
		-4x - 28y = 56 \\
		-4x - 14y = 28 \\
	\end{cases} 
	\\\\
	\begin{cases}
		-14y = 28 \\
	\end{cases}
\end{align}
$$
So $y = -2$. Meaning $-x-7y=14$ is equivalent to $-x + 14 = 14$. 
Then $x = 0, y = 2$.
# Question 7:
A certain market opens for sales every 7th day of the week. If it opened last on a Friday, what day of the week will the market be opened again after nine months? (Take one month as 30 days)
## Solution:
Let the computation of some day $d$, $x$ days away, be $x \pmod{7} = d + n \in \{0, 1, 2, 3, 4, 5, 6\}$, where $n$ is however many week days apart from $x$.

Then we have:
$$
\begin{align}
	270\pmod{7} = Friday + 4
\end{align}
$$
That means the day we are looking for is 4 days from Friday, that being Tuesday.
# Question 8:
You have four external hard drives (X, Y, Z, W) containing a total of 480 gigabytes (GB) of data.

1. The drive X has three times as much data as drive Y.
2. The drive Z has twice the amount of data as drive Y and drive W combined.
3. The sum of the amount of data on drive Z and three times the amount of data on drive W is equal to the difference between 700GB and the amount of data on drive Y.

Determine the amount of data (in GB) on each drive.
## Solution:
First we convert everything into mathematical notation, here I'll be using $(x,y,z,w)$ instead of $(X,Y,Z,W)$ for personal clarity sake (capital letters are hard to read for me).
$$
\begin{cases}
	x + y + z + w &= 480 \\
	x &= 3y \\
	z &= 2(y + w) \\
	z + 3w &= 700 - y
\end{cases}
$$
I will start by converting the "big" equations into using only $y$ and $w$. Then:
$$
\begin{align}
	&\begin{cases}
		3y + y + 2(y + w) + w &= 480 \\
		2(y + w) + 3w &= 700 - y \\
	\end{cases} \\
	&\begin{cases}
		3y + y + 2y + 2w + w &= 480 \\
		2y + 2w + 3w + y &= 700 \\
	\end{cases} \\
	&\begin{cases}
		6y + 3w &= 480 \\
		3y + 5w &= 700 \\
	\end{cases} \\
	&\begin{cases}
		6y + 3w &= 480 \\
		6y + 10w &= 1400 \\
	\end{cases} \\
	&\begin{cases}
		-7w &= -920 \\
	\end{cases}\\\\
	&w = \frac{920}{7} \approx 131.43
\end{align}
$$
Then $w = \frac{920}{7} \approx 131.43$ GB. Plugging that into $3y + 5w = 700$ yields 
$$
\begin{align}
3y + \frac{4600}{7} &= 700 \\
21y + 4600 &= 4900 \\
21y &= 4900 - 4600 \\
21y &= 300 \\
y &= \frac{100}{7} \approx 14.29
\end{align}
$$
Plug that into $z = 2(y + w)$ yields
$$
z = 2(\frac{100}{7} + \frac{920}{7}) =2*\frac{1020}{7} = \frac{2040}{7} \approx 291.43
$$
Finally, plug that into $x = 3y$ to yield
$$x = 3*\frac{100}{7}=\frac{300}{7} \approx 42.86$$

We can test to make sure all these values are correct. Attempting to sum $x,y,z,w$ yields
$$
x + y + z + w = \frac{300}{7} + \frac{100}{7} + \frac{2040}{7} + \frac{920}{7} = \frac{3360}{7}  = 480 \space\text{(correct)}
$$
Therefore, our answers are:
$$
\begin{cases}
	x = \frac{300}{7} \\
	y = \frac{100}{7} \\
	z = \frac{2040}{7} \\
	w = \frac{920}{7}
\end{cases}
$$
# Question 9:
$$
\begin{align}
	\begin{cases}
		-7x -2y &= -13 \\
		x - 2y &= 11 \\
	\end{cases}
\end{align}
$$
## Solution:
We have $x - 2y = 11$ which is equivalent to $2y = x - 11$.
Then the first equation can be substituted to become
$$
\begin{align}
-7x - (x - 11) &= -13 \\
-7x - x + 11 &= -13 \\
-8x &= -24 \\
x &= 3
\end{align}
$$
Substitute the newfound $x = 3$ into $2y = x - 11$ to get $y = -4$.
	$\therefore x = 3, y = -4$
# Question 10:
Let $a,b,c,d$ be 4 consecutive odd integers. We have $a + d = 52, a + 2 = b, b + 2 = c, c + 2 = d$.
Then we can substitute:
$$
\begin{align}
	a + d &= 52 \\
	a + c + 2 &= 52 \\
	a + b + 2 + 2 &= 52 \\
	a + a + 2 + 2 + 2 &= 52 \\
	2a &= 46 \\
	a &= 23 \\
\end{align}
$$
Then $a = 23, b = 25, c = 27, d = 29$.