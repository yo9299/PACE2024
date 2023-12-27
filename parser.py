import networkx as nx
from networkx.algorithms import bipartite
import os 

mypath = os.listdir("/home/vardevol/git/python/PACE2024/test/")
test_dir = "/home/vardevol/git/python/PACE2024/test/"

def parser(filename):
    input_graph = open(test_dir + filename, 'r')
    lines = input_graph.readlines()
    input_graph.close()
    lines = [line.rstrip() for line in lines] 
    i= 0
    data=lines[i].split(" ")
    if data[0] == 'c':
        i= 1
        data= lines[i].split("")
    (n_a, n_b, n_edges) = (int(data[2]), int(data[3]), int(data[4]))
    edges =lines[(i+1):]
    l_edges=[]
    for i in range(len(edges)):
        e = edges[i].split(" ")
        l_edges.append((int(e[0]), int(e[1])))
    return n_a, n_b, n_edges, l_edges
    
def create_graph(filename):
    n_a, n_b, n_edges, edges = parser(filename)
    G = nx.DiGraph()
    G.add_nodes_from(list(dict.fromkeys([ed[0] for ed in edges])), bipartite = 0)
    G.add_nodes_from(list(dict.fromkeys([ed[1] for ed in edges])), bipartite=1)
    G.add_edges_from(edges)
    return G, list(dict.fromkeys([ed[0] for ed in edges])),list(dict.fromkeys([ed[1] for ed in edges]))

def create_dataset(path):
    files = [f for f in mypath ]
    dataset = [f for f in files if f[-2]=="g" and f[-1] == "r"]
    list_graphs = []
    for file in dataset:
        list_graphs.append(create_graph(file))
    return list_graphs


def write_solution(filename, list_B):
    sol = open(filename, "a")
    towrite = []
    for i in range(len(list_B)):
        towrite.append(str(list_B[i]) + "\n")
    sol.writelines(towrite)
    sol.close()