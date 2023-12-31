#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:00:14 2023

@author: vardevol
"""
import sys
import algorithm as solver
import time

if len(sys.argv) < 2:
    print("Usage python3 script fileWithInputGraph")
    sys.exit()
    
filename = sys.argv[1]
#output = sys.argv[2]


def main():
    #for filename in files:
        tps=time.time()
        directory = filename.split("/")[0:-1]
        direct = "/".join(directory) + "/"
        out=filename.split("/")[-1]
        #print(out)
        out =out.split(".")[-2]
        output = out.split(".")[0] + ".sol"
        solver.solve(filename, str(direct) + str(output))
        print(time.time()-tps)
    
main()