#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np
#import classes

G= nx.Graph()
G.add_edges_from([(1, 7), (2, 5), (3, 6), (4, 8)])
orderA = [1,2,3,4]
orderB = [8,6,5,7]
#networkx graph and 2 arrays, one for the order of vertices in each side of bipartition
def doEdgesCross(g, edge1, edge2):
    #input: g graph of class bipartite_graph, 2 edges as tuples
    (v0, v1) = edge1
    (u0, u1) = edge2    
    i0 = g.orderA.index(v0)
    i1 = g.orderB.index(v1)
    j0 = g.orderA.index(u0)
    j1 = g.orderB.index(u1)
    cross = ((i0 < j0) and (j1 < i1)) or ((j0<i0) and (i1<j1))
    return cross

def get_extreme_neighbors(g, v):
    #v should be an index?
    nbs = list(g.graph.predecessors(v))
    indices = [g.orderA.index(i) for i in nbs]
    l = min(indices)
    r = max(indices) 
    return (l,r) # (g.orderA[l], g.orderA[r])    


#given adjacency matrix L2*L1
def augmentA(g):
    A = g.get_adjacency_matrix()
    pA = np.zeros([g.nB, g.nA], dtype=np.int32)
    rA = np.zeros([g.nB, g.nA], dtype=np.int32)
    l = []
    r = []
    for i in range(g.nB):
        for j in range(g.nA):
            k = j+1
            rnbs= []
            while k < g.nA:
                if A[i][k] == 1:
                    rnbs.append(k)
                k +=1
            if rnbs != []:
                pA[i][j] = int(rnbs[0])
            
            else: 
                pA[i][j] = int(g.nA +1)
            rA[i][j] = int(len(rnbs))
        l.append(get_extreme_neighbors(g, g.orderB[i])[0])
        r.append(get_extreme_neighbors(g, g.orderB[i])[1])
    return pA, rA, l , r

#does not work
def compute_crossing_numbers(g):
    pA, rA, l, r = augmentA(g)
    c = np.zeros([g.nB, g.nB], dtype=np.int32)
    for v in range(g.nB):
        for w in range(g.nB):
            if v != w:
                cvw = 0
                w0 = l[w]
                while w0 <= r[w] and w0 <= r[v]:
                    cvw += rA[v][w0]
                    w0 = pA[w][w0]
                c[v][w] = cvw
    return c

#solution is given as a permutation of 0123 which represents the input ordering ie 5768
def number_of_crossings(g, solB):
    c = compute_crossing_numbers(g)
    sol = 0
    for i in range(len(solB)):
        for j in range(i+1, len(solB)):
            sol += c[solB[i], solB[j]]
    return sol 
            
    

'''   
def numberOfCrossingsExp(Graph, orderA, orderB):
    edges = list(Graph.edges) 
    counter = 0
    for e in range(len(edges)):
        for j in range(e,len(edges)):
            if doEdgesCross(orderA, orderB, edges[e], edges[j]):
                counter += 1
    return counter 

#this is wrong    
def crossing_number(g, v, w):
    edges= g.edges
    counter= 0
    fedges = [e for e in edges if (e[1]== v or e[1] == w)]

    if g.orderB.index(v) < g.orderB.index(w):
        for i in range(len(fedges)):
            for j in range(i,len(fedges)):
                if doEdgesCross(g, fedges[i], fedges[j]):
                    counter +=1
    return  counter


def numberOfCrossings(g):
    sum=0
    for i in range(len(g.orderB)):
        for j in range(i, len(g.orderB)):
            sum += crossing_number(g, g.orderB[i], g.orderB[j])
    return sum
'''