// TODO: Fill in missing blanks

# Determinant of a Matrix
## 2x2 Matrices
Use the inverted alpha method. Basically, for some 2x2 matrix 
$$\begin{bmatrix}
a_{1,1} & a_{1,2}  \\
a_{2,1} & a_{2,2}  \\
\end{bmatrix}$$
do $(a_{1,1} \times a_{2,2}) - (a_{1,2} \times a_{2,1})$

As you can see it's kinda like an inverted alpha shape! Same thing applies for 3x3 matrices as well but it's a bit more convoluted.
## 3x3 Matrices
For some 3x3 matrix 
$$
\begin{bmatrix}
a_{1,1} & a_{1,2} & a_{1,3} \\
a_{2,1} & a_{2,2} & a_{2,3} \\
a_{3,1} & a_{3,2} & a_{3,3} 
\end{bmatrix}
$$
Take the first element of the first row. Block out the row and column intersecting it. You should have a 4 other elements. Turn that into a 2x2 matrix and find the $det$ as specified above.

Now repeat for every element of only the top row. You should have 3 products, let's call them $a, b, c$. Do $(a_{1,1} \times a) - (a_{1,2} \times b) + (a_{1,3} \times c)$. Yes the signs alternate.

Example:
[insert image here]
# Inverse of a Matrix
To find an inverse of a matrix, we can manually do this through 4 steps:

Step 1: Find the Matrix of Minors
- For each element $a_{m,n}$ of a matrix, block out row $m$ and column $n$. You should now have the other elements.
- Make 2 products from this using an inverted alpha shape. 
- Subtract these products.
- Repeat for every element.

Step 2: Matrix of Cofactors
Here you basically give the first one a positive value and alternate the positive/negative values.
- Start from the first element on the top left
- Give that one a positive value
- The next one will be negative
- Repeat for every element

Step 3: Adjugate/Adjoint 
- Turn rows into columns and vice versa (Imagine flipping all the elements along the diagonal)

Step 4: Multiply by $\frac{1}{Det}$.

[insert example image here]

> [!note] Yes, the Gauss method works too but for the sake of our curriculum, we'll do it this way instead.

