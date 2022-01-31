'''
You are given an array A of size N consisting of N integers.
A number K of array A is lonely when it appears only once, and no adjacent numbers (i.e. K + 1 and K - 1) exists in the array A.
Return a sorted list of lonely numbers of Array A.

Input Format

First line contains single integer N.
Second line contains N space seperated integers , A[0] ,A[1], A[2]... A[N-1]
Constraints

1<= N <=105
1 <= A[i] <= 106
Output Format

Print Space seperated integers on a single line

Sample Input 0

4
10 6 5 8
Sample Output 0

8 10
Explanation 0

10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
5 is not a lonely number since 6 appears in nums and vice versa. Hence, the lonely numbers in nums are [10, 8]. Note that [8, 10] may also be returned.
Sample Input 1

4
1 3 5 3
Sample Output 1

1 5
Explanation 1

1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
3 is not a lonely number since it appears twice. Hence, the lonely numbers in nums are [1, 5]. Note that [5, 1] may also be returned.
'''
def check(n,nums):
    nums.sort()
    dict={}
    list=[]
    for i in nums:
        if (i in dict):
            dict[i]+=1
        else:
            dict[i]=1
    
    for key,value in dict.items():
        if (value == 1):
            
           
            if(key+1 not in dict):
                
                if(key-1 not in dict):
                    list.append(key)
    return list
                    
            
        
n =int(input())
nums = list(map(int,input().split()))
result = check(n,nums)
print(*result)