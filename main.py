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
        out=filename.split("/")[2]
        #out =filename.split(".")[-2]
        output = out.split(".")[0] + ".sol"
        solver.solve(filename, output)
        print(time.time()-tps)
    
main()