# Matrices
Oh boy, here we go again

A matrix is a rectangular array of numbers. E.g.:
$$
\begin{bmatrix}
a_{1,1} & a_{1,2} & a_{1,3} \\
a_{2,1} & a_{2,2} & a_{2,3} \\
a_{3,1} & a_{3,2} & a_{3,3} 
\end{bmatrix}
$$
That is a matrix. We can denote a location of an element in a matrix using the notation $a_{m,n}$ where $m$ is the row number, $n$ is the column number, both start from 1.


# Computing Matrices
## Adding
We can only add 2 matrices A and B if and only if their dimensions are the same.
$$ \begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix} 
+
\begin{bmatrix}
2 & 4 \\
6 & 8 
\end{bmatrix}
= 
\begin{bmatrix}
3 & 6 \\
9 & 12 
\end{bmatrix}
$$
To add, we simply add each element of the same location/coordinate of MatA and MatB.
Of course, this being addition means they are commutative as $A + B = B + A$. We will see soon that this is not necessarily the case for subtraction (as usual)
## Subtracting
Subtracting matrices work the same way, but subtraction is not commutative. However, if we compute $A - B$ and $B - A$, we soon see that these two are inverses of each other!
$$ \begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix} 
-
\begin{bmatrix}
2 & 4 \\
6 & 8 
\end{bmatrix}
= 
\begin{bmatrix}
-1 & -2 \\
-3 & -4 
\end{bmatrix}
$$
$$ 
\begin{bmatrix}
2 & 4 \\
6 & 8 
\end{bmatrix}
-
\begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix} 
= 
\begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix}
$$
This does make sense as $A - B = A + (-B) = -(B - A)$. So, by definition, subtractions, when flipped around are inverses of each other.
## Multiplication
Multiplication is some bullshit tho. There are too many different ways to multiply matrices, here's some.
### Scalar multiplication
Matrices can be multiplied by a number, this is called a scalar. Why? Because we are multiplying every element of the matrix by a "scale".

$$
3 \times
\begin{bmatrix}
2 & 4 \\
6 & 8 
\end{bmatrix}
=
\begin{bmatrix}
6 & 12 \\
18 & 24 
\end{bmatrix}
$$
Simple so far?
### Dot product
Dot product is what you've seen in physics way too many times. Take 2 matrices, let them be A and B with sizes 2x3 and 3x2. Here's how you do it.
1. Take the first row of A and multiply with the first column of B
	1. Each element of row A1 multiplies with a corresponding element of column B1
	2. After multiplying each one, sum them together.
	3. This is your first element for row 1 of C.
2. Do this for the first row of A vs. all the columns of B. This should be your first row of C
3. Go down a row of A, do steps 1 and 2 again and you'll get the next row of C
4. Keep going until no more rows. You should have all of C.
<small>(I don't have a visual on how this is done, so please refer to the class slides for a step-by-step demonstration.)</small>

Anyways, this of course also follows a compatibility rule. To use dot product between an $m \times n$ matrix and an $n \times p$ matrix. The "middle" value must be the same. The result will be an $m \times p$ matrix.
$$
(m \times \not n) \cdot (\not n \times p) \rightarrow(m\times p)
$$
<small>^^^ visual of what I meant.</small>
### Cross product
Take 2 matrices, A and B. Let's have these silly billies be 2x2 for the sake of simplicity. To get the answer matrix C, we will do something long winded 