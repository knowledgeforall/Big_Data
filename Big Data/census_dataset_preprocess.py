# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:37:22 2021

@author: Paul Polsinelli
"""

ED = {}
DVal ={}
EX = {}
count = 0

readfile = open("adult.data","r")
writefile = open("adult.ed.data", "w")

for line in readfile:
    a = line.split(",")
    ed = a[3]
    
    if ed not in ED:
        writefile.write(ed + '\n')
        ED[ed] = 1
        DVal[ed] = 1
        
    else: ED[ed] = ED[ed] + 1

for k in ED:
    print(k, ":", ED[k])
    
writefile.close()
readfile.close()
    
print("The number of distinct values for the education column is:", len(DVal))
