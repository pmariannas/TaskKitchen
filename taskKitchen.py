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
#function sum all steps from all employee to empty space. return: matrix
def sum_value_matrix(matrixA, matrixB):
    newMatrix = []
    for i in range(len(matrixA)):
        newMatrix.append([])
        for j in range(len(matrixA[i])):
            if matrixA[i][j]=='W':
                x = matrixA[i][j]
                newMatrix[i].append(x)
            elif matrixA[i][j]=='E':
                x = matrixA[i][j]
                newMatrix[i].append(x)
            else:
                x = matrixA[i][j]
                y = matrixB[i][j]
                newMatrix[i].append(x+y)
    return newMatrix
# function check the minimal distances from all employees. return: minimal distance
def check_min_sum(matrix):
    answer=2147483647
    for i in range(len(matrix)):
        minValue = min(matrix[i])
        if minValue=='W':
            continue
        elif minValue == 'E':
            continue
        elif minValue == 1:
            continue
        elif minValue == 0:
            continue
        elif minValue >1:
            if minValue<answer:
                answer = minValue
    return answer
# function show optional location of kitchen (size of kitche 1*1)
def optional_location_of_kitchen(distancesArray,floor_map, minDistance):

    for i in range(len(distancesArray)):
        for j in range(len(distancesArray[i])):
            if distancesArray[i][j] == minDistance:
                floor_map[i][j] = 'X'
                optionalKitchenLocationIndex.append((i, j))
            else:
                continue
    return floor_map
def clear_floor_map_from_0():
    for i in range(len(floor_map)):
        for j in range(len(floor_map[i])):
            if floor_map[i][j]==0:
                floor_map[i][j]=' '
    
    
def main():                                 # Define the main function
    
    if len(floor_map)==0:
        print("Floor map is empty....!")
    else:
        print("explanation of the map:  W - wall   /  E - employee  /  ' ' - empty space   /   X - best empty space to put a kitchen ")
        print("Given a building floor map:")
        show_map(floor_map)                                              # call to show_map function
        init_wall(floor_map, len(floor_map), len(floor_map[0]))          # call init_wall() function (row = len(floor_map) , col = len(floor_map[0]))
        distancesArray = copyMatrix(floor_map)                           # copy floor map matrix to new
        # loop -for- that write destination from all employee to empty space on floor and call function that sum all steps
        for k in range(len(employee)):
            curr_loc_x = employee[k][0]
            curr_loc_y = employee[k][1]
            arrEmployee.append(employee[k])
            y = copyMatrix(floor_map)
            init_weight(y, curr_loc_x, curr_loc_y, arrEmployee)     # call to init_weight function
            distancesArray = (sum_value_matrix(distancesArray, y))  # call to sum_value_matrix function
        # loop -for- change type of weight number from str to int
        for i in range(len(distancesArray)):
            for j in range(len(distancesArray[i])):
                if distancesArray[i][j]=='W':
                    continue
                if distancesArray[i][j]=='E':
                    continue
                else:
                    distancesArray[i][j]= int(distancesArray[i][j])

        distance = (check_min_sum(distancesArray))                          # call to check_min_sum function
        optional_location_of_kitchen(distancesArray, floor_map, distance)   # call to optional_location_of_kitchen
        if len(optionalKitchenLocationIndex)>0:
            print("The map of the best empty space to put a kitchen marked with 'X':")
            clear_floor_map_from_0()
            show_map(floor_map)
            print("Indexes of the best empty space to put a kitchen:",optionalKitchenLocationIndex)
        else:
            print("floor plan does not allow some employees to reach some spaces")
            
            
main()  # call to main function