matrix = [
    [3, 5, 6],
    [8, 5, 4],
    [10, 6, 8]
]

# left diagonal
# (0,0) (1,1) (2,2)
# (0,0) .... (m-1,n-1)

# right diagonal
# (0,2) , ( 1,1) , (2,0)
# 0m-1, 1,m-2 ,2m-3
#m = 3 n = 3

def find_all_diagonal_sums(matrixs):

    left_diagonal_sum = 0
    right_diagonal_sum = 0
    max_c = len(matrixs)

    for i in range(0,max_c):
        left_diagonal_sum = left_diagonal_sum + matrixs[i][i]
        right_diagonal_sum = right_diagonal_sum + matrixs[i][(max_c-1)-i]

    return left_diagonal_sum,right_diagonal_sum

print(find_all_diagonal_sums(matrixs=matrix))