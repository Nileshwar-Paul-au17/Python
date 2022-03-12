'''
You are given an integer array A of size N and an integer K.
Append K unique positive integers that do not appear in A at the end of A such that the resulting total sum of all elements of A is minimum.

Return the sum of the K integers appended to A.

Input Format

First line of input contains a single integer N (size of array A)
Second line of input contains N space seperated integers (elements of the array A).
Constraints

1 <= A.length <= 105
1 <= A[i] <= 109
1 <= k <= 108
Output Format

Print a single integer i.e the minimum sum

Sample Input 0

5 2
1 4 25 10 25
Sample Output 0

5
Explanation 0

The two unique positive integers that do not appear in nums which we append are 2 and 3. The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum. The sum of the two integers appended is 2 + 3 = 5, so we return 5.
'''
def fun():
    return 0