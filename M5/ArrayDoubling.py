'''' 
There is an integer array A of size N satisfying two properties:

Every element of A is unique
Elements of A are sorted in increasing order
A is transformed into an array B by appending twice the value of every element in A, and then randomly shuffling the array B.
For example , if A=[1,2,3] , then we will append 2, 4 , 6 into array A which results in [1,2,3,2,4,6] and then we can shuffle this array randomly to obtain array B.

You have lost the array A and you have only array B now. Recover array A from array B. Print array A in increasing order and there shouldn't be any duplicate in A.

Input Format

First line of input contains two integers 2* N. (Length of the array B)
Second line of input contains 2* N space seperated integers( Elements of the array B)
Constraints

2 <= 2 * N <=100000
It is guaranteed that valid array B exists so that there is unique Array A corresponding to given array B
Output Format

Print N seperated integers on single line

Sample Input 0

6
1 3 4 2 6 8
Sample Output 0

1 3 4
Explanation 0

Array A could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.

Sample Input 1

4
0 0 0 0
Sample Output 1

0 0 
'''
def arrayA(arrB):
        dicti = {}
        ans = []
        arrB.sort()
        for n in arrB:
            if (n//2, n) in dicti:
                if dicti[(n//2, n)] > 1:
                    dicti[(n//2, n)]-=1
                    ans.append(n//2)
                else:
                    dicti.pop((n//2, n))
                    ans.append(n//2)
            else:
                dicti[(n, n*2)] = dicti.get((n, n*2), 0) + 1
        if dicti:
            return []
        else:
            return ans

n = int(input())
arrB = list(map(int,input().split()))
arrA = arrayA(arrB)
for i in arrA:
    print(i,end=" ")