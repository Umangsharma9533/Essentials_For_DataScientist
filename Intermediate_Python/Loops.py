#============================================================
#While Loops
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
      offset-=1
    else : 
      offset+=1    
    print(offset)
    
#==============================================================================
#For Loops
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
# i will iterate through the above list one by one and print each element of the list
for i in areas:
    print(i)
#===============================================================================
#When we want to print both index and value of the list we can use enumerate()
# Change for loop to use enumerate() and update print()
for a ,b in enumerate(areas) :
    print("room "+ str(a)+": "+ str(b))
#===============================================================================
#if we want to print index starting from 1
# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
    
#==============================================================================
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for lis in house:
    print("the "+lis[0]+" is "+str(lis[1])+" sqm")
#==================================================================================
#for loop for dictionary in this we use item method to seperate key and value pair
#the order in whiuch this will pick key value pair will be random
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, val in europe.items():
    print("the capital of "+str(key)+" is "+str(val))
#=================================================================================# Import numpy as np
#use nditer() function to iterate over nd array
import numpy as np

# For loop over np_height
for x in np_height:
    print(str(x)+" inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(str(x))
