import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations 


midx, midy = 50, 50

radius = 25


matrix = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]

# matrix =[[1,1,1,0, 0, 0], [1, 0, 0,1,1,0],[0,1,0,1,0,1], [0,0,1,0,1,1]]

matrix = [[1, 1, -1, 0,0,0,0,0], [-1,0,0,1,0,1,0,0],[0,-1,0,0,1,0,0,0], [0,0,1,-1,-1,0,1,1,], [0,0,0,0,0,-1,-1,0]]


matrix = np.array(matrix)

print(matrix.shape,"matrix shape")

verts = []
start =0
end = 0
no_vert = matrix.shape[0]
no_edge = matrix.shape[1]
for i in range(no_vert):
    verts.append(i)
permuts =(verts)
print


n = matrix.shape[0]
pi = 3.141
x = []
y = []
for i in range(n):
    x.append(radius * math.cos(2*pi*i/n) + midx)
    y.append(radius * math.sin(2*pi*i/n) + midy)

for i in range(1):
    p = permuts
    print(p,"p")
    edges = []
    for i in range(no_edge):
        ones = []
        flag = 0
        for j in range(no_vert):
            if matrix[j][i]==1:
                start = p[j]
                ones.append(start)
                
            if matrix[j][i]== -1:
                flag=1
                end = p[j]
        
        
        
        if(flag == 1):
            

            ones.append(end)
            length  = len(ones)
            if(length == 1):
                ones.append(ones[0])
            ones.append(1)
            
        else :
            length  = len(ones)
            if(length == 1):
                ones.append(ones[0])
            ones.append(0)

           
        edges.append(ones)
    edges = np.array(edges)

    print(edges,"edges")
    
    plt.axis([0, 100, 0, 100])
    for i in range(edges.shape[0]):
        print(edges[i][0], edges[i][1])
        x0 = x[edges[i][0]]
        x1 = x[edges[i][1]]
        y0 = y[edges[i][0]]
        y1 = y[edges[i][1]]
        directed = edges[i][2]
        # plt.plot([x[edges[i][0]], x[edges[i][1]]], [y[edges[i][0]], y[edges[i][1]]], 'ro-')
        ax = plt.axes()
        # ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
        ax = plt.axes()
        # ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
        if(directed == 0):
            ax.annotate("", xy=(x1,y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-"))
            
        else:
            ax.annotate("", xy=(x1,y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->"))
        plt.scatter(x0, y0, marker='.', color='red')
        plt.scatter(x1, y1, marker='.', color='red')
        plt.text(x1+0.3, y1+0.3, edges[i][1], fontsize=9)
        plt.text(x0+0.3, y0+0.3, edges[i][0], fontsize=9)

        if( x1 == x0 and y1 == y0):
            plt.scatter(x1, y1, marker='.', color='green')
            



    plt.show()