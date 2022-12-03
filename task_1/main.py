#!/usr/bin/python
# -*- coding: utf-8 -*-
#Jakub Grabowski


def calorie_counting(filepath: str):

    with open(filepath, 'r') as file:
            suma = []
            n = 1
            max = 0
            for line in file:
                
                if len(line.split()) == 0:
                    temp_max = sum(suma)
                    if temp_max > max:
                        max = temp_max
                        elf_index = n
                    n = n+1
                    suma.clear()
                    continue

                temp = line.strip().split()
                
                for i in range(0,len(temp)):
                    if int(float(temp[i])) == float(temp[i]):   
                        temp[i] = int(float(temp[i])) 
                    else:   
                        temp[i] = float(temp[i])

                suma.append(temp[0])

    return elf_index, max


print(calorie_counting('entry.txt'))
