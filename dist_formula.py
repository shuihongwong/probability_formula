import math
f_fact = lambda x : math.factorial(x)
f_bin = lambda n, c, p: f_fact(n)/(f_fact(c) * f_fact(n-c)) * p**c * (1-p)**(n-c) 