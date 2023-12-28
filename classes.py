#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np

class Bipartite_graph:
    def __init__(self, graph, orderA, orderB):
        self.graph=graph
        self.orderA = orderA
        self.orderB = orderB
        self.edges = list(graph.edges)
        self.nA = len(orderA)
        self.nB = len(orderB)

    def get_adjacency_matrix(self):
        A = np.zeros([self.nB, self.nA])
        for i in range(self.nB):
            for j in range(self.nA):
                if (self.orderA[j], self.orderB[i]) in self.edges:
                    A[i][j] = 1
        return A
 
class Node:
    def __init__(self, graph, digraph):
        self.graph=graph
        self.digraph=digraph
        self.orderA = graph.orderA 
        self.orderB= graph.orderB
        
  
#cycle_8_shffled
G2= nx.DiGraph()
G2.add_edges_from([(1,6), (1,8), (2,6), (2,7), (3,5),(3,7),(4,5),(4,8)])
orderA = [1,2,3,4]
orderB = [6,7,8,5] 
initialGraph= Bipartite_graph(G2, orderA, orderB)
#initialNode= Node(initialGraph, cond.initialize_D(G2, orderA, orderB))


   