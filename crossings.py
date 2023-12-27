#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np

G= nx.Graph()
G.add_edges_from([(1, 7), (2, 5), (3, 6), (4, 8)])
orderA = [1,2,3,4]
orderB = [8,6,5,7]
#networkx graph and 2 arrays, one for the order of vertices in each side of bipartition
def doEdgesCross(orderA, orderB, edge1, edge2):
    (v0, v1) = edge1
    (u0, u1) = edge2    
    i0 = orderA.index(v0)
    i1 = orderB.index(v1)
    j0 = orderA.index(u0)
    j1 = orderB.index(u1)
    cross = ((i0 < j0) and (j1 < i1)) or ((j0<i0) and (i1<j1))
    return cross

    
def crossing_number(graph, orderA, orderB, v, w):
    edges= list(G.edges)
    counter= 0
    fedges = [e for e in edges if (e[1]== v or e[1] == w)]

    if orderB.index(v) < orderB.index(w):
        for i in range(len(fedges)):
            for j in range(i,len(fedges)):
                if doEdgesCross(orderA, orderB, fedges[i], fedges[j]):
                    counter +=1
    return  counter


def numberOfCrossings(graph, orderA, orderB):
    sum=0
    for i in range(len(orderB)):
        for j in range(i, len(orderB)):
            sum += crossing_number(graph, orderA, orderB, orderB[i], orderB[j])
    return sum

    
def numberOfCrossingsExp(Graph, orderA, orderB):
    edges = list(Graph.edges) 
    counter = 0
    for e in range(len(edges)):
        for j in range(e,len(edges)):
            if doEdgesCross(orderA, orderB, edges[e], edges[j]):
                counter += 1
    return counter 