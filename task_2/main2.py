#!/usr/bin/python
# -*- coding: utf-8 -*-
#Jakub Grabowski

# A - rock
# B - Paper
# C - scissors

# X - rock
# Y - Paper
# Z - scissors

#win - 6
#draw - 3
#loss - 0


def score(l: str, r:str) -> int:
    
    if l == "A": # A - rock
        if r == "X":
            return 4 #1 + draw
        if r == "Y":
            return 8 #2 + win
        if r == "Z":
            return 3 #3 + loss
    if l == "B": # B - Paper
        if r == "X":
            return 1 #1 + loss
        if r == "Y":
            return 5 #2 + draw
        if r == "Z":
            return 9 #3 + win
    if l == "C": # C - scissors
        if r == "X":
            return 7 #1 + win
        if r == "Y":
            return 2 #2 + loss
        if r == "Z":
            return 6 #3 + draw

## x = lose 0 
# y = draw 3
# z = win 6

def score2(l: str, r:str) -> int:
    
    if l == "A": # A - rock
        if r == "X":
            return 3 #3 + loss
        if r == "Y":
            return 4 #1 + draw
        if r == "Z":
            return 8 #2 + win
    if l == "B": # B - Paper
        if r == "X":
            return 1 #1 + loss
        if r == "Y":
            return 5 #2 + draw
        if r == "Z":
            return 9 #3 + win
    if l == "C": # C - scissors
        if r == "X":
            return 2 #2 + loss
        if r == "Y":
            return 6 #3 + draw
        if r == "Z":
            return 7 #1 + win
    
        




def rps(filepath: str):
    result = 0
    result2 = 0
    with open(filepath, 'r') as file:

            for line in file:
                
                if len(line.split()) == 0:
                    continue

                temp = line.strip().split()
                
                # for i in range(0,len(temp)):
                #     if int(float(temp[i])) == float(temp[i]):   
                #         temp[i] = int(float(temp[i])) 
                #     else:   
                #         temp[i] = float(temp[i])
                result += score(temp[0],temp[1])
                result2 += score2(temp[0],temp[1])
    return (result, result2)


print(rps("entry.txt"))