#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:59:45 2024

@author: vardevol
"""

def upper_bound_sol(input_graph):
    g = input_graph.graph 
    scores = dict.fromkeys(input_graph.orderB)
    for v in input_graph.orderB:
        #print(v)
        #print(list(g.predecessors(v)))
        vector = 0
        for n in list(g.predecessors(v)): # 
            vector += input_graph.orderA.index(n)
        scores[v] =( vector/g.degree[v])
        print(scores)
    #no hay que devolver los indices
    sortedsol = sorted(scores, key=scores.get)
    #print(sortedsol)
    #print([input_graph.orderB.index(v) for v in sortedsol] )
    #the return type is wrong
    return sortedsol #[input_graph.orderB.index(v) for v in sortedsol] 

def upper_bound_ind(input_graph):
    sol = upper_bound_sol(input_graph)
    return [input_graph.orderB.index(v) for v in sol]
       

