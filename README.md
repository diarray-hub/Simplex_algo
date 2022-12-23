# Simplex_algo
Python (numpy) implementation of Simplex method for linear programming problems solving.

This is an implementation of simplex algorithm for linear programming maximization and minimization problems made by the baby python programmer that I am.
I would like y'all to test this code, help me fuguring out how to improve this implementation and please report any problem you got with the code.
Good to notice that this implementation miss test and will surely shows lakes and problems with some problems.
However it proved a certain consistency.

Better provide the cannonical form's coefficients of problems you wanna solve with it
x + y ≥ b is equivalent to - x - y ≤ - b
x + y = b is equivalent to x + y ≥ b, x + y ≤ b
For Maximization:

Max z = cT x 
  Ax ≤ b          where T represent the transpose operation 
  x ≥ 0
And for Minimization:

Min z = cT x
  Ax ≥ b
  x ≥ 0
