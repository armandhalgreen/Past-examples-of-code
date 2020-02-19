# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 10:45:36 2018

@author: ah302
"""
import numpy as np
import matplotlib.pyplot as plt

# MT2507
# Armand Halgreen
print
print 'MT2507 Computer project' 
print


# Part 1
print 'Part 1'
print


# Question 1
print 'Question 1'
print


s=0.01
r=0.4


def F(x):
    F=s-r*x+(x**2)/(1+x**2)
    return F


def dFdx(x):
    dFdx=-r+(2*x)/(1+x**2)-(2*x**3)/((1+x**2)**2)
    return dFdx


xn3=np.linspace(0.0,2.5,50)
fig1=plt.figure(2)
ax1 = fig1.add_subplot(111)
ax1.plot(xn3,F(xn3),'b-+')
ax1.set_xlabel('$x$',size='large')
ax1.set_ylabel('$F(x)$',size='large')
plt.show()


# Here you can choose the starting value for the Newton Raphson method due to the graph


xn2=0.0 
xn3=0.5
xn4=2.0


def xn(xn1,n,err):
        error=1.0
        n1=0
        while ((abs(error) > abs(err)) and (n1 < n)):
            n1 = n1+1
            error=(-((F(xn1))/(dFdx(xn1))))
            xn1 = xn1 + error
            print 'n=',n1,'xn=',xn1,'xn-xn-1',error
        return 'xn=',xn1,'nmax=',n,'xn-xn-1=',error,'number of iterations required=',n1,'error=',err


# These are the different roots 


print 'First root is'
print xn(xn2,100,1*10**(-5))
print
print 'Second root is',
print xn(xn3,100,1*10**(-5))
print
print 'Third root is'
print xn(xn4,100,1*10**(-5))
print


    
def Runge_Katta(xj,tj,h,n):
    xj2=[]
    xj0=xj
    for i in xrange(n):
        k1=F(xj)*h
        k2=F(xj+k1/2.0)*h
        k3=F(xj+k2/2.0)*h
        k4=F(xj+k3)*h
        xj1=xj+(1.0/6.0)*(k1+2*k2+2*k3+k4)
        xj=xj1
        xj2.append(xj1)
        tj2=[]
        for i in xrange(n):
            tj2.append(tj+h*i)
    fig2=plt.figure(2)
    ax2 = fig2.add_subplot(111)
    ax2.plot(tj2,xj2,'b-+')
    ax2.set_xlabel('$t$',size='large')
    ax2.set_ylabel('$x$',size='large')
    plt.show()
    return 'Initial conditions','tj=',tj,'xj=',xj0,'number of iterations=',n,'stepsize=',h


# Question 2
print 'Question 2'
print


print'a)'


print Runge_Katta(0.45,0.0,0.25,20)
print 


print 'b)'
print Runge_Katta(0.5,0.0,0.25,20) 
print   
    

# Part 2
print 'Part 2'
print


def f1(a1,b1,c1,d1,xn5,yn1):
    f1=a1-b1*xn5-c1*np.exp(d1*yn1)
    return f1


def f2(a2,b2,c2,d2,xn5,yn1):
    f2=a2-b2*yn1-c2*np.exp(d2*xn5)
    return f2


def df1dx(a1,b1,c1,d1,xn5,yn1):
    df1dx=-b1
    return df1dx


def df2dx(a2,b2,c2,d2,xn5,yn1):
    df2dx=-c2*d2*np.exp(d2*xn5)
    return df2dx


def df1dy(a1,b1,c1,d1,xn5,yn1):
    df2dy=-c1*d1*np.exp(d1*yn1)
    return df2dy


def df2dy(a2,b2,c2,d2,xn5,yn1):
    df2dy=-b2
    return df2dy


def fig3(a1,a2,b1,b2,c1,c2,d1,d2):
    xn6=np.linspace(0.0,0.9,50)
    fig3=plt.figure(3)
    ax3 = fig3.add_subplot(111)
    ax3.plot(xn6,(1/d1)*(np.log((a1-b1*xn6)/(c1))),'b-+')
    print np.log((a1-b1*xn6)/(c1))
    ax3.plot(xn6,(1/b2)*(a2-c2*np.exp(d1*xn6)),'b-+')
    ax3.set_xlabel('$x$',size='large')
    ax3.set_ylabel('$y$',size='large')
    plt.show()
    return 


# Here you can choose the starting value for the Newton Raphson method in 2D due to the graph


xn7=1.0
yn2=1.0


def fourth_steady_state(xn5,yn1,a1,a2,b1,b2,c1,c2,d1,d2,err,nmax1):
    errorx = 1.0
    errory = 1.0
    n = 0
    xn7=xn5
    yn2=yn1
    while ((abs(errorx) > abs(err)) or (abs(errory) > abs(err)) and (n < nmax1)):
        n = n+1
        det = df2dx(a2,b2,c2,d2,xn5,yn1)*df1dy(a1,b1,c1,d1,xn5,yn1) - df2dy(a2,b2,c2,d2,xn5,yn1)*df1dx(a1,b1,c1,d1,xn5,yn1)
        errorx = (- f2(a2,b2,c2,d2,xn5,yn1)*df1dy(a1,b1,c1,d1,xn5,yn1) + f1(a1,b1,c1,d1,xn5,yn1)*df2dy(a2,b2,c2,d2,xn5,yn1))/det
        errory = (f2(a2,b2,c2,d2,xn5,yn1)*df1dx(a1,b1,c1,d1,xn5,yn1) - f1(a1,b1,c1,d1,xn5,yn1)*df2dx(a2,b2,c2,d2,xn5,yn1))/det
        xn5 = xn5 + errorx
        yn1 = yn1 + errory
    print [[xn5],[yn1]]
    return 'x=',xn5,'y=',yn1,'f1(x,y)=',f1(a1,b1,c1,d1,xn5,yn1),'f2(x,y)=',f2(a2,b2,c2,d2,xn5,yn1),'nmax=',nmax1,'error=',err,'starting point',(xn7,yn2)
 
    
print fourth_steady_state(xn7,yn2,1.0,1.0,1.0,1.0,0.1,0.2,0.1,0.3,1.0e-6,30)    
print


# Part 3
print 'Part 3'
print    


def dxdt(tn,xn8,yn3,a,b):
    dxdt=1.0-(1.0+b)*xn8+(a*(xn8**(2.0))*yn3)
    return dxdt


def dydt(tn,xn8,yn3,a,b):
    dydt=b*xn8-a*((xn8**(2.0))*yn3)
    return dydt



def Runge_Katta(tj,xj,yj,h,n,a,b):
    tj1=[]
    xj1=[]
    yj1=[]
    for i in xrange(n):
        k1=dxdt(tj,xj,yj,a,b)
        l1=dydt(tj,xj,yj,a,b)
        k2=dxdt(tj+0.5*h,xj+0.5*h*k1,yj+0.5*h*l1,a,b)
        l2=dydt(tj+0.5*h,xj+0.5*h*k1,yj+0.5*h*l1,a,b)
        k3=dxdt(tj+0.5*h,xj+0.5*h*k2,yj+0.5*h*l2,a,b)
        l3=dydt(tj+0.5*h,xj+0.5*h*k2,yj+0.5*h*l2,a,b)
        k4=dxdt(tj+h,xj+h*k3,yj+h*l3,a,b)
        l4=dydt(tj+h,xj+h*k3,yj+h*l3,a,b)
        k=(1.0/6.0)*(k1+2.0*k2+2.0*k3+k4)
        l=(1.0/6.0)*(l1+2.0*l2+2.0*l3+l4)
        tj=(tj+h)
        tj1.append(tj)
        xj=(xj+h*k)
        xj1.append(xj)
        yj=(yj+h*l)
        yj1.append(yj)
    fig4=plt.figure(4)
    print'Question 1'
    print 
    print 'For a=',a,'b=',b
    print
    print 'The solution is',('xj1=',xj1[n-1],'yj1=',yj1[n-1]),'and for tj1=',tj1[n-1]
    print
    print'Question 2'
    print'a)'
    print 
    ax4 = fig4.add_subplot(111)
    ax4.plot(tj1,xj1,'b-+')
    ax4.set_xlabel('$t$',size='large')
    ax4.set_ylabel('$x$',size='large')
    plt.show()
    print
    fig5=plt.figure(5)
    ax5 = fig5.add_subplot(111)
    ax5.plot(tj1,yj1,'b-+')
    ax5.set_xlabel('$t$',size='large')
    ax5.set_ylabel('$y$',size='large')
    plt.show()
    print
    print'b)'
    print 'For a=',a,'b=',b    
    print
    print 'Phase plane'
    fig6=plt.figure(6)
    ax6 = fig6.add_subplot(111)
    ax6.plot(xj1,yj1,'b-+')
    ax6.set_xlabel('$x$',size='large')
    ax6.set_ylabel('$y$',size='large')
    plt.show()
    return





print Runge_Katta(0.1,0.1,0.1,0.25,1000,(input("What is a? ")),(input("What is b? ")))
print
print Runge_Katta(0.1,0.1,0.1,0.25,1000,(input("What is a? ")),(input("What is b? ")))
