#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:26:43 2024

@author: vardevol
"""

'''def number_of_crossings(g, c, solB):
    #c = compute_crossing_numbers(g)
    sol = 0
    for i in range(len(solB)):
        for j in range(i+1, len(solB)):
            sol += c[solB[i], solB[j]]
    return sol 
            '''
import algorithm as solver
import conditions as cond
#heuristic: for each edge u,v to be added, it's the min of 
#    tobeadded = cond.edges_to_be_added(node) this is not the same each time bc we take the transitive
#closure each time. but still the heuristic of taking the min over edges to be added is admissible
#cost is exactly number_of_crossings
#k, the budget = upper bound

def cost(node, Cij):
    return solver.compute_current_crossings(node, Cij)

def heuristic(node, Cij):
    tobeadded = cond.edges_to_be_added(node)
    choices = []
    curmin = 0
    #filter so that only one directed edge appears. 
    #compute min Cij[]
    for (i,j) in tobeadded:
        if (i,j) not in choices and (j,i) not in choices:
            choices.append((i,j))
    for e in choices:
        curmin += min(Cij[e[0]][e[1]], Cij[e[1]][e[0]])
    return curmin 

    
def evaluation(node, Cij):
    return cost(node, Cij) + heuristic(node,Cij)

def find_best(list_nodes,Cij):
    nodes_d = dict.fromkeys(list_nodes)
    for n in list_nodes:
        nodes_d[n]=evaluation(n, Cij)
    return min(nodes_d, key=nodes_d.get)