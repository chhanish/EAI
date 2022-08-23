# a0

Question 1: 
AIM:  
To write a program to find the shortest path between the agent and the goal position in the form of string of letters (L, R, U, D for left, right, up and down). 
ABSTRACT: 
INITIAL STATE:  It is the location of the “Pichu” in the given map. 
GOAL STATE:  To search until the agent reach the goal state ‘@’. 
SUCCESSOR MOVES:  The possible moves for a particular node(L,R,U, D) in which the agent (‘p’) currently exists. 
SOLUTION TRACE:  To trace the path of the agent after it reaches the goal position. 
COST FUNCTION:  we assume the cost function to be a unit (‘1’) for every move. 
CONDITIONS: 
To assume there are only one ‘p’ & one ‘@’. Also, a condition is already written such that ‘p’ only moves to the ‘.@’ locations avoiding the ‘x’ (obstacle node position).  
PROCEDURE: 
Initially I have studied the code and have understood that the agent is going into the infinite loop. 
Then I have figured out the position of nodes because of which the loop is going infinite.  
After which I have decided to create a visited list to add the all the nodes of the fringe which have been popped out to the current move every time. 
Using this visited list I have created an if condition in the search condition before appending the successor move to the fringe. So that if the next move already exists in the visited list, then it won’t append the particular node to the fringe which in turn stops the infinite loop. 
 
 
 
 
After stopping the infinite loop, in order to find the path, I have created a dictionary called ‘path’ in which I have used the key & value concept such that for a node as a key its previous node from which it has come is initiated as value. 
 After which I have created another list called ’path1’ to which I added the initial node as the goal position and appended the previous node of the goal position from the dictionary created ‘path’ to the variable ‘tup’ and appending ‘tup’ again to the ‘path1’. similarly for the last node appended in ‘path1’ finding its previous node from the dictionary, this continuous as a loop until it reaches the initial agent position. 
Printing the ‘path1’ we get the optimal path of the agent in reverse direction which is from goal position to initial position. 
In order to print the optimal path in the form of string letters (U, L, R, D directions) I have defined a function called solution trace in which I have given the ‘path1’ list in reversed order. 
Using the row and column positions in the map I have created the logic using for loops and assign the directions to be printed for that particular logic. 
Finally, the solution with the optimal path is printed in the form of (U,D,R,L) along with the current position.  
 
 
 
 
 
 
 
 
 
 
 
Question 2: 
AIM: 
To write a program to find out the positions in which ‘k’ agents can be placed under the condition that no agent can see one another. The agents can be on the same row when the view is obscure with a wall in between. 
ABSTRACT: 
INITIAL STATE:  It is the location of the first “Pichu” in the given map. 
GOAL STATE:  To place the ‘k ‘agents in the map by satisfying the given conditions. 
SUCCESSOR MOVES:  To place the current agent with respect to the previously placed agents such that the given condition is satisfied. 
SOLUTION TRACE:  To find the correct positions to place the ‘k’ agents optimally. 
COST FUNCTION:  we assume the cost function to be a unit (‘1’) for every move. 
PROCEDURE: 
Initially I have studied the code and have understood that I need to write a logic to satisfy the conditions given. 
I have defined two functions possible check and cross check to write the logic to check the vertical, horizontal and diagonal next nodes of a particular node. If the condition is satisfied then place the agent in the particular node position. 
In the possible check function, we need to check the horizontal and vertical next position of a particular node.   
 
 
 
           
For this we can apply the logic with the help of row and column position. As each node is assumed to be at the position (row, Col) in the map. For example, to check the right position of a particular node we increment col position by 1 (col+1) and keep the row number same which takes us to the next node in the row. Similar logic is applied to check horizontal, vertical next nodes of a node by making changes to the (row, Col) either incrementing or decrementing by one. 
The logic is written with the if conditions to check if the next positions equal to the “x” or ‘p’ such that if the next position has a wall, then place the agent, if else a ‘p’ is there then we should write False as placing agent would result in seeing each other, which leads to dissatisfying the condition. 
Similarly, a cross check function is defined to check the diagonal next positions of a particular node. In this to get the position of the node which is diagonal to a particular. We make changes both to the row and col. For example, if we have to get to the right up diagonal position of a particular node, we decrement the row by one and increment the col by one (row-1, col+1). Similarly, to get to the other diagonal positions of a particular node we either increment or decrement the (row, col) individually. 
Similar to as possible check we check if the diagonal positions are equal to ‘x’ or ‘p’ and place agent according to the condition. 
I have defined another function called correct position in order to define the condition for both checks when false in which I have written an if condition such that if the above checks are false then return false. 
Finally, I have added the correct position function inside the successors function with an ‘and’ condition so that it works only if both the conditions of and are satisfied. 
Finally, when the ‘k’ agents are given as input they are placed in the map satisfying the given conditions. 
 
 
 
 
       
 
 
 
 
