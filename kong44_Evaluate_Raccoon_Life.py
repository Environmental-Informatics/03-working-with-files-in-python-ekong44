#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:44:21 2020
@author: kong44
Assignment 3 - Using Files and Simple Data Structures with Python

Objectives: 
1) open, read, write the contents of data files 
2) organize and summarize data 
"""
import pandas

# part 1 of the assignment 
george_data = open("2008Male00006.txt","r")

# part 2 of the assignment 
## all rows is everything in one list
all_rows = george_data.readlines() # Return all lines in the file, as a list where each line is an item in the list object
george_data.close()
#print(all_rows)

# reference code from the course wiki page 
matrix = [0]*len(all_rows) # matrix is equal to a list of zeros that has a length of all the rows from the data set

# turning the rows into lists 
## matrix is now a list of lists 
for lidx in range(len(all_rows)):
    matrix[lidx] = all_rows[lidx].split(",") # split the line based on the separation flag
#print(matrix) 
    
# checking number of rows    
num_of_rows = len(matrix)
# print(num_of_rows)
yearH = matrix[0][0]
#print(yearH)

column_one = {}

def extraction(matrix):
    return [year[0] for year in matrix]

print(extraction(matrix))

""" 
messing with panda and data frames

https://thispointer.com/python-pandas-how-to-convert-lists-to-a-dataframe/
https://thispointer.com/select-rows-columns-by-name-or-index-in-dataframe-using-loc-iloc-python-pandas/
https://stackoverflow.com/questions/53414960/how-do-i-create-a-sum-row-and-sum-column-in-pandas

"""
test = pandas.DataFrame(matrix, columns = ['Year', 'Day', 'Time', 'George #', ' X', ' Y', ' Asleep', 'Behavior Mode', 'Energy Level', 'Risk', 'ProbFoodCap', 'MVL', 'MSL', 'PercptionDist', 'Percent Step'])
#test = pandas.DataFrame(matrix)
#print(test)

yeardata = test.loc[1:14,'Year']
#print(yeardata)
#print(yeardata.to_string(index = False))