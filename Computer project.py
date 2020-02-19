import numpy as np
import networkx as nx
import matplotlib as plt
plt.rcParams['figure.figsize'] = [12.0,12.0]
def grid_positions(G,scale=1):
    return dict((n,(scale*n[0],scale*n[1])) for n in G.nodes())
    
def edge_subgraph_nodes(E):
    V = set()
    for e in E:
        V.update(e)
        
    return V
    
def set_node_colors(G,N,color):
    for n in N:
        G.node[n]['color'] = color
        
def set_edge_colors(G,E,color):
    for i,j in E:
        G[i][j]['color'] = color
        
def set_edge_weights(G,E,weight):
    for i,j in E:
        G[i][j]['weight'] = weight
        
def draw_grid(n,X):
    """
    Draw an n x n grid with edges / nodes from X in red
    """
    
    G = nx.grid_2d_graph(n+1,n+1)
    set_node_colors(G,G.nodes(),'k')
    set_edge_colors(G,G.edges(),'k')
    set_edge_weights(G,G.edges(),0.5)
    
    set_node_colors(G,edge_subgraph_nodes(X),'r')
    set_edge_colors(G,X,'r')
    set_edge_weights(G,X,1)
    
    nc = [G.node[n]['color'] for n in G.nodes()]
    ec = [G[i][j]['color'] for i,j in G.edges()]
    w = [G[i][j]['weight'] for i,j in G.edges()]
    
    nx.draw(G,grid_positions(G,2),node_size=0.5,width=w,node_color=nc,edge_color=ec)

#Computer project
# MT2504 Computer project
print 'MT2504 Computer project'


# Exercise 1
print 'Exercise 1'
# Define your input n
n=3
# Define the function grid_vertices
def grid_vertices(n):
    s=[]
    for i in xrange (0,n+1,1):
        for j in xrange (0,n+1,1):
            s.append((i,j))
            
    return s
print 'Input value is',n
print grid_vertices(n) 


# Exercise 2
print 'Exercise 2'
# Define your inputs n1,n2
n1=3
n2=7
# Define the function step_right
def step_right(n1,n2):
    s1=[] 
    s1.append((n1,n2))
    s1.append((n1+1,n2))
    return s1
print 'The input values are',n1,n2
print 'output=',step_right(n1,n2) 


# Exercise 3
print 'Exercise 3'
# Define your inputs n3,n4
n3=3
n4=7
# Define the function step_up
def step_up(n3,n4):
    s2=[]
    s2.append((n3,n4))     
    s2.append((n3,n4+1))
    return s2
# Note enter now your input values in the ()
print 'The input values are',n3,n4
print 'output=',step_up(n3,n4) 


# Exercise 4
print 'Exercise 4'
# Define your inputs n5,n6,n7,n8
n5=1
n6=1
n7=1
n8=1
print 'The input values are',n5,n6,n7,n8
my_list=(n5,n6,n7,n8)
# Define the function set_to_path
def set_to_path(n5,n6,n7,n8):
    k=0
    l=0
    set_to_path=[]
    for i in my_list: 
        set_to_path.append([(k,l),(k+i,l+1-i)])
        k=k+i
        l=l+1-i
    return set_to_path
print 'output=',set_to_path(n5,n6,n7,n8)


# Exercise 5
print 'Exercise 5'
# Define your input n9
n9=5
print 'The input value n9 is',n9
# Define the function unifrom_set
def uniform_set(n9):
    s3=list(np.random.randint(2,size=n9))
    return s3
print 'output=',uniform_set(n9)



# Exercise 6
print 'Exercise 6'
# Part 1
print 'Part 1'
# Shuffle numbers from 1 to 9 inclusively
print 'Shuffle numbers from 1 to 9 inclusively'
x = [[i] for i in range(10)]
print 'The input values are=',x
np.random.shuffle(x)
print 'Output=', x

# Part 2
print 'Part 2'
# Shuffle k1 1's and n10-k1 0's
print 'Shuffle k1 1 s and n10-k1 0 s'
# Note k1 and n10 are variables

# Define your input values 
k1=5
n10=10
k2=n10-k1
print k1,'1 values'
print k2,'0 values'
my_list1=[]
for i in range(k2):
    my_list1.append(i*0)
for i in range(k1):
    my_list1.append(i*0+1)
print 'The input values are', my_list1

# Define the function uniform_k_set
def uniform_k_set(n10,k1):
    np.random.shuffle(my_list1)
    return my_list1
print 'For uniform_k_set(',n10,k1,') output=',uniform_k_set(n10,k1)

# Exercise 7
print 'Exercise 7'
# Define your inputs n11,n12
n11=5
n12=3
print 'The input values are',n11,n12
# Define the function unifrom_set
def uniform_sets(n11,n12):
    s4=[]
    for x in xrange (n11):
        s3=list(np.random.randint(2,size=n12))
        s4.append(s3)
    return s4
print 'For uniform_sets (',n11,',',n12,')output=', uniform_sets(n11,n12)


# Exercise 8
print 'Exercise 8'
# Define your inputs n13,n14
n16=0
n17=0
n18=0

n19=0
n20=1
n21=1

n22=1
n23=0
n24=1

n13=(n16,n17,n18)
n14=(n19,n20,n21)
n15=(n22,n23,n24)
print 'The input values are',n13,n14,n15
# Define the function unifrom_set
def sets_to_paths(n13,n14,n15):
   k=0
   z=0
   m=0
   n=0
   s=0
   p=0
   s8=[]
   s5=[]
   for i1 in n13:
       s5.append([(k,z),(k+i1,z+1-i1)])
       k=k+i1
       z=z+1-i1
       s8.append(s5)
       s6=[]
   for i2 in n14: 
       s6.append([(m,n),(m+i2,n+1-i2)])
       m=m+i2
       n=n+1-i2
       s8.append(s6)
       s7=[]
   for i3 in n15:
       s7.append([(s,p),(s+i3,p+1-i3)])
       s=s+i3
       p=p+1-i3
       s8.append(s7)
       return s8
print 'For sets_to_paths (',n13,',',n14,',',n15,')output=', sets_to_paths(n13,n14,n15)
print 'Please note it prints each 3 times however unsure how to get rid of this'

# Exercise 9
print 'Exercise 9'
# Define your inputs n25,n26
n25=10000
n26=100
print 'The input values are',n25,n26
# Define the function unifrom_set
def uniform_sets1(n25,n26):
    s9=[]
    for x in xrange (n25):
        s10=list(np.random.randint(2,size=n26))
        s9.append(s10)
    return s9
print 'For uniform_sets (',n25,',',n26,')output is stored in u10k'

# Store in variable u10k
u10k=uniform_sets1(n25,n26)


# Exercise 10
print 'Exercise 10'
# Define your inputs n27,n28,n30
n27=5
n28=10
n29=n28-n27
n30=5
print n27,'1 values'
print n29,'0 values'
s11=[]
for i in range(n29):
    s11.append(i*0)
for i in range(n27):
    s11.append(i*0+1)
print s11
print 'The input values are', s11

# Define the function uniform_k_set
def uniform_k_sets(n27,n28,n30):
    s12=[]
    for i in range(n30):
        np.random.shuffle(s11)
        s12.append(s11)
    return s12
print 'For uniform_k_sets(',n27,n28,n30,') output=', uniform_k_sets(n27,n28,n30)