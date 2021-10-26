"""
You are given two Sorted arrays A and B of size N and M respectively.
For each element of the second array, find the number of elements in the first array strictly less than it.

Input Format

The first line contains integers N and M, the sizes of the arrays.
The second line contains N integers A[i], elements of the first array.
The third line contains M integers B[i] , elements of the second array.
Constraints

1<= N,M <=106
-109 <= A[i],B[i] <= 109
Output Format

Print M numbers, the number of elements of the first array less than each of the elements of the second array.

Sample Input 0

6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
Sample Output 0

1 1 2 3 4 6 6 
Explanation 0

First element of the second array is 2. There is only 1 element in 1st array less than 2.
Second element of the second array is 3. There is only 1 element in 1st array less than 3.
Third element of the second array is 8. There are 2 elements in 1st array less than 8.
Fourth element of the second array is 13. There are 3 elements in 1st array less than 13.
Fifth element of the second array is 15. There are 4 elements in 1st array less than 15.
Sixth element of the second array is 21. There are 6 elements in 1st array less than 21.
Seventh element of the second array is 25. There are 6 elements in 1st array less than 25.
"""

def check(a,b,n,m):
    
    max1=max(n,m)
    min1=min(n,m)
    outpt=[0]*max1
    
    for i in range(0,max1):
        
        for j in range(0,min1):
            
            if b[i] > a[j]:
                outpt[i]+=1
        
    
    
    print(" ".join(str(x) for x in outpt))


ints=list(map(int,input().split()))
n=ints[0]
m=ints[1]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
check(a,b,n,m)