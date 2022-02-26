''' 
You are given two arrays A and B of size N.
A[i] represents the ith show name and B[i] represents the number of people who watched ith show.

Print the K Most watched show.
Print show names in lexicographical order.

NOTE:

It is guaranteed that all elements of array A and B are unique
Input Format

First line of input contains two integers N and K.
Second line of input contains N space seperated integers (elements of array A).
Third line of input contains N space seperated integers (elements of array B).
Constraints

1 <= N <=1000
Output Format

Print show names in lexicographical order

Sample Input 0

5 2
topgun aviator top roma logan
5 3 4 2 6
Sample Output 0

logan topgun

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