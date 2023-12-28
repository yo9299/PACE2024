#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:00:14 2023

@author: vardevol
"""
import sys
import algorithm as solver

if len(sys.argv) < 2:
    print("Usage python3 script fileWithInputGraph")
    sys.exit()
    
filename = sys.argv[1]
#output = sys.argv[2]

def main():
    output = filename.split(".")[0] + ".sol"
    solver.solve(filename, output)
    
main()