from scipy.special import lambertw
import math
import sympy as sym

# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
n = np.array(range(2, 50))
#print(n)
t1 = (n**2-n)/2
t2 = (3/4)*n**2
t3 = (1/4)*n**2

plt.plot(n,t1, label='(n**2-n)/2')
plt.plot(n,t2, label='(3/4)*n**2')
plt.plot(n,t3, label='(1/4)*n**2')
#plt.plot(n,t4)
#plt.plot(n,t5)
#plt.plot(n,t6)
#plt.plot(n, t7)

# Show the plot
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('f1(n) vs T(n) vs f2(n)')
plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()

#sym.init_printing()
#x = sym.symbols('x')
#f = sym.Eq(x*sym.log(x)*(10**-9), 86400)
#result = sym.solve(f, x)
#print(result)



