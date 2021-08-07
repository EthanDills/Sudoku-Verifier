''' Outputs whether a sudoku map of n by n is valid, where n is a perfect square number'''

# Input
'''
baseline_correct =[   [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9],
        ]
'''
from typing import List
from math import sqrt

sudoku =[   [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9],
        ]
n = len(sudoku) # length (and width) of the sudoku map. Should be a perfect square number

# Compute
# check rows, columns, and boxes
    # check duplicates and that each value is between 1 and 9
r = 0 # starting row
c = 0 # starting column
def compute_rows():
    r = 0
    c = 0
    print("compute_rows() called")
    while(r<n and sudoku[r][c] <= n and sudoku[r][c] > 0): # while we haven't gone off the edge, and each value is between 1 and 9
        c = 0
        j = 1
        while(c < n-1): # compare duplicates after A[k] (nothing after A[n-1], so only have to stop at A[n-2])
            while(j < n and sudoku[r][c] != sudoku[r][j]): # compare each value between A[k+1] to A[n-1]
                j += 1
            if(j <= n-1): # if j doesn't equal n-1, then we found a duplicate
                return -1
            else:
                # print("iterating c and j")
                c += 1
                j = c+1
            
        r+=1
    
def compute_columns():
    r = 0
    c = 0
    print("compute_columns() called")
    while(c<n): # while we haven't gone off the edge ( don't need to check if it's between 1 and 9, because we checked for that in compute_rows() )
        r = 0
        j = 1
        while(r < n-1): # compare duplicates after A[k] (nothing after A[n-1], so only have to stop at A[n-2]) 
            while(j < n and sudoku[r][c] != sudoku[j][c]): # compare each value between A[k+1] to A[n-1]
                j += 1
            if(j <= n-1): # if j doesn't equal n-1, then we found a duplicate
                return -1
            else:
                r += 1
                j = r+1
        c+=1
        
def compute_boxes():
    print("compute_boxes() called")

    # there are n boxes
    # need to find duplicates inside the box
    # lower it to a one-dimensional problem (deltaR and deltaC)
    # generate the arrays for deltaR and deltaC depending on n 
        # start in the top right corner of each box
        # 3 * 3 example of how each box is counted for the index of deltaR and deltaC:
        #   [0, 1, 2]
        #   [3, 4, 5]
        #   [6, 7, 8]
        #   deltaR = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        #   deltaC = [0, 1, 2, 0, 1, 2, 0, 1, 2]##
    # generating deltaR based on n:
        # fill out 0 for sqrt(n) times, then go to 1, then 2, etc all the way to sqrt(n)-1

    deltaR = [] # change in rows for each cell within a box
    deltaC = [] # change in columns for each cell within a box
    value = 0 # the value being filled into deltaR and deltaC
    r = 0 # row of current cell
    c = 0 # column of current cell
    inner_count = 0 # which cell inside the current box we're on
    outer_count = 0 # which box we're on
    j = inner_count + 1 
    outer_deltaR = [] # change in rows when we shift to a new box
    outer_deltaC = [] # change in columns when we shift to a new box
    
    # determinant iteration
    for i in range(int(sqrt(n))): # add value to deltaR sqrt(n) times, then increment value by 1 and repeat all of that for a total of sqrt(n) times
        for k in range(int(sqrt(n))):
            deltaR.append(value)
        value += 1
    print(deltaR)
    for i in range(int(sqrt(n))): # (add value to deltaC and increment value) sqrt(n) times, and then repeat all of that for a total of sqrt(n) times
        value = 0
        for k in range(int(sqrt(n))):
            deltaC.append(value)
            value += 1
    print(deltaC)

    # very similar to filling out deltaR[] and deltaC[]
    value = 0 # resetting value after it was used for appending deltaR[] and deltaC[]
    for i in range(int(sqrt(n))):
        for k in range(int(sqrt(n))):
            outer_deltaR.append(value)
        value += int(sqrt(n))
    print(outer_deltaR)
    for i in range(int(sqrt(n))):
        value = 0
        for k in range(int(sqrt(n))):
            outer_deltaC.append(value)
            value += int(sqrt(n))
    print(outer_deltaC)
 
    # implement find duplicate program into sudoku[r+deltaR[count]][c+deltaC[count]]
    while(outer_count < n): # we only need to check n boxes
        while(inner_count < n-1): # each box has n cells, and we start the count at zero
            while(j < n and sudoku[r+deltaR[inner_count]][c+deltaC[inner_count]] != sudoku[r+deltaR[j]][c+deltaC[j]]):
                j += 1
            if(j <= n-1): # if j doesn't equal n-1, then we found a duplicate
                return -1
            else:
                inner_count += 1
                j = inner_count + 1
        outer_count += 1
        if(outer_count < n): # if count equals n, we would get an IndexError (could also use try and except)
            r = outer_deltaR[outer_count]
            c = outer_deltaC[outer_count]


# Output
if(sqrt(n) - int(sqrt(n)) != 0):
    print("n must be a perfect square")
elif(compute_rows()==-1): 
    print("rows not valid")
elif(compute_columns()==-1):
    print("columns not valid")
elif(compute_boxes()==-1):
    print("boxes not valid")
else:
    print("valid so far")