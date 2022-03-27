'''
You are given an array A of size N where A[i] represents the score of the ith student. You are also given an integer K.

A set containing K students is called a K-set. Absolute difference between maximum score and minimum score of a K-set(set containing K students) is called K-Score.

Return the minimum possible value of K-Score.

Input Format

First line of input contains two integers , N and K.
Second line of input contains N space seperated integers (Scores of N students).
Constraints

N<=1000000
K < = N
A[i] <=100000
Output Format

Print a single integer

Sample Input 0

4 2
9 4 1 7
Sample Output 0

2
Explanation 0

There are six ways to pick score(s) of two students:

[9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
[9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
[9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
[9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
[9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
[9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.


***********************////////\\\\\\\\\***********************************

Refrence:-https://www.geeksforgeeks.org/k-numbers-difference-maximum-minimum-k-number-minimized/

'''
'''
n, k = input().split()
N = 4
K = 2

arr = [9,4,1,7]

def minimumDiff( nums, k):

    nums = sorted(nums)
    res = nums[k-1] - nums[0]

    for i in range(k, len(nums)):
        res = min(res, nums[i] - nums[i - k + 1])
        print(res)

    return res

    


print(minimumDiff(arr,K))
'''
def minDiff(arr,n,k):
    result = +2147483647
  
    # Sorting the array.
    arr.sort()
  
    # Find minimum value among
    # all K size subarray.
    for i in range(n-k+1):
        result = int(min(result, arr[i+k-1] - arr[i]))
  
    return result
 
# Driver code
 
arr= [10, 100, 300, 200, 1000, 20, 30]
n =len(arr)
k = 3
  
print(minDiff(arr, n, k))