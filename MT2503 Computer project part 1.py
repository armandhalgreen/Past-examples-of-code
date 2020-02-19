# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:53:51 2017

@author: ah302
"""
# MT2503 Project part 1
# Armand Halgreen
print 'MT2503 Project part 1'

# Question 1
# Part 1
print 'Question 1'
print 'Part 1'

from numpy import *
from matplotlib.pyplot import *

# First define for f(x): f1=sin(pi*exp(-x))

def f1(x):
    f=sin(pi*exp(-x))
    return f

#Note actual derivative =-pi*exp(-x12)cos(pi*exp(-x12))
def f2(x12):
    f=-pi*exp(-x12)*cos(pi*exp(-x12))
    return f

# n is the number of grid points. 
n = 10000
print 'n=',n

# x10 and x11 is a very small as clos to 0 as possible across which we are differentiating
x10=-0.000005
x11=0.000005
# x varies from x10 to x11

# zeros sets up a vector of the correct length with every element zero
x = zeros(n+1,dtype=float)
# We can see this by using a print statement
print 'x=',x
# the step size is (x11-x10)/n (distance between x values). Note we change the integer n into a real number 
step = (x11-x10)/float(n)
print 'step=',step

f = zeros(n+1,dtype=float)
df = zeros(n+1,dtype=float)
df2 = zeros(n+1,dtype=float)
dfdx= zeros(n+1,dtype=float)

# Starting value for x is x10
for i in range(0,n+1):
# assign the grid points in the vector x[i]
    x[i] = x10 + float(i)*step
# assign the function values (here called f1(x)) into the array f[i]
    f[i] = f1(x[i])
for i in range(0,n):
    
# First order accurate derivative
    df[i] = (f[i+1]-f[i])/step
df[n] = (f[n] - f[n-1])/step

# Second order accurate derivative 
df2[0]=(f[1]-f[0])/step
df2[n]=(f[n] - f[n-1])/step
for i in range(1,n):
    
# Second order accurate form for derivative
    df2[i] = (f[i+1]-f[i-1])/(2.0*step)



# Print the solution
print 'for',n,'gridpoints'
print 'x10=',x10,'x11=',x11
print 'First order accurate derivate=',df[n]
print 'Second order accurate derivate=',df2[i]
print 'Actual derivative=',f2(0)
print 'Percentage difference between actual derivative and econd order accurate derivate',((f2(0)-df2[i])/f2(0))*100,'%'
print 'Therefore rounds to 3.1416(4d.p.)'


# Question 1
# Part 2
print 'Question 1'
print 'Part 2'
# Part 2
# Plot the function f = sin(pi*exp(-x))

# Set up a 1D array from x=10**(-2) to x1=10**(-8) in steps of 10**(-1)
print 'Graph of the second order accurate derivative of sin(pi*exp(-x))'
print 'This is a logarithmic graph. It is going down by 10**(-1) each time on the x axis'
my_list1=[-2,-3,-4,-5,-6,-7,-8,-9]
x1=my_list1
print 'These are the x values, x=',x1

# Create a 1D array for y=sin(pi*exp(-x1))
my_list2=[3.14159149256,3.14033374299,3.14004993117,3.14002153347,3.14001869382,3.14001841488,3.14001837032,3.14001837032]
y=my_list2
print 'These are the y values, y=',y
# Plot y as a function of x1
plot(x1,y)
# Display the figure:
show()




# Question 2
# Part 1
print 'Question 2'
print 'Part 1'

# Define the function
def f(x):
    f = sin(pi*exp(-x))
    return f
close() 
# close any open graphics windows
# Set up an array of x values from 0 to 2
# Choose 1000 intervals in the x direction
n = 10000
step = 2.0/float(n)

# Use n gridpoints in x
x = zeros(n+1,dtype=float)

# Evaluate the integrand at the point x_i
Integrand = zeros(n+1,dtype=float)
x[0] = 0
x[n] = 2.0
Integrand[0] = f(x[0])
Integrand[n] = f(x[n])

# In the Trapezoidal rule we need the two end points and double all other points
# Add the terms and store them in the variable called sum
sum=Integrand[0]
for i in range(1,n):
    x[i] = 0 + float(i)*step
    Integrand[i] = f(x[i])
    sum = sum + 2.0*Integrand[i]
sum = sum + Integrand[n]
Integral = sum * step/2.0

print 'My integral = ',Integral,' for ', n,' intervals.'
print 'The integral correct to 4 d.p. =1.4310'
print 'Note if you increase n to 1000000 you get "My integral =  1.43101546242  for  1000000  intervals." So therefore it clearly rounds to 1.4310 4d.p.'




# Part 2
print 'Question 2'
print 'Part 2'
# Plot the function f = sin(pi*exp(-x))
# Set up a 1D array from x1=0 to x1=2 in steps of 0.01
# using numpy's arange():
print 'Graph of f = sin(pi*exp(-x))'
x1 = arange(0,2.01,0.01)

# Create a 1D array for y=sin(pi*exp(-x1))
y=sin(pi*exp(-x1))

# Plot y as a function of x1:
plot(x1,y)

# Display the figure:
show()

# Plot the Trapeziodal rule to numericallly integrate f = sin(pi*exp(-x))
# Set up a 1D array from x1=0 to x1=2 in steps of 0.01
# using numpy's arange():
print 'Graph for the Trapeziodal rule to numericallly integrate f = sin(pi*exp(-x))'
x2 = arange(0,1.9,0.1)
print 'x2/x values=',x2

#create a 1D array for sum
my_list1=[0.0294528473722,0.0833717721145,0.156092430281,0.242115407696,0.336567087861,0.435393636013,0.535387882015,0.634123518341,0.729846655224,0.821355505973,0.907885345057,0.989006995615,1.06454172265,1.13449240968,1.19898941317,1.25824891163,1.31254149253,1.36216890072,1.40744715781]
print 'my_list1/ y values=',my_list1

# Create a 1D array for y
y=my_list1

# Plot y as a function of x1:
plot(x2,y)

# Display the figure:
show()



























