""" 
You are given a Sequence of N integers A1 , A2 , A3 . . . AN.

You can perform the following operation:

Remove the largest and the smallest element from the sequence and add their absolute difference back into the sequence. You can insert anywhere.

You are given Q queries and in each query, you are given an integer K. For each query ,you have to tell sum of all the elements in the array after K operations.
Input Format

First line contains two space-separated integers N and Q, denoting the number of elements in the sequence and number of queries respectively.

Next line contains N space-separated integers denoting elements of the sequence.

Next Q lines contain a single integer K.

Constraints

2 <= N <= 105

1 <= Q <= 105

0 <= A[i] <= 109

0 <= K < N

Output Format

For each task, print answer in a new line.

Sample Input 0

5 2
3 2 1 5 4
1
2
Sample Output 0

13
9
Explanation 0

After 1st operation, the array will become, A = [3,2,4,4]. So, sum of elements = 13.

After 2nd operation, the array will become, A = [3,2,4]. So, sum of elements = 9.
"""

