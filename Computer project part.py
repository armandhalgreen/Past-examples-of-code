# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
# MT2505 Project part 1
# Armand Halgreen


# Question 1
def is_mult_table(X):
    if not isinstance(X, list):
        return False
    X1=np.asarray(X)
    if len(X1.shape) == 1:
       return False
    numrows = len(X)
    for i in xrange(numrows):    
        numcols = len(X[i])
        if not numrows==numcols:
           return False
    
    for i in xrange(numrows):
        for j in xrange(numcols):
            if not isinstance(X[i][j],int):
                return False
    for i in xrange(numrows):
        for j in xrange(numcols):
            if X[i][j]>=numrows or X[i][j]<0:
                return False
    for i in xrange(numrows):
        for j in xrange(numcols):
            if X[i][j]<numrows:
                return True                     
 

# Question 3
def random_mult_table(n):
    assert isinstance(n, int), "the argument must be an integer"
    assert n > 0, "the argument must be a positive integer"
    out = []
    for i in range(n):
        for j in range(n):
            out.append(list(np.random.randint(n,size=n)))
        return out


# Question 4
# There are n**(n**2) multiplication tables

# Question 5
def is_associative_mult_table(X):
    if not is_mult_table(X):
        return False
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                if not X[X[i][j]][k]==X[i][X[j][k]]:
                    return False
    else:
        return True 
    
    
# Question 7
def row_mult_table(X, i):
    assert is_mult_table(X), ("the first argument X must be a multiplication " "table")
    assert isinstance(i, int), "the second argument i must be an integer" 
    assert 0 <= i and i < len(X), ("the second argument must be at least 0 "
                             "and at most %d" % len(X) - 1)
    return X[i]
def col_mult_table(X, i):
    assert is_mult_table(X), ("the first argument X must be a multiplication " "table")
    assert isinstance(i, int), "the second argument i must be an integer" 
    assert 0 <= i and i < len(X), ("the second argument must be at least 0 "
                             "and at most %d" % len(X) - 1)
    return [row[i] for row in X] 

def identity_mult_tabel(X):
    x1=[]
    for i in xrange(len(X)): 
        count=0
        for j in xrange(len(X)):
            if row_mult_table(X,i)[j]==j and col_mult_table(X,i)[j]==j:
                count=count+1
        if count==len(X):
            x1.append(i)
    if len(x1)==1:
        return x1[0]
    else:
        return -1


import requests
X = eval(requests.get("https://goo.gl/QA6dWL").text)


# Question 8
import requests
X = eval(requests.get("https://goo.gl/QA6dWL").text)    


# Question 9
import pickle, requests
tabs = pickle.loads(requests.get("http://goo.gl/ZtqICh").text)


# a)
def is_associative_mult_table1(X):
    for n in xrange(len(X)):
        if not is_mult_table(X[n]):
            return 'Not a multiplication table'
        for i in xrange(len(X[n])):
            for j in xrange(len(X[n])):
                for k in xrange(len(X[n])):
                    if not X[n][X[n][i][j]][k]==X[n][i][X[n][j][k]]:
                        return 'Can find a multiplication table which fails to be associative on just one of the triple elements'
    else:
        return 'Cannot find a multiplication table which fails to be associative on just one of the triple elements'
is_associative_mult_table1(tabs)


# b)
def is_associative_mult_table2(X):
    for n in xrange(len(X)):
        if not is_mult_table(X[n]):
            return 'Not a multiplication table'
        count=0
        for i in xrange(len(X[n])):
            for j in xrange(len(X[n])):
                for k in xrange(len(X[n])):
                    if not X[n][X[n][i][j]][k]==X[n][i][X[n][j][k]]:
                        count=count+1
        if count==27:
        
            return 'Can find a multiplication table which fails to be associative on every of the triple elements'
    else:
        return 'Cannot find a multiplication table which fails to be associative on every of the triple elements'
is_associative_mult_table2(tabs)
     
             
# c)  
def is_associative_mult_table3(X,m):
    for n in xrange(len(X)):
        if not is_mult_table(X[n]):
            return 'Not a multiplication table'
        count=0
        for i in xrange(len(X[n])):
            for j in xrange(len(X[n])):
                for k in xrange(len(X[n])):
                    if not X[n][X[n][i][j]][k]==X[n][i][X[n][j][k]]:
                        count=count+1
        if count==m:
           return 'Can find m multiplication tables which fails to be associative on exaclty m of the triple elements where 0=<m=<27'
    else:
           return 'Cannot find m multiplication tables which fails to be associative on exaclty m of the triple elements where 0=<m=<27'
