''' Outputs whether a sudoku map of 9 by 9 is valid'''

# Input
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
expected_total = (n*(n+1))/2 # closed form solution to 1 + 2 + 3 .... + n

# Compute
'''If there's a repeat in a column, row, or box, then it isn't valid'''

'''each column, row, and 'box' must add up to expected_total'''

''' Loop through each row, and check that it adds up to total. 
    If it doesn't add up to total, output such. Repeat with columns and boxes.
    - Rows: Iteration, Case Analysis
    - Columns: Iteration, Case Analysis
    - Boxes: Iteration, Case Analysis
    '''



''' Let i = 0 such that i < n, where i represents the current row in a 2D array. Let row_total equal 
    the sum of all elements in the current row, and compare it to expected_total'''
row_total = expected_total # initialized as a valid value to pass the condition on the first iteration
i = 0
while (i < n and row_total == expected_total): 
    
    # loop through the ENTIRE current row, and add up each element of the row
    row_total = 0
    for j in range(len(sudoku[i])):
        row_total += sudoku[i][j]
    i += 1
        
    
    # Check each column
    # Check each box (change of coordinate systems)


if(i < n-1):
    print("not valid")
else:
    print("valid so far")
# Output
# if (is_valid):
#     print("valid")
# else:
#     print("not valid")