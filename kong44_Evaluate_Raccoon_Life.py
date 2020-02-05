#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:44:21 2020
@author: kong44
Assignment 3 - Using Files and Simple Data Structures with Python

Objectives: 
    1) open, read, write the contents of data files 
    2) organize and summarize data 
    
Helpful files:
    https://stackoverflow.com/questions/25050311/extract-first-item-of-each-sublist
    https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary
"""

# part 1 of the assignment 
george_data = open("2008Male00006.txt","r")
filename = george_data

# part 2 of the assignment 
# all rows is everything in one list
all_rows = george_data.readlines() # Return all lines in the file, as a list where each line is an item in the list object
george_data.close()

# reference code from the course wiki page 
matrix = [0]*len(all_rows) # matrix is equal to a list of zeros that has a length of all the rows from the data set

# turning the rows into lists 
## matrix is now a list of lists 
for lidx in range(len(all_rows)):
    matrix[lidx] = all_rows[lidx].split(",") # split the line based on the separation flag
    
# checking number of rows    
num_of_rows = len(matrix)

# storing rows as variables
row0 = matrix[0]
row1 = matrix[1]
row15 = matrix[15] # storing the final line as a variable

del matrix[15] # deleting the final line from the matrix so we can work with it 
del matrix[0] # removing the header 

transform_matrix = list(zip(*matrix)) #everything is now a tuple
                        #header information is part of the tuple
final_matrix = dict(zip(row0,transform_matrix))

# convert tuples to list
conv_X = list(final_matrix[" X"]) # space is present or else keyword won't work
float_X = [float(i) for i in conv_X]

conv_Y = list(final_matrix[" Y"]) #space is necessary because original txt has the space 
float_Y = [float(i) for i in conv_Y] # turn to float

conv_day = list(final_matrix["Day"]) # left as string
conv_asleep = list(final_matrix[" Asleep"]) # left as string
conv_behave = list(final_matrix["Behavior Mode"]) # left as string

def average_list():
    
def sum_list():
    
def distance():
