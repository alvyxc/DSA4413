from scipy.special import lambertw
import math
import sympy as sym

x = (86400 / math.pow(10, -9))
print (x)
y = lambertw(86400000000000)

print (x/y)

print(y) # (0.8526055020137254+0j)


# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
n = np.array(range(100))
#print(n)
t1 = 15 * n ** 2
t2 = 8 * n ** 3
t3 = 2 ** n
t4 = 3 ** n

t5 = []
#for x in n:
#    t5.append(math.factorial(x))

t6 = n * np.log(n)

t7 = n - 8 * np.log(n)

# Create the plot
#plt.plot(n,t1)
#plt.plot(n,t2)
#plt.plot(n, t3)
#plt.plot(n,t4)
#plt.plot(n,t5)
#plt.plot(n,t6)
#plt.plot(n, t7)

# Show the plot
#plt.xlim(0)
#plt.ylim(0)
#plt.show()

sym.init_printing()
x = sym.symbols('x')
f = sym.Eq(x*sym.log(x)*(10**-9), 86400)
result = sym.solve(f, x)
print(result)



