'''
You are given a binary array A and an integer K.
Print "YES" if all 1's are at least K places away from each other, otherwise Print "NO".

Input Format

First line of input contains two integers N and K.
Second line of input contains N space seperated integers (Elements of array A).
Constraints

1 <= A.length <= 100000
0 <= K <= A.length
A[i] is 0 or 1
Output Format

Print "YES" or "NO"

Sample Input 0

8 2
1 0 0 0 1 0 0 1 
Sample Output 0

YES
Explanation 0

Each of the 1s are at least 2 places away from each other.

Sample Input 1

6 2
1 0 0 1 0 1
Sample Output 1

NO
'''
def check(list, k):
    p = 0
    c = 0    
    while (p < len(list) and list[p] == 0):
        p += 1
    for i in range(p + 1, len(list)):
        if list[i] == 0:
            c += 1
        else :
            if c < k:
                return "NO"
            c = 0
    return "YES"

N,K= list(map(int, input().split()))[:2]
list = list(map(int,input().split()))[:N] 
print(check(list, K))