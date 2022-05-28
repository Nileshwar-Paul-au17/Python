'''
You are given an N x N integer matrix.
You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1. Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Input Format

First Line of input contains integer N(size of the matrix).
Next N lines contains N integers echh(elements of the matrix).
Constraints

N == matrix.length == matrix[i].length 2 <= N <= 250 -100000 <= matrix[i][j] <= 100000

Output Format

Print a single integer.

Sample Input 0

2 
1 -1
-1 1
Sample Output 0

4
Explanation 0

We can follow the following steps to reach sum equals 4:

Multiply the 2 elements in the first row by -1.
Multiply the 2 elements in the first column by -1.
Sample Input 1

3
1 2 3
-1 -2 -3
1 2 3
Sample Output 1

16
Explanation 1

We can follow the following step to reach sum equals 16: - Multiply the 2 last elements in the second row by -1.
'''
n=int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

tot_sum = 0
neg_nums, min_val = 0, float('inf')
for row in matrix:
    for col_val in row:
        tot_sum += abs(col_val)
        min_val = min(min_val, abs(col_val))
        if col_val < 0:
            neg_nums += 1
if neg_nums % 2 == 0:
    print(tot_sum)
else:
    print(tot_sum - 2*min_val)