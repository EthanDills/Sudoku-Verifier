'''
for given array A of size n, determine whether there are any duplicate values in the array
'''

# Input array
A = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

# Compute ( determine existence of duplicate )
    ## could stop at any point
    #  let int k=0 s.t. A[k] is compared to every value in A[k+1...n-1], 
    #  and when A[k] doesn't equal any value in A[k+1...n-1]
    #  k advances by 1 until k equals n-1. ##
k = 0
j = k+1
while(k < len(A)-1): # compare duplicates after A[k] (nothing after A[n-1], so only have to stop at A[n-2])
    
    while(j < len(A) and A[k] != A[j]): # compare each value between A[k+1] to A[n-1]
        j += 1
        # print("A[" + k.__str__() + "] doesn't equal A[" + j.__str__() + "]")

    if(j <= len(A)-1): # if j doesn't equal n-1, then we found a duplicate
        print("A[" + k.__str__() + "] equals A[" + j.__str__() + "]")
        break
    else:
        for i in range(k, j): # for visualization of how the max # of comparisons is (n^2 - 2)/2
            print(A[i], end=" ")
        print()
        k += 1
        j = k+1

# Output whether there are duplicates or not
if(k == len(A)-1): # if k reaches n-1, then we found no duplicates
    print('no duplicates found')
else:
    print('at least one duplicate in the array')