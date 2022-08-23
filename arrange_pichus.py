#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

def possible_check(house_map,row,col): #defining a function to check positions of up,down,left, right of a node
    column_up_flg = True
    column_down_flg = True
    row_right_flg= True
    row_left_flg=True
    for i in range(row-1,-1,-1): # to check the column up position
        if house_map[i][col]=='X':
            break
        
        if house_map[i][col]=='p':
            column_up_flg = False

    for i in range(row+1,len(house_map)): # to check the column dowm postion
        if house_map[i][col]=='X':
            break
        
        if house_map[i][col]=='p':
            column_down_flg = False
            break
    
    for i in range(col+1,len(house_map[0])): #to check the row right position
        if house_map[row][i]=='X':
            
            break
        
        if house_map[row][i]=='p':
            row_right_flg = False
            break


    for i in range(col-1,-1,-1):# to check the row left side position
        if house_map[row][i]=='X':
            
            break
        
        if house_map[row][i]=='p':
            row_left_flg=False
            break
    
    return column_up_flg and column_down_flg  and row_right_flg and row_left_flg

def cross_check(house_map,row,col): # defining an other function for diagonal position check for a node:
    
    # right_down_flg = True
    # right_up_flg = True
    # left_up_flg= True
    # left_down_flg=True
    # defining another functions seperately for each diagonal position checks
    def right_down(house_map,row,col): 
        right_down_flg = True
        i=row+1
        j=col+1 #to check right down diagonal position
        while i<len(house_map) and j<len(house_map[0]): 
        
            if house_map[i][j]=='X':
                right_down_flg = True
                break
        
            if house_map[i][j]=='p':
                right_down_flg =False
                break               
            j=j+1
            i=i+1
        return right_down_flg
    right_down_flg = right_down(house_map,row,col)
    
        
    def right_up(house_map,row,col):
        right_up_flg = True
        i=row-1
        j=col+1 #to check right up diagonal position
        while  i>=0 and j<len(house_map[0]):
            if house_map[i][j]=='X':
                right_up_flg = True
                break
        
            if house_map[i][j]=='p':
                right_up_flg = False
                break
            i-=1
            j+=1
        return right_up_flg
    
    right_up_flg = right_up(house_map,row,col)

    def left_up(house_map,row,col):
        left_up_flg = True
        i=row-1
        j=col-1 # to check left up diagonal position
        while i>=0 and j >=0: 
            if house_map[i][j]=='X':
                left_up_flg= True
                break
        
            if house_map[i][j]=='p':
                left_up_flg= False
                break
            j=j-1
            i=i-1
        return left_up_flg

    left_up_flg = left_up(house_map,row,col)

    def left_down(house_map,row,col):
        left_down_flg = True
        i=row+1
        j=col-1 #to check left down diaonal postion
        while i<len(house_map) and j >=0: 
        
            if house_map[i][j]=="X":
                left_down_flg=True
                break
        
            if house_map[i][j]=='p':
                left_down_flg= False
                break    
        
            j=j-1
            i=i+1
        return left_down_flg

    left_down_flg = left_down(house_map,row,col)

    return right_down_flg  and right_up_flg and left_up_flg and left_down_flg
def correct_position(house_map,r,c): # defining a function to return false, if the possible_checks & cross_check are false
    row_col_check=  possible_check(house_map,r,c)     
    if   row_col_check==False:
        return False
    diagonal_check=cross_check(house_map,r,c) 
    if  diagonal_check==False:
        return False
    return True
# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    print(house_map)
    return "\n".join(["".join(row) for row in house_map])# to print house_map


# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):

    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' and  correct_position(house_map,r,c)] #also including the check methods

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
    return(initial_house_map,False)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")
