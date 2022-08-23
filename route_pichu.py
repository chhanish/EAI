#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [Hanish Chidipothu   hachid@iu.edu]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:   #"r" for reading the file
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:] #rstrip removes all specified characters from string
            
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1)) #possible moves for a particular node
        #print("possible moves are for :{},{}".format(row,col)) #to print possible moves for the node in a fringe
        #print( [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ])
        #print("----------") # sepreting the particular print statement from others for better understanding
        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
def solution_trace(path1): # defining a function to assign the "UDRL" paths
        path1=list(reversed(path1)) # since the dict we created is showing a revesed path from goal state . we print the solution in reverse for correct answer
        solution1=""
        for i in range(len(path1)-1):
                if path1[i][1]==path1[i+1][1]:
                        if path1[i][0]>path1[i+1][0]:
                                solution1=solution1+'U'
                        else:
                                solution1+='D'
                if path1[i][0]==path1[i+1][0]:
                        if path1[i][1]>path1[i+1][1]:
                                solution1+="L"
                        else:
                                solution1+="R"
        return solution1


def search(house_map):
       
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0)]
        #print(fringe) # to better understand whats the intial location
        #print(pichu_loc) #finding the intial location of pichu (5,0)
        
        visited_list = [] # creating a  visited list 
        path={} # creating a dict to store node pattern  with using key and value method
        
        while fringe:
                #print(fringe) #trying to print fringe again for understanding the process here
                (curr_move, curr_dist)=fringe.pop(0)

                visited_list.append(curr_move) # every current move which is popped out of fringe is added to the visited list
                
                for move in moves(house_map, *curr_move):
                      
                        if house_map[move[0]][move[1]]=="@": 
                                visited_list.append(move) #to add the final (5,6) into the visited_list  
                                path[move]=curr_move # creating a key and value such that each node will be assigned to its previous node
                                #print(" visited list: {}".format(visited_list))
                                #print(path)
                                tup = ((move[0],move[1]))
                                path1=[] # to creating a list of nodes in the optimal path
                                path1.append(move)
                                while True:
                                
                                        tup = path[tup]
                                        
                                        #print(path[tup])
                                        path1.append(tup)
                                        #print(path1)
                                        
                                        
                                        
                                        if tup == pichu_loc: #end when reached the intial pichu location
                                                break
                                
                                return (curr_dist+1,solution_trace(path1))  


                             
                        else:
                                if move not in visited_list: 
                                        path[move]=curr_move
                                        fringe.append((move,curr_dist+1))
                


# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
       # print(solution)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1]) #printing the answer

