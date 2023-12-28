#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:15:50 2023

@author: vardevol
"""
import networkx as nx
import conditions as cond
import parser as parse
import sys
import classes as c
import crossings as cr

#sys. setrecursionlimit(64)


def solve(filename, output):
    g, ordera, orderb = parse.create_graph(filename)
    g = c.Bipartite_graph(g, ordera, orderb)
    n = c.Node(g, cond.initialize_D(g))
    sol = dfs([n])
    return list(nx.topological_sort(sol.digraph))
    #parse.write_solution(output, sol)
    

def algo(graph, orderA, orderB):
    D = cond.initialize_D(graph, orderA, orderB)
    print(D.edges)
    
    return recursion(graph, orderA, orderB, D,c)
        

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
        
       
def branch(node, edge): #graph, orderA, orderB, D, edge):
    node1 = nx.DiGraph()
    node1.add_edges_from(list(node.digraph.edges))
    node1.add_edge(edge[0], edge[1])
    node1 = nx.transitive_closure_dag(node1)
    node2 = nx.DiGraph()
    node2.add_edges_from(list(node.digraph.edges))
    node2.add_edge(edge[1], edge[0])
    node2 = nx.transitive_closure_dag(node2)
    return [c.Node(node.graph, node1), c.Node(node.graph, node2)]


 
def expand(node):
    tobeadded = cond.edges_to_be_added(node)
    e = tobeadded.pop()
    return branch(node, e)
#branch shoud return a node!

def unfeasible(node):
    return False
      

def dfs(list_nodes):
    sol = []
    curmin = 100000 
    cursol = []
    if list_nodes != []:
        n = list_nodes[0]
        if cond.is_leaf(n):
        #compare to current min and replace if better, continue
            sol = n
        elif unfeasible(n):
            sol = dfs(list_nodes[1:])
        else:
            sol = dfs(expand(n)+list_nodes[1:])
    return sol

'''def dfs(list_nodes):
    sol = []
    curmin = 100000 
    cursol = []
    if list_nodes != []:
        n = list_nodes[0]
        if cond.is_leaf(n):
        #compare to current min and replace if better, continue
            sol = list(nx.topological_sort(n.digraph))
            psol = [n.graph.orderB.index(i) for i in sol]
            ncross = cr.number_of_crossings(n.graph, psol)
            if ncross < curmin:
                curmin = ncross
                cursol = sol 
            sol = dfs(list_nodes[1:])
        elif unfeasible(n):
            sol = dfs(list_nodes[1:])
        else:
            sol = dfs(expand(n)+list_nodes[1:])
    else: 
        return cursol
    #return sol 
        
 '''
       
    
    
    
     