is_associative_mult_table3(tabs,1)
               

# Question 10 
# a)
def inverse(X):
    if not identity_mult_tabel(X)==-1:
        count=0
        for i in xrange(len(X)):
            for j in xrange(len(X)):
                if X[i][j]==identity_mult_tabel(X) and X[j][i]==identity_mult_tabel(X):
                    count=count+1
                    if count==len(X):
                        return True
    else:
        return False
  

def is_group_mult_table(X):
    count1=0
    for n in xrange(len(X)):
        if is_mult_table(X[n])==True:
            if is_associative_mult_table(X[n])==True:
                if not identity_mult_tabel(X[n])==-1:
                    if inverse(X[n])==True:
                        count1=count1+1
    return count1
is_group_mult_table(tabs)        


def is_group_mult_table1(X):
    count1=0
    for n in xrange(len(X)):
        count=0
        if is_mult_table(X[n])==True:
            if is_associative_mult_table(X[n])==True:
                if not identity_mult_tabel(X[n])==-1:
                    if inverse(X[n])==True:
                        for i in xrange(len(X[n])):
                            for j in xrange(len(X[n])):
                                if X[n][i][j]==X[n][j][i]:
                                    count=count+1
                        if count==len(X[n])*len(X[n]):
                            count1=count1+1
    return count1
is_group_mult_table1(tabs)        


# c) 
def is_group_mult_table2(X):
    count1=0
    for n in xrange(len(X)):
        count=0
        if not is_associative_mult_table(X[n])==True:
                for i in xrange(len(X[n])):
                    for j in xrange(len(X[n])):
                        if X[n][i][j]==X[n][j][i]:
                            count=count+1
                if count==len(X[n])*len(X[n]):
                    count1=count1+1
    return count1
is_group_mult_table2(tabs)           


def is_group_mult_table3(X):
    count1=0
    for n in xrange(len(X)):
        count=0
        if is_associative_mult_table(X[n])==True:
                for i in xrange(len(X[n])):
                    for j in xrange(len(X[n])):
                        if not X[n][i][j]==X[n][j][i]:
                            count=count+1
                if count>=1:
                    count1=count1+1
    return count1
is_group_mult_table3(tabs)           


# d)
def is_group_mult_table4(X):
    for n in xrange(len(X)):
        if is_mult_table(X[n])==True:
            x1=[]
            for i in xrange(len(X[n])): 
                count=0
                for j in xrange(len(X[n])):
                    if row_mult_table(X[n],i)[j]==j and col_mult_table(X[n],i)[j]==j:
                        count=count+1
                if count==len(X):
                    x1.append(i)
            if len(x1)>=1:
                return 'Yes some of the multiplication tables have more than one identity'
            else:
                return 'No there are no multiplication tables that have more than one identity'
is_group_mult_table4(tabs)        
  
 
# e)
def is_group_mult_table5(X):
    count=0
    for n in xrange(len(X)):
        if is_mult_table(X[n])==True:
            if is_associative_mult_table(X[n])==True:
                if  identity_mult_tabel(X[n])==-1:
                  if not inverse(X[n])==True:
                     count=count+1                                 
    return count
is_group_mult_table5(tabs)        



# f)
def is_group_mult_table6(X):
    for n in xrange(len(X)):
        if is_mult_table(X[n])==True:
            if not is_associative_mult_table(X[n])==True:
                if  not identity_mult_tabel(X[n])==-1:
                  if not inverse(X[n])==True:
                      return 'Can find a multiplication table satisfying the identity axiom but neither the associativity'
    else:
        return 'Cannot find a multiplication table satisfying the identity axiom but neither the associativity'

is_group_mult_table6(tabs)        

  
# Part 2

import requests
open("groups.pyc", "wb").write(requests.get("http://goo.gl/pWPkMJ").content)
from groups import *


# Question 1
def order_perm(x):
    assert IsPerm(x), "the argument must be a permutation"
    identity=SymmetricGroup(x.degree()).identity()
    order=1
    while x**order != identity:
        order=order+1
    return order


# Question 4
def is_subgroup(G, H):
    assert IsSymmetricGroup(G), "the first argument should be a symmetric group" 
    for h in H:
        if not h in G:
            return False
        for h1 in H:
            for h2 in H:
                print h**-1
                if not (h1*h2) in H:
                    if not (h1**-1) in H:
                        return False
    return True


print len(tabs)       
print 3**(9)

