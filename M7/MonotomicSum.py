'''
You are given an array A of size N consiting of N positive integers.
A subarray is called monotonic if every element of the subarray is strictly greater than the the previous(immediate left) element.
In other words, a subarray [ A[i] , A[i+1] , ... , A[j] ] is monotonic if for all k where i < k <= j, A[k] >A[k-1]. Note that a subarray of size 1 is monotonic.

Find the largest possible sum of a monotonic subarray.

A subarray is defined as a contiguous sequence of numbers in an array.

Expected Complexity: O(n)
Input Format

The first input line has one integers N (Number of elements of the array)
The next line has N space seperated integers i,e A[0],A[1] ,… ,A[N-1]
Constraints

1 <= A.length <= 100
1 <= A[i] <= 100
Output Format

Print a single integer in one line

Sample Input 0

6
10 20 30 5 10 50
Sample Output 0

65
Explanation 0

[5,10,50] is the monotonic subarray with the maximum sum of 65.
'''
def checn(list1, n):
    sum1=list1[0]
    sum2=list1[0]
    for i in range(1, n):
        if (list1[i-1] < list1[i]):
            sum1= sum1+ list1[i]
            sum2= max(sum2,sum1)
        else:
            
            sum1= list1[i]
    return max(sum2,sum1)

n = int(input())
list1 = list(map(int, input().split()))
n = len(list1)
print(checn(list1, n))