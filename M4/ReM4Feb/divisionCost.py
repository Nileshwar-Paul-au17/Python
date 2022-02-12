'''
You are given an array A of size N consisting of 0s and 1s only.
A can be divided at index i (where 0 <= i <= n) into two arrays Aleft which will contain all elements from index 0 to index (i-1) and Aright which will contain all elements from index i to index (n-1).

Aleft = A[0 ... i-1]
Aright = A[i ... n-1]
If i == 0, Aleft is empty, while Aright has all the elements of A.
If i == n, Aleft has all the elements of A, while Aright is empty.
The cost of deviding array A at index i is the sum of the number of 0's in Aleft and the number of 1's in Aright.

Return all distinct indices(in sorted order) that have the highest possible division score.

Solve this in O(n) runtime complexity.

Input Format

First line of input contains an integer N(size of the array).
Second line of input contains N space seperated integers(elements of the array)
Constraints

1<= N <= 100000
Output Format

Print a single line consisting of required number of integers seperated by space

Sample Input 0

4
0 0 1 0
Sample Output 0

2 4
Explanation 0

Division at index

0: Aleft is []. Aright is [0,0,1,0]. The score is 0 + 1 = 1.
1: Aleft is [0]. Aright is [0,1,0]. The score is 1 + 1 = 2.
2: Aleft is [0,0]. Aright is [1,0]. The score is 2 + 1 = 3.
3: Aleft is [0,0,1]. Aright is [0]. The score is 2 + 0 = 2.
4: Aleft is [0,0,1,0]. Aright is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3. Note the answer should be in sorted order with no duplicates

Submissions: 2
Max Score: 30
Difficulty: Hard
Rate This Challenge:

    
More
 

'''
