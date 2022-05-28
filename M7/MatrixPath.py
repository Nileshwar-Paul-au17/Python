'''
Consider an N×N grid. Rows of the grid are numbered from 1 to N and columns are also numbered from 1 to N.
Cell present at row i and column j is denoted by ( i , j ).
Top left cell is ( 1 , 1 ) and bottom most cell is ( N , N ).
Some cells are blocked and some cells are empty. if cell ( i , j ) contains " * ", then it is blocked and you cannot move into that cell. If the cell is empty then cell ( i , j ) will be ".".

Your task is to calculate the number of paths from the upper-left square to the lower-right square such that no path crosses through any blocked cell.
You only can move right or down.
Print the number of paths modulo 109+7.
In othe words, if number of paths is K (could be a very large integer), print k%M where M=1000000007.

Input Format

The first input line has an integer N: the size of the grid.

After this, there are N lines that describe the grid. Each line has N characters: "." denotes an empty cell, and " * " denotes a trap.

Constraints

1 <= N <=1000
Output Format

Print the number of paths modulo 109+7.

Sample Input 0

4
....
.*..
...*
*...
Sample Output 0

3
Sample Input 1

3
*..
...
..*
Sample Output 1

0
Explanation 1

Since , the top left cell is blocked , Number of paths from (1,1) to (N,N) will be zero
'''
def number_of_paths(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[n - 1][m - 1] % 1000000007

n = int(input())
grid = []
for i in range(n):
    grid.append(input())
print(number_of_paths(grid))