#Libraries
import numpy as np
import time

### my functions' import
from myfunctions import multinsert

"""
    First of all, let's precise that there are countless means to solve Linear programming problems with python. 
    There are many libraries such as Scipy, PuLP, Pyomo, and Google OR-Tools
    Scipy is one of the best python library for Linear algebra. Scipy has many implentation of several Linear programming solving methods 
    including simplex's one thus the first option for many Python users is logically SciPy's optimize.linprog. 
    It is quite easy to use:
    just install Scipy and type in a python shell:
        from scipy.optimize import linprog
        linprog(c=c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='simplex')
        where "c" The coefficients of the linear objective function to be minimized,
        "A_ub" The inequality constraint matrix. Each row of A_ub specifies the coefficients of a linear inequality constraint on x.
        "b_ub" The inequality constraint vector. Each element represents an upper bound on the corresponding value of A_ub @ x.
        bounds A sequence of (min, max) pairs for each element in x, defining the minimum and maximum values of that decision variable 
    However, SciPy's linprog only solves minimization problems. Therefore, we need to provide our objective function in minimization form. 
    To do that, we need to “flip” the sign of the coefficients of our objective function — the equivalent of maximizing 10x1 + 5x2 is minimizing -10x1 - 5x2.
    For more detailled informations I strongly encourage you to read Scipy docs
    Notice that simplex methods as all others will be removed and replaced by "HIGHS" in Scipy's next release because the latter is faster and more robuste

    Okay, knowing that you can take a look at my numpy implementation of Simplex algorithm for maximization problems.
    Please Compare it to Scipy's one and send me feedbacks in order to improve mine.
"""

# The main function
def simplex(of, restrictions, biases, mode='max', Dual=False):
    if mode == 'max': 
        return SAM(of, restrictions, biases, mode, Dual=Dual)
    elif mode == 'min':
        global Dual1
        Dual1 = Dual
        restrictions = np.transpose(restrictions)
        return SAM(biases, restrictions, of, mode, Dual=True)
    else: return ValueError(mode)

#Simplex's algo for maximisation problem
def SAM(of, restrictions, biases, mode, Dual):
    """
        'restrictions' is a table of all the restrictions' coefs related to any primary variables
        thus 'restrictions' items must have the same shape which testify of the number of primary variables
        'biases' is a list of bias related to each restrictions
        'of' is a list coefs related to each primary variables in the objective function
        'Dual' is a bool to decide returning Dual solutions
    """
    begin = time.time()
    #Number of columns, NB: number of rows are explicitly defined creating "matrix"
    num_var = len(of)
    columns = num_var + len(restrictions) + 1
    #reshaping objective function coef to match with numbers of columns of the future matrice
    of = np.concatenate((np.array(of), np.zeros(columns - len(of))))
    #Creating the main matrice
    matrix = np.array([x for x in restrictions])
    biases = np.array(biases)
    matrix = np.append(np.hstack((matrix, np.identity(len(restrictions)), biases.reshape(len(biases), 1))), [of], axis=0)
    #Initializing order like a list all gaps
    order = ["E%i"%i for i in range(1, len(restrictions) + 1)]
    #Starting iterations
    while np.any(matrix[-1] > 0):
        #Column indice of the variable which is entering in the base or column indice of pivot 
        varin = np.argmax(matrix[-1])
        #Note that I would use matrix[:, [i]] to get the vectorized form
        bi_air = [bi/air for (bi, air) in zip(matrix[:, -1][:-1], matrix[:, varin][:-1]) if air != 0]
        multinsert(bi_air, np.where(matrix[:, varin][-1] == 0)[0], np.inf) #np.inf == float('inf')
        #index min(bi_air, for bi/air positives) and thus pivot row indice
        # or row indice of the variable to go out of the base "varout"
        varout = bi_air.index(min(filter(lambda a: a >= 0, bi_air)))
        order = base_move(num_var=num_var, order=order, inout=(varin, varout)) #Move in and out desired variables
        pivot = matrix[varout, varin] #simplex' algorithm pivot
        xpivot_row = np.copy(matrix[varout]) #save of pivot row
        matrix[varout] /= pivot
        for row in matrix:
            if np.array_equal(row, matrix[varout]):  # equivalent of (row == matrix[varout]).all
                continue                             # Don't touch pivot row
            uprow = np.array([row[varin] * xpivot_row[j] / pivot for j in range(columns)])
            row -= uprow    #update row by row
    matrix[-1] *= -1        # to get non-negative values in the last row
    order.append("fun")
    order = np.array(order).reshape(len(order), 1)
    if Dual:
        dual_var = dual_solut(array=matrix[-1][:-1], num_var=num_var)
        latency = time.time() - begin  # In seconds
        results = (np.hstack((order, matrix[:, [-1]])), np.hstack((dual_var, matrix[-1].reshape(dual_var.shape))), latency)
        return output(results=results, Dual=Dual, mode=mode)
    else: 
        latency = time.time() - begin  # In seconds
        results = (np.hstack((order, matrix[:, [-1]])), latency)
        return output(results=results, Dual=Dual, mode=mode)

### Miscellaneous functions
# A function to stay aware of variables' moves
def base_move(num_var, order, inout):
    if inout[0] < num_var: order[inout[1]] = "X%i" %(inout[0] + 1)
    else: order[inout[1]] = "E%i" %(inout[0] - num_var +1)
    return order

# A function to get dual variables
def dual_solut(array, num_var):
    slack = []
    for i in range(len(array)):
        if i < num_var: slack.append(f"E{i +1}")
        else: slack.append(f"Y{i -num_var +1}")
    slack.append("fun")
    return np.reshape(slack, (len(slack), 1))

# A function for a better results aesthetic
def output(results, Dual, mode):
    if mode == 'max':
        if Dual:
            print("Primal solution :")
            print(results[0])
            print(f"Dual Solution :")
            print(results[1])
            print(f"Execution time : {results[2]}")
        else:
            print(f"Primal solution :")
            print(results[0])
            print(f"Execution time : {results[1]}")
    else:
        if Dual1:
            print("Primal solution :")
            print(results[1])
            print(f"Dual Solution :")
            print(results[0])
            print(f"Execution time : {results[2]}")
        else:
            print(f"Primal solution :")
            print(results[1])
            print(f"Execution time : {results[2]}")
