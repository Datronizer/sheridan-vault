# Matrix Transformation
Suppose I have a matrix A and I want to stretch it by a factor of 2 on the x-axis, flip it along the y-axis, then flip it along the x-axis, how would I do that?

a = [-3, 1]

Method 1: One transformation at a time:

Method 2: Combo matrix (all at once)
$$ 
\begin{bmatrix}
1 & 0 \\
0 & -1 
\end{bmatrix} 

\begin{bmatrix}
-1 & 0 \\
0 & 1 
\end{bmatrix} 

\begin{bmatrix}
2 & 0 \\
0 & 1 
\end{bmatrix}
=
\begin{bmatrix}
-1 & 0 \\
0 & -1 
\end{bmatrix} 

\begin{bmatrix}
2 & 0 \\
0 & 1 
\end{bmatrix}
=
\begin{bmatrix}
-2 & 0 \\
0 & -1 
\end{bmatrix}
$$
Then we multiply this combo matrix to our matrix A to get the transformed matrix!

