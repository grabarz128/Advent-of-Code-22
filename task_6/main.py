# -*- coding: utf-8 -*-
#Jakub Grabowski

def read_file(filepath: str):
    with open(filepath, 'r') as file:

            for line in file:
                
                if len(line.split()) == 0:
                    continue

                temp = line.strip().split()
                   
    return temp[0]




def marker_check_four(input: str):

    position = 4 

    for i in range(0,len(input)-3):
        if len(set([input[i],input[i+1],input[i+2],input[i+3]])) == 4:
            break
        position += 1

    return position 

def marker_check_fourteen(input: str):

    position = 14

    for i in range(0,len(input)-13):
        test = []
        for j in range(0,14):
            test.append(input[i+j])
        
        if len(set(test)) == 14:
            break
        position += 1

    return position


entry = read_file("entry.txt")

print(marker_check_fourteen(entry))
