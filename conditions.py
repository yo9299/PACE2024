#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#optimality coditions
import crossings as cr
import numpy as np 
import networkx as nx
from networkx.algorithms import bipartite
import classes as c


G= nx.Graph()
G.add_nodes_from([1,2,3,4], bipartite = 0)
G.add_nodes_from([5,6,7,8], bipartite = 1)
G.add_edges_from([(1, 7), (2, 5), (3, 6), (4, 8)])


def is_suited_pair(g, v, w):
    (lv, rv) = cr.get_extreme_neighbors(g, v)
    (lw, rw) = cr.get_extreme_neighbors(g, w)
    if rv <= lw:
        return True, [v,w]
    elif rw <= lv:
        return True, [w,v]
    else:
        return False, []
    
def initialize_C(g):
    C=[]
    c = cr.compute_crossing_numbers(g)
    for i in range(g.nB):
        for j in range(g.nB):
            if c[i][j]==c[j][i]:
                C.append((i,j))
    return C

            
def initialize_D(g):
    D = nx.DiGraph()
    D.add_nodes_from(g.orderB)
    for i in range(len(g.orderB)):
        for j in range(i+1, len(g.orderB)):
            answer = is_suited_pair(g, g.orderB[i], g.orderB[j])
            if answer[0]:
                D.add_edge(answer[1][0], answer[1][1])
    return D

def edges_to_be_added(n):
    g= n.graph
    D = n.digraph
    C = initialize_C(n.graph)
    to_explore = []
    for i in range(len(g.orderB)):
        for j in range(i+1, len(g.orderB)):
            if not (i, j) in C :
                if not ((g.orderB[i], g.orderB[j]) in D.edges or (g.orderB[j], g.orderB[i]) in D.edges):
                    to_explore.append((g.orderB[i], g.orderB[j]))
    return to_explore

def is_leaf(n):
    return edges_to_be_added(n) == [] 

def solution_leaf(g, D):
    return list(nx.topological_sort(D))

initialNode= c.Node(c.initialGraph, initialize_D(c.initialGraph))
    
#if to_explore is empty, then we are in a leaf node, otherwise, branch over two possible
#edges and construct nx.transitive_closure_dag()
    
    

    
#create a dag with edges all the pairs obtained by is_suited_pair