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
        
        
        
# function show the plan of kitchen in matrix n*m
def show_map(floor_map):
    print(np.matrix(floor_map))
# function that init matrix n*m ( W==WALL / E==employee / 0==empty space). return: floor map in matrix
def init_wall(floor_map, row, col):
    for i in range(row):
        for j in range(col):
            if floor_map[i][j]=='W':
                # floor_map[i][j] = -1
                continue
            elif floor_map[i][j]=='E':
                employee.append([i,j])
                continue
            else:
                floor_map[i][j] = 0
    return floor_map
    
    
    
def main():                                 # Define the main function
    
    if len(floor_map)==0:
        print("Floor map is empty....!")
    else:
        print("explanation of the map:  W - wall   /  E - employee  /  ' ' - empty space   /   X - best empty space to put a kitchen ")
        
main()  # call to main function