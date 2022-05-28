'''
You are given an array A consisting of N positive integers.
You can shuffle the array A in any way.
After that , you can create a new array B of length N where B[i]=(A[i] + i)%2 , for each i (1 <= i<= N).

Find the maximum possible sum of integers of the array B if you shuffle A optimally.
NOTE:
% represents the modulo operation.

Input Format

The first line of each test case contains an integer N.
The second line of each test case contains N space-separated integers A[1],A[2] ,…, A[N].
Constraints

1 <=T <=10000
1 <=N <=100000
1 <= A[i] <=10000000
Output Format

For each test case, print a single line containing one integer - the maximum sum of integers of the array B.

Sample Input 0

3
1 2 3
Sample Output 0

2
Explanation 0

One of the optimal ways to shuffle the array A is [2,1,3]. Then the array B=[(2+1)%2,(1+2)%2,(3+3)%2]=[1,1,0]. So the sum of integers of array B is 2. This is the maximum possible sum we can achieve

Sample Input 1

3
2 4 5
Sample Output 1

3
'''
import math
def check(n,list1):
    count_odd = 0
    count_even = 0
    for i in list1:
            if i % 2:
                count_odd += 1
            else:
                count_even += 1
    num_odd = math.ceil(n/2)
    num_even = math.floor(n/2)
    return(min(count_odd, num_even) + min(count_even, num_odd))

n = int(input())
list1 = list(map(int, input().split()))
print(check(n,list1))