You can install and use my package for this implementation just by typing:
pip install diarray-simplex
in a terminal, note that while this package name is diarray-simplex the module name remind simplex_algo (To use it you have to import "simplex_algo" not "diarray-simplex"). Use it like below:

import simplex_algo
    simplex_algo.simplex(of, restrictions, biases, mode, Dual)

More infos about the package at https://pypi.org/project/diarray-simplex/

# Simplex_algo
Python (numpy) implementation of Simplex method for linear programming problems solving.

This is an implementation of simplex's algorithm for linear programming maximization and minimization problems made by the baby programmer that I am.
I would like y'all to test this code, help me fuguring out how to improve this implementation and please report any problem you got with the code.
Good to notice that this implementation miss test and will surely shows lacks with some problems.
However it proved a certain consistency.

Better provide the cannonical form's coefficients of problems you wanna solve with it
x + y ≥ b is equivalent to - x - y ≤ - b
x + y = b is equivalent to x + y ≥ b, x + y ≤ b
For Maximization:

Max z = cT x 
  Ax ≤ b          
  x ≥ 0
And for Minimization:

Min z = cT x
  Ax ≥ b
  x ≥ 0

where T represent the transpose operation

You can report issues here and send feedbacks to this email: yacoudiarra.wl@gmail.com
