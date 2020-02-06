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
from statistics import mean
import math

# part 1 of the assignment 
george_data = open("2008Male00006.txt","r")

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
    
# storing rows as variables
row0 = matrix[0]
row1 = matrix[1]
row15 = matrix[15] # storing the final line as a variable

del matrix[15] # deleting the final line from the matrix so we can work with it 
del matrix[0] # removing the header 

transform_matrix = list(zip(*matrix)) #everything is now a tuple
final_matrix = dict(zip(row0,transform_matrix))

"""
convert tuples to list of the correct type
"""
# turn to float
conv_X = list(final_matrix[" X"]) # space is present or else keyword won't work
float_X = [float(i) for i in conv_X]

conv_Y = list(final_matrix[" Y"]) #space is necessary because original txt has the space 
float_Y = [float(i) for i in conv_Y] 

conv_E = list(final_matrix["Energy Level"])
float_E = [float(i) for i in conv_E]

conv_msl = list(final_matrix["MSL"])
float_msl = [float(i) for i in conv_msl]

conv_mvl = list(final_matrix["MVL"])   
float_mvl = [float(i) for i in conv_mvl]

conv_step = list(final_matrix["Percent Step\n"])   
float_step = [float(i) for i in conv_step]

conv_dist = list(final_matrix["PercptionDist"])
float_dist = [float(i) for i in conv_dist]

conv_cap = list(final_matrix["ProbFoodCap"])
float_cap = [float(i) for i in conv_cap]

conv_risk = list(final_matrix["Risk"])
float_risk = [float(i) for i in conv_risk]

# left as string
conv_day = list(final_matrix["Day"])
conv_asleep = list(final_matrix[" Asleep"])
conv_behave = list(final_matrix["Behavior Mode"]) 
conv_time = list(final_matrix["Time"])
conv_year = list(final_matrix["Year"])

# turn to int
conv_number = list(final_matrix["George #"])
int_num = [int(i) for i in conv_number] 

"""
Convert the lists above to dictionaries
"""
y_dict = {}
y_dict["Y"] = float_Y
day_dict = {}
day_dict["Day"] = conv_day
asleep_dict = {}
asleep_dict["Asleep"] = conv_asleep
x_dict = {}
x_dict["X"] = float_X
behav_dict = {}
behav_dict["Behavior Mode"] = conv_behave
energy_dict = {}
energy_dict["Energy Level"] = float_E
num_dict = {}
num_dict["George #"] = int_num
msl_dict = {}
msl_dict["MSL"] = float_msl
mvl_dict = {}
mvl_dict["MVL"] = float_mvl
step_dict = {}
step_dict["Percent Step"] = float_step
dist_dict = {}
dist_dict["PercptionDist"] = float_dist
cap_dict = {}
cap_dict["ProbFoodCap"] = float_cap
risk_dict = {}
risk_dict["Risk"] = float_risk
time_dict = {}
time_dict["Time"] = conv_time
year_dict = {}
year_dict["Year"] = conv_year


"""
Functions and calculations
"""
# mean calculation
def average_list(val):
    return mean(val)

# sum calculation    
def sum_list(val2):
    return sum(val2)

# distance calculation    
def distance(val3, val4):
    between_points = [0] # set the inital point to zero
    for i in range(1,len(val3)):
        between_points.append(math.sqrt((val3[i]-val3[i-1])**2 + (val4[i]-val4[i-1])**2)) #difference between points for X and Y
    return between_points


# using functions to find values  
average_energy = average_list(float_E)
average_X = average_list(float_X)
average_Y = average_list(float_Y)
movement = distance(float_X, float_Y)
total_traveled = sum_list(movement)


# dictionary compiling
distance_dict = {}
distance_dict["Distance"] = movement
final_dictionary = {**y_dict, **day_dict, **asleep_dict, **x_dict, **behav_dict, **energy_dict,
                    **num_dict, **msl_dict, **mvl_dict, **step_dict, **dist_dict, **cap_dict, 
                    **risk_dict, **time_dict, **year_dict, **distance_dict}

"""
Output the new file
"""
# getting his name from the txt file 
message_split = all_rows[15].split()
name = message_split[0]

out_file = open("kong44_Georges_life.txt","w")
out_file.write(("Raccoon name: < {} >\n").format(name))
out_file.write(("Average location: < {}, {} >\n").format(average_X,average_Y))
out_file.write(("Distance traveled: < {} >\n").format(total_traveled))
out_file.write(("Average energy level: < {} >\n").format(average_energy))
out_file.write(("Raccoon end state: < {} >\n\n").format(all_rows[15]))

out_file.write("Date    Time    X    Y    Asleep    Behavior Mode    Distance Traveled\n")
for i in range(len(final_dictionary['Year'])):
    out_file.write('%s \t %s \t %f \t %f \t %s \t %s \t %f\n' % (final_dictionary['Day'][i], final_dictionary['Time'][i],
    final_dictionary['X'][i], final_dictionary['Y'][i], final_dictionary['Asleep'][i], final_dictionary['Behavior Mode'][i],
    final_dictionary['Distance'][i]))

out_file.close()