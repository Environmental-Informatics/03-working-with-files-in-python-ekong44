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
import pandas
import itertools

# part 1 of the assignment 
george_data = open("2008Male00006.txt","r")
filename = george_data

# part 2 of the assignment 
## all rows is everything in one list
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
# =============================================================================
row0 = matrix[0]
row1 = matrix[1]
# row2 = matrix[2]
# row3 = matrix[3]
# row4 = matrix[4]
# row5 = matrix[5]
# row6 = matrix[6]
# row7 = matrix[7]
# row8 = matrix[8]
# row9 = matrix[9]
# row10 = matrix[10]
# row11 = matrix[11]
# row12 = matrix[12]
# row13 = matrix[13]
# row14 = matrix[14]
# =============================================================================
row15 = matrix[15] # storing the final line as a variable
del matrix[15] # deleting the final line from the matrix so we can work with it 

# =============================================================================
# yeardata_presort = [year[0] for year in matrix]
# datedata = [date[1] for date in matrix]
# timedata = [time[2] for time in matrix]
# print(timedata)
# =============================================================================

""" 
get key word to be equal to a list of values 
"""

transform_matrix = list(zip(*matrix))
final_matrix = dict(zip(row0,transform_matrix))
print(final_matrix)

# =============================================================================
# def adding_to_matrix():
#     i = 0
#     while i <= 15:
#         date_test = matrix[i][i]
#         i = i + 1
#         return date_test        
# print(adding_to_matrix())
# =============================================================================

""" 
messing with panda and data frames

https://thispointer.com/python-pandas-how-to-convert-lists-to-a-dataframe/
https://thispointer.com/select-rows-columns-by-name-or-index-in-dataframe-using-loc-iloc-python-pandas/
https://stackoverflow.com/questions/53414960/how-do-i-create-a-sum-row-and-sum-column-in-pandas

"""
# =============================================================================
# test = pandas.DataFrame(matrix, columns = ['Year', 'Day', 'Time', 'George #', ' X', ' Y', ' Asleep', 'Behavior Mode', 'Energy Level', 'Risk', 'ProbFoodCap', 'MVL', 'MSL', 'PercptionDist', 'Percent Step'])
# test = pandas.DataFrame(matrix)
# print(test)
# 
# yeardata = test.loc[1:14,'Year']
# print(yeardata)
# print(yeardata.to_string(index = False))
# =============================================================================
