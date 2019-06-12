import numpy as np
# define GLOBAL variables
employee = []                               # array of employees 1
arrEmployee = []                            # array of employees 2
optionalKitchenLocationIndex = []           # indexes of optional kitchen location on floor map
floor_map = []

# ----------------------------------------------- INPUT-1
# floor_map = [['W','W','W','W','W','W'],
#             ['W','E',' ','W',' ','W'],
#             ['W',' ',' ','W','E','W'],
#             ['W','W','W','W','W','W']]
# ----------------------------------------------- INPUT-2
# floor_map = [['W','W','W','W','W','W','W','W'],
#        ['W',' ',' ',' ',' ',' ',' ','W'],
#        ['W','E',' ',' ',' ',' ',' ','W'],
#        ['W',' ',' ',' ',' ',' ',' ','W'],
#        ['W',' ',' ',' ',' ',' ','E','W'],
#        ['W','E',' ',' ',' ',' ',' ','W'],
#        ['W','W','W','W','W','W','W','W']]
# ----------------------------------------------- INPUT-3
floor_map = [['W','W','W','W','W','W','W','W','W','W','W','W','W'],
        ['W','E',' ',' ',' ',' ','W','E',' ',' ',' ',' ','W'],
        ['W',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ','W'],
        ['W',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','W'],
        ['W',' ',' ',' ',' ',' ','W',' ',' ',' ',' ',' ','W'],
        ['W','E',' ',' ',' ',' ','W','E',' ',' ',' ',' ','W'],
        ['W','W','W','W','W','W','W','W','W','W','W','W','W']]
        
def main():                                 # Define the main function
    
    if len(floor_map)==0:
        print("Floor map is empty....!")
    else:
        print("explanation of the map:  W - wall   /  E - employee  /  ' ' - empty space   /   X - best empty space to put a kitchen ")
        
main()  # call to main function