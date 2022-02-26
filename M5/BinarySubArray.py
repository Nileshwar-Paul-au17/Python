''' 
You are given an array A of size N consisting of only 0s and 1s.
A subarray is called beautiful is and only if all elements of the subarray is 1.
You are also given an integer M.
You can change atmost M zeros of the array to 1.
Find the maximum possible length of beautiful subarray that can be formed by atmost M operations.

Input Format

First line of input contains two integers N and M. (Length of the array and maximum number of operations)
Second line of input contains N space seperated integers( Element of the array)
Constraints

1<= N <=100000
Output Format

Print a single integer in one line

Sample Input 0

7 1
1 0 0 1 1 0 1
Sample Output 0

4
Explanation 0

Explanation : Here, we should only change 1 zero(0).
Maximum possible length we can get is 4 by changing the 3rd zero in the array
The new array will be A[] = {1, 0, 0, 1, 1, 1, 1}
'''
def longestSubSeg(a, n, k):
 
    cnt0 = 0
    l = 0
    max_len = 0

    for i in range(0, n):
        if a[i] == 0:
            cnt0 += 1

        while (cnt0 > k):
            if a[l] == 0:
                cnt0 -= 1
            l += 1
        
        max_len = max(max_len, i - l + 1);
   
    return max_len

n, k = [int(x) for x in input().split()]
a = list(map(int,input().strip().split()))
print(longestSubSeg(a, n, k))