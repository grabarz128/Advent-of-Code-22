# -*- coding: utf-8 -*-
#Jakub Grabowski
from typing import List
import numpy as np

def read_file(filepath: str):
    with open(filepath, 'r') as file:

            to_convert = []

            for line in file:
                
                if len(line.split()) == 0:
                    continue

                temp = line.strip().split()
                to_convert.append(temp[0])

    return to_convert


def list_to_matrix(entry: List[str]):
    e_len = len(entry)
    matrix = np.zeros((e_len,e_len))

    for i in range(e_len):
        for j in range(e_len):
            matrix[i][j] = entry[i][j]

    return matrix

def check_if_visible(matrix: np.ndarray):
    
    result = 2*len(matrix) + 2*(len(matrix)-2)

    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix)-1):
            if if_point_visible(i,j,matrix):
                result += 1

    return result


def if_point_visible(x: int, y: int, matrix: np.ndarray) -> bool:
    house = matrix[x,y]
    left, right, top, bottom = False, False, False, False
    
    # horizontal axis

    # left side
    for i in range(0,y):
        if matrix[x][i] >= house:
            left = True
            break
    #right side
    for i in range(y+1,len(matrix)):
        if matrix[x][i] >= house:
            right = True
            break    

    # vertical axis

    #top side
    for i in range(0,x):
        if matrix[i][y] >= house:
            top = True
            break  
    
    #bottom side
    for i in range(x+1,len(matrix)):
        if matrix[i][y] >= house:
            bottom = True
            break  
    
    #print(x,y, house, left, top, right,bottom)
    #if all are true -> house won't be visible
    if left and right and top and bottom:
        return False
    else: 
        return True
    
def point_visible_score(x: int, y: int, matrix: np.ndarray) -> int:
    house = matrix[x,y]
    left, right, top, bottom = False, False, False, False
    score_left, score_top, score_right, score_bottom = 0, 0, 0, 0
    
    # horizontal axis

    # left side
    for i in reversed(range(0,y)):
        score_left +=1
        if matrix[x][i] >= house:
            left = True
            break
    #right side
    for i in range(y+1,len(matrix)):
        score_right +=1
        if matrix[x][i] >= house:
            right = True
            break    

    # vertical axis

    #top side
    for i in reversed(range(0,x)):
        score_top +=1
        if matrix[i][y] >= house:
            top = True
            break  
    
    #bottom side
    for i in range(x+1,len(matrix)):
        score_bottom +=1
        if matrix[i][y] >= house:
            bottom = True
            break  
    
    #print(x,y, house, score_left, score_top, score_right,score_bottom)
    #if all are true -> house won't be visible
    return score_left * score_top * score_right * score_bottom 

def find_maximum_score(matrix: np.ndarray) -> int:
    maxiumum = 0

    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix)-1):
            if point_visible_score(i,j,matrix) > maxiumum:
                maxiumum = point_visible_score(i,j,matrix)
                
    return maxiumum

#print(read_file("entry.txt"))
entry = read_file("entry.txt")

#print(list_to_matrix(entry))

matrix = list_to_matrix(entry)
#print(check_if_visible(matrix))
print(find_maximum_score(matrix))
