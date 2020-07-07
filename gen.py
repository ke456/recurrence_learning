import random
import numpy as np

# generates d random numbers between lowest to highest
def rand_vec( d, lowest=-1.1, highest=1.1):
    return np.array([ random.uniform(lowest, highest) for i in range(d) ])

# given the roots (r_i) of the linear recurrence and coefficients given
# by the initial conditions (a_i), computes \sum_i r_i^{D} a_i 
def gen_Dth ( D, roots, coeff):
    return sum( [ roots[i]**D * coeff[i] for i in range(len(roots)) ] )

# generates the slice (D, D+d-1)
def gen_slice( D, roots, coeff):
    return np.array([ gen_Dth(D+i, roots, coeff) for i in range(len(roots)) ] )
