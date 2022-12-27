#!/usr/bin/python
# -*- coding: utf-8 -*-
#Jakub Grabowski


#starting point


def get_table(filepath: str):
    
    with open(filepath, 'r') as file:
	        input = file.read()
            
            # for line in file:
            #     if len(line.split()) == 0:
            #         continue
                
            #     reading and deleting "," and "-" from string
            #     temp = line.strip().split()
            #     print(temp)
                
                
            #     task = [int(s) for s in temp.split() if s.isdigit()]
    print(input)

def supply_stacks(filepath: str):
    
    with open(filepath, 'r') as file:
          

            for line in file:
                if len(line.split()) == 0:
                    continue
                
                #reading and deleting "," and "-" from string
                #temp = line.strip().split()
                #task = [int(s) for s in temp.split() if s.isdigit()]
    pass



              




get_table("table.txt")