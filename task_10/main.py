# -*- coding: utf-8 -*-
#Jakub Grabowski
from typing import List, Dict
import numpy as np

def read_file(filepath: str):
    with open(filepath, 'r') as file:

            to_convert = []

            for line in file:
                
                if len(line.split()) == 0:
                    continue

                temp = line.strip().split()
                to_convert.append(temp)

    return to_convert


def signal_read(entry: List[str]):
    x = 1
    cycle = 0
    cycles_n_values = {}
    for n in range(len(entry)):
        if entry[n][0] == "noop":
            cycle +=1 # and do nothing
            cycles_n_values[cycle] = x
        elif entry[n][0] == "addx":
            cycle +=1
            cycles_n_values[cycle] = x
            cycle +=1
            cycles_n_values[cycle] = x
            x += int(entry[n][1])
        if n == len(entry)-1:
            cycles_n_values["end"] = x

    
    return cycles_n_values
    
def find_signal_strength(cycles_values: Dict, cycle_list: List[int]) -> int:
    result = 0
    for cycle in cycle_list:
        result += cycle* cycles_values[cycle]

    return result




#print(read_file("entry.txt"))

entry = read_file("entry.txt")
result = signal_read(entry)

cycles = [20, 60, 100, 140, 180, 220]

print(find_signal_strength(result,cycles))

