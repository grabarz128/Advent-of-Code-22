#!/usr/bin/python
# -*- coding: utf-8 -*-
#Jakub Grabowski

def includer(filepath: str):
    
    with open(filepath, 'r') as file:
            counter = 0
            counter2 = 0
            for line in file:
                
                if len(line.split()) == 0:
                    continue
                
                #reading and deleting "," and "-" from string
                temp = line.strip().split(",")
                temp[0], temp[1] = temp[0].split('-'), temp[1].split('-')
                for i in range(0,2):
                    for j in range(0,2):
                        if int(float(temp[i][j])) == float(temp[i][j]):   
                            temp[i][j] = int(float(temp[i][j])) 
                        else:   
                            temp[i][j] = float(temp[i][j])
                
                #making [5,8] to [5,6,7,8] 
                temp[0] = [n for n in range(temp[0][0],temp[0][1]+1)]
                temp[1] = [n for n in range(temp[1][0],temp[1][1]+1)]

                #check if temp[0]/[1] includes in temp[1]/[0] depending on the len()
                if len(temp[0]) < len(temp[1]):
                    if set(temp[0]).issubset(set(temp[1])):
                        counter += 1
                        counter2 += 1
                    elif  any(item in temp[1] for item in temp[0]):
                        counter2 += 1
                else:
                    if set(temp[1]).issubset(set(temp[0])):
                        counter += 1
                        counter2 += 1
                    elif  any(item in temp[1] for item in temp[0]):
                        counter2 += 1


    return counter, counter2

print(includer("entries.txt"))