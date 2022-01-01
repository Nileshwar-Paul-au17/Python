"""
You are given an array A of n integers i.e A0 , A1 , A2 , A3 ... An-1.
An index i is called a good index if and only if there exists j such that j > i and A[j] < A[i].
In other words , an index i is a good index if there exists an array element after index i which strictly smaller than the element at index i.
Count the number of good indexes of the array.

Input Format

Each input data set consists of two lines.
The first line contains an integer n (size of the array).
The second line contains n integers A0 , A1 , A2 , A3 ... An-1
Constraints

1 <= N <= 150000
1<= Ai <= 106
Output Format

Print a single integer i.e, the required answer

Sample Input 0

6
3 9 4 6 7 5
Sample Output 0

3
Explanation 0

The array index i=1 (a1 = 9) , i=3(a3=6) , i=4(a4=7) are good indexes
"""


def check(n,list1):
    c=0
    j=n-1
    for i in range(0,n):
        for j in range(n-1,-1,-1):
            if j>i and list1[j]<list1[i]:
                c =c +1
                break      
    return c

#n = int(input())
n=6

#list1 = list(map(int,input().split()))

list1 =[3,9,4,6,7,5]

result = check(n,list1)

print(result)
