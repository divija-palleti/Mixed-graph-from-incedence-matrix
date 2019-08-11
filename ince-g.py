import numpy as np
import matplotlib.pyplot as plt
import math
# from itertools import permutations 

#--------------------------------------------------------------------

####### To find in which quadrant the point is present
def whichqua(x,y):
    
    if(x>= 50 and y>=50):
        return 0
    if(x>= 50 and y<50):
        return 1
    if(x<= 50 and y<=50):
        return 2
    if(x< 50 and y>=50):
        
        return 3
    return 4


#--------------------------------------------------------------------

####### Mark the point according to the quadrant
def mark( x, y, val):
    qua = whichqua(x,y)
    distance = 1.5
   
    if(qua == 0):
        x = x + distance
        y = y+distance

    if(qua == 1):
        x = x+distance
        y = y-distance

    if(qua == 2):
        x = x-distance -1
        y = y-distance -1
    if(qua == 3):
        x = x-distance
        y = y+distance
    plt.text(x,y, val, fontsize=9)


#--------------------------------------------------------------------

####### Plot the edges using matplotlib
def plotgraph(edges):


    plt.axis([0, 100, 0, 100])
    for i in range(edges.shape[0]):
        print(edges[i][0], edges[i][1])
        x0 = x[edges[i][0]]
        x1 = x[edges[i][1]]
        y0 = y[edges[i][0]]
        y1 = y[edges[i][1]]
        directed = edges[i][2]
        ax = plt.axes()
        if(directed == 0):
            ax.annotate("", xy=(x1,y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-"))
            
        else:
            ax.annotate("", xy=(x1,y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->"))
        
        plt.scatter(x0, y0, marker='.', color='red')
        plt.scatter(x1, y1, marker='.', color='red')

        mark( x0, y0, edges[i][0] )
        mark( x1, y1, edges[i][1] )

        #to indicate the self loop
        if( x1 == x0 and y1 == y0):
            plt.scatter(x1, y1, marker='.', color='green')
    
    plt.show()


#--------------------------------------------------------------------

####### Form the graph from the given matrix

def drawgraph(permuts, no_edge, no_vert, x, y, start, end, verts):

   
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
    return edges
    

#-------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":


    midx, midy = 50, 50
    radius = 25

    # matrix = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]

    # matrix =[[1,1,1,0, 0, 0], [1, 0, 0,1,1,0],[0,1,0,1,0,1], [0,0,1,0,1,1]]

    matrix = [[1, 1, 1, 0,0,0,0,0], [1,0,0,1,0,1,0,0],[0,-1,0,0,1,0,0,0], [0,0,1,-1,-1,0,1,1,], [0,0,0,0,0,-1,-1,0]]


    matrix = np.array(matrix)

    print(matrix.shape,"matrix shape")

    verts = []
    start = 0
    end = 0
    no_vert = matrix.shape[0]
    no_edge = matrix.shape[1]
    for i in range(no_vert):
        verts.append(i)
    permuts =(verts)



    n = matrix.shape[0]
    pi = 3.141
    x = []
    y = []
    
    ## In reference to a circle

    for i in range(n):
        x.append(radius * math.cos(2*pi*i/n) + midx)
        y.append(radius * math.sin(2*pi*i/n) + midy)

    
    edges = drawgraph(permuts, no_edge, no_vert, x, y, start, end, verts)

    plotgraph(edges)

    