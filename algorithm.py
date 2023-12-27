#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:15:50 2023

@author: vardevol
"""
import conditions as cond
import parser as parse
import sys

#sys. setrecursionlimit(64)

def solve(filename, output):
    g, ordera, orderb = parse.create_graph(filename)
    sol = algo(g, ordera, orderb)
    return sol
    parse.write_solution(output, sol)
    

def algo(graph, orderA, orderB):
    c=0
    D = cond.initialize_D(graph, orderA, orderB)
    print(D.edges)
    
    return recursion(graph, orderA, orderB, D,c), c
        


def recursion(graph, orderA, orderB, D, c):
    c +=1
    tobeadded = cond.edges_to_be_added(graph, orderA, orderB, D)
    print("D")
    print(D.edges)
    if tobeadded == []:
        print("empty list:")
        print(cond.solution_leaf(graph, orderA, orderB, D))
        return cond.solution_leaf(graph, orderA, orderB, D)
        print("should have returned sth")
    else: 
        e = tobeadded.pop() 
        print(e)
        node1, node2 = cond.branch(graph, orderA, orderB, D, e)
        print("before recursion1")
        recursion(graph, orderA,orderB, node1, c)
        print("before recursion 2")
        recursion(graph, orderA,orderB, node2, c)
        print("after recursions")
        print(c)

     