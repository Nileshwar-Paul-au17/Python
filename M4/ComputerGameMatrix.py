"""
You are given a rectangular grid of 2 rows and N columns.
You starts in cell (1,1) — at the intersection of the 1st row and the 1st column.
Each cell of the grid is either 0 or 1.
You can move from one cell to another in one step if the cells are adjacent by side and/or corner.
Formally, it is possible to move from cell (x1,y1) to cell (x2,y2) in one step if |x1−x2|≤1 and |y1−y2|≤1.
It is prohibited to go outside the grid.
Cells with 1 in it cannot be visited.

Return if it is possible to reach the cell (2,N).

Input Format

The first line contains a single integer N — the number of columns.
The next two lines describe the grid. The i-th of these lines describes the i-th line of the grid — the line consists of the characters '0' and '1'. The character '0' corresponds to a safe cell, the character '1' corresponds to a trap cell(cell which cannot be visited).
Constraints

N<=100
Additional constraint on the input: cells (1,1) and (2,n) are safe.
Output Format

Output YES if it is possible to reach the target cell, and NO otherwise.

Sample Input 0

3
000
000
Sample Output 0

YES
Explanation 0

One of the possible paths is (1,1)→(2,2)→(2,3).

Sample Input 1

4
0011
1100
Sample Output 1

YES
Explanation 1

one of the possible paths is (1,1)→(1,2)→(2,3)→(2,4).

Sample Input 2

4
0111
1110
Sample Output 2

NO
"""
"""
n = int(input())
r1 = list(input())
r2 = list(input())
"""

r1=['0','0','1','1','1']
r2=['1','1','0','0','0']
n=len(r1)

for i in range(1, n):
    print(f'i={i}')
    if r1[i] == '0':
        #print(r1[i-1],r2[i-1])
        if r1[i-1] == '1' and r2[i-1] == '1':
            r1[i] = '1'
            print(r1[i])
    if r2[i] == '0':
        #print(r1[i-1],r2[i-1])
        if r1[i-1] =='1' and r2[i-1] == '1':
            r2[i] = '1'
            print(r1[i])
print(r1,r2,i)
if r2[i] == '1':
    print('NO')
else:
    print('YES')