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


def calorie_counting2(filepath: str):

    with open(filepath, 'r') as file:
            suma = []
            result = []
            num = 0
            
            for line in file:
                if len(line.split()) == 0:
                    continue
                num += 1
    
    n = 0
    with open(filepath, 'r') as file:
            for line in file:
                
                if len(line.split()) == 0:
                    result.append(sum(suma))
                    suma.clear()
                    continue
                

                temp = line.strip().split()
                
                for i in range(0,len(temp)):
                    if int(float(temp[i])) == float(temp[i]):   
                        temp[i] = int(float(temp[i])) 
                    else:   
                        temp[i] = float(temp[i])

                suma.append(temp[0])
                
                n +=1
                if n == num:
                    result.append(sum(suma))
                
                    break

    result.sort(reverse=True)
 
    return sum(result[0:3])


print(calorie_counting2('task_1/entry.txt'))
