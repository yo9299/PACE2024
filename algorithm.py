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
import time

sys. setrecursionlimit(100000)


def solve(filename, output):
    g, ordera, orderb = parse.create_graph(filename)
    g = c.Bipartite_graph(g, ordera, orderb)
    n = c.Node(g, cond.initialize_D(g))
    sol, m = dfs_opt([n], [], 100000)
    #return sol, m#list(nx.topological_sort(sol.digraph)) #sol
    parse.write_solution(output, sol)
    
        
       
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


 
def expand(node, curmin):
    #every time i branch, check that the cross number of node is smaller than curropt
    tobeadded = cond.edges_to_be_added(node)
    e = tobeadded.pop()
    new_nodes= branch(node, e)
    sol = [i for i in new_nodes if compute_current_crossings(i)< curmin]
    return new_nodes #sol
#branch shoud return a node!

def unfeasible(node):
    return False
      

def dfs(list_nodes):
    sol = []
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

def dfs_opt(list_nodes, cursol, curmin):
    sol = []
    #curmin = 100000 
    #cursol = []
    if list_nodes == []:
        return cursol, curmin 
    elif list_nodes != []:
        n = list_nodes[0]
        if cond.is_leaf(n):
        #compare to current min and replace if better, continue
            sol = list(nx.topological_sort(n.digraph))
            psol = [n.graph.orderB.index(i) for i in sol]
            ncross = cr.number_of_crossings(n.graph, psol)
            if ncross < curmin:
                curmin = ncross
                cursol = sol 
            return dfs_opt(list_nodes[1:], cursol, curmin)
        elif unfeasible(n):
            return dfs_opt(list_nodes[1:], cursol, curmin)
        else:
            return dfs_opt(expand(n, curmin)+list_nodes[1:], cursol, curmin)
         
        
def compute_current_crossings(node):
    D = node.digraph 
    sol = list(nx.topological_sort(D)) #only nodes in the edges
    not_ordered = list(nx.isolates(D))
    cursol = [ i for i in sol if i not in not_ordered ]
    psol = [node.graph.orderB.index(i) for i in cursol]
    value = cr.number_of_crossings(node.graph, psol)
    return value
    
   
    
    
     