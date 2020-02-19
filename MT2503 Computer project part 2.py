# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# MT2503 Project part 2
# Armand Halgreen
print 'MT2503 Project part 2'


from numpy import *
from matplotlib.pyplot import *


# Question 4
print 'Question 4'

# Define the functions
def g(x,y):
    g=a1-b1*x-c1*exp(d1*y)
    return g
def h(x,y):
    h=a2-b2*y-c2*exp(d2*x)
    return h
a1=a2=b1=b2=1
c1=d1=0.1
c2=0.2
d2=0.3

# Print the functions
print 'g(x,y)=a1-b1x-c1*exp(d1*y)'
print 'h(x,y)=a2-b2x-c2*exp(d2*y)'

# Define the partial derivatives
# Partial deivatives for g(x,y)
def gx(x,y):
    gx=-b1
    return gx
def gy(x,y):
    gy=-d1*c1*exp(d1*y)
    return gy

# Partial derivative for h(x,y)
def hx(x,y):
    hx=-d2*c2*exp(d2*y)
    return hx
def hy(x,y):
    hy=-b2
    return hy

# Define xn,yn,xn1,yn1
#Note these values are chosen as a 'starting point' they are slighty random,however please note that due to the percentage part the starting number cannot be too big
xn=1.0
yn=1.0
xn1=1.0
yn1=1.0
percentage=99.999999999
# Define iterative formula (xn1)
xn1=((hy(xn,yn)*(g(xn,yn)-gx(xn,yn)*xn-gy(xn,yn)*yn))-(gy(xn,yn)*(h(xn,yn)-hx(xn,yn)*xn-hy(xn,yn)*yn)))/(gy(xn,yn)*hx(xn,yn)-hy(xn,yn)*gx(xn,yn))
print 'This is my iteration formula for xn1'
'xn1=((hy(xn,yn)*(g(xn,yn)-gx(xn,yn)*xn-gy(xn,yn)*yn))-(gy(xn,yn)*(h(xn,yn)-hx(xn,yn)*xn-hy(xn,yn)*yn)))/(gy(xn,yn)*fx(xn,yn)-fy(xn,yn)*gx(xn,yn))'

# Define iterative formula (yn1)
yn1=((hx(xn,yn)*(g(xn,yn)-gx(xn,yn)*xn-gy(xn,yn)*yn))-(gx(xn,yn)*(h(xn,yn)-hx(xn,yn)*xn-hy(xn,yn)*yn)))/(gx(xn,yn)*hy(xn,yn)-hx(xn,yn)*gy(xn,yn))
print 'This is iteration formula for yn1'
'yn1=((hx(xn,yn)*(g(xn,yn)-gx(xn,yn)*xn-gy(xn,yn)*yn))-(gx(xn,yn)*(h(xn,yn)-hx(xn,yn)*xn-hy(xn,yn)*yn)))/(gx(xn,yn)*hy(xn,yn)-hx(xn,yn)*gy(xn,yn))'

# Create the loop for the iteration, this is for the x value
while ((xn1/xn)*100)<percentage:
    xn=xn1
    xn1=((hy(xn,yn)*(g(xn,yn)-gx(xn,yn)*xn-gy(xn,yn)*yn))-(gy(xn,yn)*(h(xn,yn)-hx(xn,yn)*xn-hy(xn,yn)*yn)))/(gy(xn,yn)*hx(xn,yn)-hy(xn,yn)*gx(xn,yn))
print 'xn1 or alpha=',xn1
print 'xn1=0.892372(6d.p.)'
     
# Create the loop for the iteration, this is for the y value
while ((yn1/yn)*100)<percentage:
    yn=yn1
    yn1=((hx(xn,yn)*(g(xn,yn)-gx(xn,yn)*xn-gy(xn,yn)*yn))-(gx(xn,yn)*(h(xn,yn)-hx(xn,yn)*xn-hy(xn,yn)*yn)))/(gx(xn,yn)*hy(xn,yn)-hx(xn,yn)*gy(xn,yn))
print 'yn1 or beta=',yn1
print 'yn1=0.738609(6d.p.)'
print 'Point of intersection correct to 6d.p. is (0.892372,0.738609)'
print 'Please note these values are chosen as a "starting point" they are slighty random,however please note that due to the percentage part the starting number cannot be too big'


    