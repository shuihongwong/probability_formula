import math
f_fact = lambda x : math.factorial(x)
# Binominal distribution
prob_bin = lambda n, c, p: f_fact(n)/(f_fact(c) * f_fact(n-c)) * p**c * (1-p)**(n-c) 
exp_bin = lambda n, p: n*p
var_bin = lambda n, p: n*p*(1-p)
# Hypergeometric distribution
prob_hypergeom = lambda a, b, n, k: (f_fact(a)/(f_fact(a-k) *f_fact(k)) * f_fact(b)/(f_fact(n-k)*f_fact(b-n+k)))/(f_fact(a+b)/(f_fact(a+b-n)*f_fact(n)))
exp_hypergeom = lambda a, b, n: n*(a/(a+b))
var_hypergeom = lambda a, b, n: n*(a/a+b) *(1 - a/(a+b)) * ((a+b-n)/a+b-1)
# Geometric distribution
prob_geom = lambda p, k: (1-p)**(k-1) * p
exp_geom = lambda p: 1/p
var_geom = lambda p: (1-p)/p**2
# Negative binominal distribution
p_neg_bin = lambda k, r, p: f_fact(k-1)/(f_fact(k-r) * f_fact(r-1)) * p**r * (1-p)**(k-r)
exp_neg_bin = lambda r, p: r/p
var_neg_bin = lambda r, p: r*(1-p)/p**2
# Poisson distribution
prob_poisson = lambda Lambda, n, t: math.exp(-Lambda*t) *(Lambda*t)**n/f_fact(n)
exp_poisson = lambda Lambda: Lambda
var_poisson = lambda Lambda: Lambda

