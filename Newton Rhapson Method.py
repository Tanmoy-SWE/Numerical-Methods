# -*- coding: utf-8 -*-
"""

# Newton-Raphson method**
The Newton-Raphson method is another method of finding roots of a nonlinear function. Unlike the Bisection and False position method, it falls under the category of **Open methods** due to the fact that we only need one initial guess that does not have to bracket the actual root and may be taken on either side of the root.

In today's lab, we will be implementing the Newton-Raphson method in python. We will be considering the function f(x) as an array of coefficients, for instance if we want to have f(x) = x<sup>3</sup>+x-2, then in python we will create an array as follows:
"""

f = [1,0,1,-2]

"""Note that your implementation should be able to handle the array f of any size,which means it should be able to find the root of any given polynomial. But for testing purposes, you can use the array f given here.

Next, you will need to create a user-defined function as follows
```
func(f, x)
```
This function will take the coefficent array f and a point x as input and evaluate the value of the function at that point x using a loop and return that value. This function will be called in the other function that you will implement, which is as follows:
```
newtonraphson(f, Xi, epsilon)
```
This function will return the root of the equation represented by the array f and in case it does not reach the root exactly then it will return the close enough value to the root that has an absolute relative approximate error of at most epsilon (%).
"""

#Execute this cell to test how the function works

def func(a,b):
  result = a + b
  return result

print(func(1,2))

"""Note that in python, we do not need to specify the data type for parameters nor any return type for the function as these are implicitly determined. Also, note the colon (:) after the function signature. Indentation matters in python, since the consecutive codes having same indentation will be considered as a single block."""

def fun(f, x):
  result = 0
  for i in range(len(f)-1, -1, -1):
    
      result = result + f[len(f)-i-1]*pow(x,i)
  return result
fun(f,2)

def derivative(f, x):
  result = 0
  for i in range(len(f)-1, -1, -1):
      if i-1>0:
        result = result + f[len(f)-i-1]*pow(x,i-1)*i
  return result+1
derivative(f,2)

"""##Task 1
Implement the Newton-Raphson method for the above function and write a script for testing its implementation. The actual root is 1, and you can take the initial guess as 2.
"""

Xi = 2
epsilon = 0.01

# Write a function for evaluating the derivative of the polynomial given by array f
# def derivative(f, x):
#   result = 0
#   for i in range(len(f)-1, -1, -1):
    
#       result = result + f[len(f)-i-1]*pow(x,i-1)*i
#   return result
  


# Complete the following function
def newtonraphson(f, Xi, epsilon):
  # write your implementation here
  error = 10000
  while(error > epsilon):
    feqn = fun(f,Xi)
    fDeri = derivative(f,Xi)
    xnew = Xi - (feqn/fDeri)
    error = abs(xnew-Xi)*100/xnew
    Xi = xnew
    print(Xi," ",error)
  return Xi


# Write a script here for calling the above function
print(newtonraphson(f, Xi, epsilon))

newtonraphson(f,2,0.05)

"""## Task 2
We can plot graphs in python using the matplotlib library. An example of plotting graphs is shown here
"""

import numpy as np
import matplotlib.pyplot as plt

iters = np.arange(0, 5) #start=0, stop=5, and since no step is given, so default step=1
vals = np.arange(100, 200, 20) #start=100, stop=200, step=20

plt.plot(iters, vals)
plt.title("Iterations vs values plot")
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.show()

def plot(f, Xi, epsilon, ans,errors):
  # write your implementation here
  error = 10000
  while(error > epsilon):
    ans.append(Xi)
    feqn = fun(f,Xi)
    fDeri = derivative(f,Xi)
    xnew = Xi - (feqn/fDeri)
    error = abs(xnew-Xi)*100/xnew
    errors.append(error)
    Xi = xnew
    print(Xi," ",error)
  return Xi

ans = []
errors = []
plot(f,2,0.01, ans, errors)

"""Generate a plot of **iteration vs xmid** for the bisection method function you implemented earlier."""

#Write the code for generating the error curve here
import numpy as np
import matplotlib.pyplot as plt

# iters = np.arange(0, 5) #start=0, stop=5, and since no step is given, so default step=1
# vals = np.arange(100, 200, 20) #start=100, stop=200, step=20

plt.plot(errors)
plt.title("Iterations vs error plot")
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.show()
