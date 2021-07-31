''' Outputs whether a sudoku map of 9 by 9 is valid'''

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
n = 9 # length (and width) of the sudoku map. Should be a perfect square number
print("something")
print(len(sudoku))
# Compute
'''If there's a repeat in a column, row, or box, then it isn't valid'''

''' Loop through each row, and check for duplicates and that each cell is between 1 and 9.
    If there are duplicates / any cells aren't between 1 and 9, output such.
    - Rows: Iteration, Case Analysis
    - Columns: Iteration, Case Analysis
    - Boxes: Iteration, Case Analysis
    '''
# check rows
    # check duplicates and that each value is between 1 and 9
r = 0 # starting row
c = 0 # starting column
def compute_rows():
    r = 0
    c = 0
    print("compute_rows() called")
    while(r<n and sudoku[r][c] < 10 and sudoku[r][c] > 0): # while we haven't gone off the edge, and each value is between 1 and 9
        c = 0
        j = 1
        while(c < n-1): # compare duplicates after A[k] (nothing after A[n-1], so only have to stop at A[n-2])
            
            while(j < len(sudoku) and sudoku[r][c] != sudoku[r][j]): # compare each value between A[k+1] to A[n-1]
                # print("sudoku[" + r.__str__() + "][" + c.__str__() + "] doesn't equal sudoku[" + r.__str__() + "][" + j.__str__() + "]")
                # print("sudoku[" + r.__str__() + "][" + c.__str__() + "]: " + sudoku[r][c].__str__() )
                # print("sudoku[" + r.__str__() + "][" + j.__str__() + "]: " + sudoku[r][j].__str__() )
                j += 1

            if(j <= len(sudoku)-1): # if j doesn't equal n-1, then we found a duplicate
                # print("sudoku[" + r.__str__() + "][" + c.__str__() + "] equals sudoku[" + r.__str__() + "][" + j.__str__() + "]")
                # print("sudoku[" + r.__str__() + "][" + c.__str__() + "]: " + sudoku[r][c].__str__() )
                # print("sudoku[" + r.__str__() + "][" + j.__str__() + "]: " + sudoku[r][j].__str__() )
                return -1
            else:
                # print("iterating c and j")
                c += 1
                j = c+1
                # print("column: " + c.__str__())
                # print("row: " + r.__str__())
            
        r+=1
    
def compute_columns():
    r = 0
    c = 0
    print("compute_columns called")
    while(c<n and sudoku[r][c] < 10 and sudoku[r][c] > 0): # while we haven't gone off the edge, and each value is between 1 and 9
        r = 0
        j = 1
        while(r < n-1): # compare duplicates after A[k] (nothing after A[n-1], so only have to stop at A[n-2]) 
            while(j < len(sudoku) and sudoku[r][c] != sudoku[j][c]): # compare each value between A[k+1] to A[n-1]
                j += 1
            if(j <= len(sudoku)-1): # if j doesn't equal n-1, then we found a duplicate
                return -1
            else:
                r += 1
                j = r+1
        c+=1
        


if(compute_rows()==-1 or compute_columns()==-1): # if we didn't reach the end, it isn't valid
    print("not valid")
else:
    print("valid so far")



# Output