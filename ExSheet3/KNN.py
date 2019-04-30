import pandas as pd

def square_root(x):
    return x**(1/2)

def power(x):
    return x**2

def euclidean_distance(p, q):
    '''returns the euclidean distance of the points p and q'''
    square_root(power(pi - qi for pi, qi in zip(p, q)))
    
def euclidean_distance2(p, q):
    '''Returns the euclidean distance of the two given series p and p'''
 
    return square_root( sum( [(pi - qi)**2 for pi, qi in zip(p, q)] ) )

p = pd.DataFrame([5,5,3,2])
q = pd.DataFrame([5,5,1,1])


print(euclidean_distance2(p, q))