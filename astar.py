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
    for (i,j) in tobeadded:
        if (i,j) not in choices and (j,i) not in choice:
            choices.append((i,j))
    for e in choices:
        node.

    
def evaluation(node, Cij):
    return cost(node, Cij) + heuristic(node,Cij)