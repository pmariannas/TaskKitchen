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
<<<<<<< HEAD
    
=======
# function init employee steps in matrix based on bfs algorithm. return: floor map with steps
def init_weight(floor_map, curr_loc_x, curr_loc_y, arr):
   while(arr):
        value = floor_map[curr_loc_x][curr_loc_y]
        if value=='E':
            value = 0
        # check all steps around
        if floor_map[curr_loc_x][curr_loc_y+1]!= 'W':
            if floor_map[curr_loc_x][curr_loc_y+1]!='E':
                if floor_map[curr_loc_x][curr_loc_y+1]==0:
                    arr.append([curr_loc_x,curr_loc_y+1])
                    floor_map[curr_loc_x][curr_loc_y + 1] += value + 1
        if floor_map[curr_loc_x+1][curr_loc_y] != 'W':
            if floor_map[curr_loc_x+1][curr_loc_y] != 'E':
                if floor_map[curr_loc_x+1][curr_loc_y] == 0:
                    arr.append([curr_loc_x+1,curr_loc_y])
                    floor_map[curr_loc_x+1][curr_loc_y] +=value + 1
        if floor_map[curr_loc_x-1][curr_loc_y] != 'W':
            if floor_map[curr_loc_x-1][curr_loc_y] != 'E':
                if floor_map[curr_loc_x-1][curr_loc_y] == 0:
                    arr.append([curr_loc_x-1,curr_loc_y])
                    floor_map[curr_loc_x-1][curr_loc_y] += value + 1
        if floor_map[curr_loc_x][curr_loc_y - 1] != 'W':
            if floor_map[curr_loc_x][curr_loc_y - 1] != 'E':
                if floor_map[curr_loc_x][curr_loc_y - 1] == 0:
                    arr.append([curr_loc_x,curr_loc_y - 1])
                    floor_map[curr_loc_x][curr_loc_y - 1] += value + 1

        if len(arrEmployee)==0:
            return floor_map
        else:
            del arrEmployee[0]
            if len(arrEmployee)!=0:
                curr_loc_x =arrEmployee[0][0]
                curr_loc_y =arrEmployee[0][1]
            else:
                return floor_map
# function copy matrix. return: matrix
def copyMatrix(matrix):
    newMatrix=[]
    for i in range(len(matrix)):
        newMatrix.append([])
        for j in range(len(matrix[i])):
            newMatrix[i].append(matrix[i][j])
    return newMatrix
>>>>>>> 9af0cf9... create function-copy matrix
    
    
def main():                                 # Define the main function
    
    if len(floor_map)==0:
        print("Floor map is empty....!")
    else:
        print("explanation of the map:  W - wall   /  E - employee  /  ' ' - empty space   /   X - best empty space to put a kitchen ")
        
main()  # call to main function