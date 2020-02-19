# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# MT2503 Project part 3
# Armand Halgreen
print 'MT2503 Project part 3'



from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

# Question 4
print 'Question 5'


# Define the functions
def f(x,y):
    f=-x**3+y**3+3*x**2-6*x-4*y+4
    return f
def g(x,y):
    g=x**3+y**3+x-2*y-1
    return g
def h(x,y):
    h=1/(3+x**3+sin(pi*y))
    return h


# Part 1
print 'Part 1'

xlist = linspace(0.0, 2.0, 20)
ylist = linspace(0.0, 2.0, 20)
X, Y =  meshgrid(xlist, ylist)
Z=-X**3+Y**3+3*X**2-6*X-4*Y+4
W=X**3+Y**3+X-2*Y-1

plt.figure()
cp = plt.contour(X, Y, Z,levels=[0.0])
cp = plt.contour(X, Y, W,levels=[0.0])

plt.title('Contour Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Estimate alpha and beta
print 'my estimate for alpha is (0.3,1.6)'
print 'my estimate for beta is (0.8,0.2)'


# Part 2
print 'Part 2'

def dfdx(x,y):
    fx = -3*x**2+6*x-6
    return fx

def dfdy(x,y):
    fy = 3*y**2-4
    return fy

def dgdx(x,y):
    gx = 3*x**2+1
    return gx

def dgdy(x,y):
    gy= 3*y**2-2
    return gy

# This will be used as a root finding method for two functions of two variables
def ghroot(x,y,f2,g2,df2dx,df2dy,dg2dx,dg2dy,err,nmax):
    errorx = 1.0
    errory = 1.0
    n = 0
    
    while ((abs(errorx) > abs(err)) or (abs(errory) > abs(err)) and (n < nmax)):
        n = n+1
        det = df2dx(x,y)*dg2dy(x,y) - df2dy(x,y)*dg2dx(x,y)
        errorx = (- f2(x,y)*dg2dy(x,y) + g2(x,y)*df2dy(x,y))/det
        errory = (f2(x,y)*dg2dx(x,y) - g2(x,y)*df2dx(x,y))/det
        x = x + errorx
        y = y + errory
    return x, y

x0=0.3
y0= 1.6

err = 1.0e-6

nmax = 30

xyroot = ghroot(x0,y0,f,g,dfdx,dfdy,dgdx,dgdy,err,nmax)
xroot = xyroot[0]
yroot = xyroot[1]
print 'The root for alpha of f(x,y) and g(x,y)is x=',xroot,'and y=',yroot
print 'Alpha correct to 4d.p. is(0.4892,1.5595)'


# This will be used as a root finding method for two functions of two variables
def ghroot(x,y,f2,g2,df2dx,df2dy,dg2dx,dg2dy,err,nmax):
    errorx = 1.0
    errory = 1.0
    n = 0
    
    while ((abs(errorx) > abs(err)) or (abs(errory) > abs(err)) and (n < nmax)):
        n = n+1
        det = df2dx(x,y)*dg2dy(x,y) - df2dy(x,y)*dg2dx(x,y)
        errorx = (- f2(x,y)*dg2dy(x,y) + g2(x,y)*df2dy(x,y))/det
        errory = (f2(x,y)*dg2dx(x,y) - g2(x,y)*df2dx(x,y))/det
        x = x + errorx
        y = y + errory
    return x, y

x0=0.8
y0= 0.2

err = 1.0e-6

nmax = 30

xyroot = ghroot(x0,y0,f,g,dfdx,dfdy,dgdx,dgdy,err,nmax)
xroot1 = xyroot[0]
yroot1 = xyroot[1]
print 'The root for beta of f(x,y) and g(x,y) is x=',xroot1,'and y=',yroot1
print 'Beta correct to 4d.p. is (0.7978,0.1546)'


# Part 4
print 'Part 4'
print 'For this question requires to use the trapezoidal rule twice'
print 'This is the integration over x'
Integral = zeros(5,dtype=float)
for ival in range(1,5):
    n = 10**ival
# maximum value of x is xroot1
    step = xroot1/float(n)
#
# Use n gridpoints in x
#
    x = zeros(n+1,dtype=float)
#
# Evaluate the integrand at the point x_i
#
    Int = zeros(n+1,dtype=float)
    Integrand = zeros(n+1,dtype=float)
    Int[0] = 0.0
    Integrand[0] = 0.0
    x[0] = xroot
    print 'For ', n,' points, step = ',step
    for i in range(1,n+1):
        y1=yroot1*step
        x[i] = x[i-1] + step
        Integrand[i] = h(x[i],1)
        Int[i]= Int[i-1] + step*(h(x[i-1],y1)+h(x[i],y1))/abs(xroot-xroot1)
    print Int[n]
    if(ival < 5):
        Integral[ival] = Int[n]
        print 'Integral = ',Integral[ival],' for n=', n,' gridpoints' 

print 'This is the integration over y'
Integral1 = zeros(5,dtype=float)
for ival in range(1,5):
    n = 10**ival
# maximum value of x is yroot
    step = yroot/float(n)
#
# Use n gridpoints in x
#
    x = zeros(n+1,dtype=float)
#
# Evaluate the integrand at the point x_i
    Integrand1 = zeros(n+1,dtype=float)
    Int[0] = 0.0
    Integrand1[0] = 0.0
    x[0] = yroot1
    print 'For ', n,' points, step = ',step
    for i in range(1,n+1):
        x1=yroot1*step
        x[i] = x[i-1] + step
        Integrand1[i] = h(x1,x[i])
        Int[i]= Int[i-1] + step*(h(x1,x[i-1])+h(x1,x[i]))/abs(yroot-yroot1)
    print Int[n]
    if(ival < 5):
        Integral1[ival] = Int[n]
        print 'Integral = ',Integral1[ival],' for n=', n,' gridpoints'


print 'The doueble integrals is',Integral*Integral1