#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#optimality coditions
import crossings as cr
import numpy as np 
import networkx as nx
from networkx.algorithms import bipartite


G= nx.Graph()
G.add_nodes_from([1,2,3,4], bipartite = 0)
G.add_nodes_from([5,6,7,8], bipartite = 1)

G.add_edges_from([(1, 7), (2, 5), (3, 6), (4, 8)])


G2= nx.DiGraph()
G2.add_edges_from([(1,6), (1,8), (2,6), (2,7), (3,5),(3,7),(4,5),(4,8)])
orderA = [1,2,3,4]
orderB = [5,6,7,8]

def get_extreme_neighbors(graph, orderA, orderB, v):
    nbs = list(graph.predecessors(v))
    indices = [orderA.index(i) for i in nbs]
    l = min(indices)
    r = max(indices) 
    return (orderA[l], orderA[r])    
    

def is_suited_pair(graph, orderA, orderB, v, w):
    (lv, rv) = get_extreme_neighbors(graph, orderA, orderB, v)
    (lw, rw) = get_extreme_neighbors(graph, orderA, orderB, w)
    if rv <= lw:
        return True, [v,w]
    elif rw <= lv:
        return True, [w,v]
    else:
        return False, []
    
def initialize_c(graph,orderA, orderB):
    c = np.zeros([len(orderB), len(orderB)])
    for i in range(np.shape(c)[0]):
        for j in range(np.shape(c)[1]):
            c[i][j]= cr.crossing_number(graph, orderA, orderB, orderB[i], orderB[j])
    return c

def initialize_SetC(graph, orderA, orderB):
    C= []
    for i in range(len(orderB)):
        for j in range(i+1, len(orderB)):
            cij = cr.crossing_number(graph, orderA, orderB, orderB[i], orderB[j])
            cji = cr.crossing_number(graph, orderA, orderB, orderB[j], orderB[i])
            if cij == cji:
                C.append((orderB[i], orderB[j]))
    return C
            
def initialize_D(graph, orderA, orderB):
    D = nx.DiGraph()
    for i in range(len(orderB)):
        for j in range(i+1, len(orderB)):
            answer = is_suited_pair(graph, orderA, orderB, orderB[i], orderB[j])
            if answer[0]:
                D.add_edge(answer[1][0], answer[1][1])
    return D
   

def edges_to_be_added(graph, orderA, orderB, D):
    C = initialize_SetC(graph, orderA, orderB)
    print("C")
    print(C)
    to_explore = []
    for i in range(len(orderB)):
        for j in range(i+1, len(orderB)):
            if True: #not ((orderB[i], orderB[j]) in C or (orderB[j], orderB[i]) in C):
                
                if not ((orderB[i], orderB[j]) in D.edges or (orderB[j], orderB[i]) in D.edges):
                    to_explore.append((orderB[i], orderB[j]))
    return to_explore

def is_leaf(graph, orderA, orderB, D):
    return edges_to_be_added(graph, orderA, orderB, D) == [] 

def solution_leaf(graph, orderA, orderB, D):
    return list(nx.topological_sort(D))

def branch(graph, orderA, orderB, D, edge):
    node1 = nx.DiGraph()
    node1.add_edges_from(list(D.edges))
    node1.add_edge(edge[0], edge[1])
    node1 = nx.transitive_closure_dag(node1)
    node2 = nx.DiGraph()
    node2.add_edges_from(list(D.edges))
    node2.add_edge(edge[1], edge[0])
    node2 = nx.transitive_closure_dag(node2)
    return node1, node2


    
    
#if to_explore is empty, then we are in a leaf node, otherwise, branch over two possible
#edges and construct nx.transitive_closure_dag()
    
    

    
#create a dag with edges all the pairs obtained by is_suited_pair