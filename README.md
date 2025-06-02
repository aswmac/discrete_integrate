
  
# discrete_integrate
The forward difference operator on the coefficients of a polynomial can be performed as a series of synthetic division steps,
which in turn can be represented as a matrix factorization of the matrix representation of the operator.

Keeping the evaluation input as the constant x and breaking down the synthetic division steps, gives a matrix representation:



# Matrix representation of one step of synth-op


$$\begin{bmatrix}
1 & 0 & 0 & 0 \\
x & 1 & 0 & 0 \\
x^2 & x & 1 & 0 \\
x^3 & x^2 & x & 1 \\
\end{bmatrix}
\begin{pmatrix}
a \\
b \\
c \\
d
\end{pmatrix} = \begin{matrix}
a \\
ax + b \\
ax^2 + bx + c \\
ax^3 + bx^2 + cx + d \\
\end{matrix}
$$

# So for  f(x) to f(x + 1)
$$\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 1 & 1 & 0 \\
1 & 1 & 1 & 1 \\
\end{bmatrix}=\begin{bmatrix}
1 & 0 & 0 & 0 \\
3 & 1 & 0 & 0 \\
3 & 2 & 1 & 0 \\
1 & 1 & 1 & 1 \\
\end{bmatrix}
$$
# The binomial numbers, as expected, because of the powers of (x + 1), giving delta f (because minus identity)
$$\begin{bmatrix}
0 & 0 & 0 & 0 \\
3 & 0 & 0 & 0 \\
3 & 2 & 0 & 0 \\
1 & 1 & 1 & 0 \\
\end{bmatrix}
$$
<p>
Losing one dimension makes sense because the difference of a constant is zero.
 The rest of the matrix is from the binomial numbers, missing the column of ones as well.
 </p>
#Binomial number patterns
 Now that it is known that the pattern comes from the binomial numbers, the matrix may be factored
 in terms of synthetic division steps, and those steps can be reversed a-la inverse matrix steps.
 #Hypergeometric pattern of Binomial numbers
 <p>
   $$ x^{\underline{2}} $$
 </p>
