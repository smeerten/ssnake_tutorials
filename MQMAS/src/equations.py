import numpy as np
I = np.array([3/2,5/2,5/2,7/2,7/2,7/2,9/2,9/2,9/2,9/2])
p = np.array([-3,3,-5,3,5,-7,3,5,7,-9])
from fractions import Fraction
#Encyclo eq 12
#Shearing factor
K = p*(36*I*(I+1)-17*p**2 - 10)/(36*I*(I+1) - 27)

for elem in K:
    print(Fraction(elem).limit_denominator(4000))

print('----')
lam = p * (I*(I+1)-3/4*p**2)/(-I*(I+1)+3/4) 
r = -3/10*(I*(I+1)-3/4)/(2*I*(2*I-1))**2
a = K - p
b = r*(K+lam)
z = 1 / (b/a - r)
for elem in z:
    print(Fraction(elem).limit_denominator(1000000))

