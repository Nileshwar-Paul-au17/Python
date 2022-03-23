'''
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

**************/////////////***************************
Refrence:-https://www.geeksforgeeks.org/element-1st-array-count-elements-less-equal-2nd-array/

'''

n, k = input().split()
N = int(n)
K = int(k)

Arr1 = list(map(int,input().split()))[:int(N)]
Arr2 = list(map(int,input().split()))[:int(K)]


def bin_search(Arr, n, x):
    l = 0
    h = n - 1
    while(l <= h):
        mid = int((l + h) // 2)

        if(Arr[mid] < x):
            l = mid + 1
        else:
            h = mid - 1
    return h


def countElements(Arr1, Arr2, m, n):
    Arr2.sort()

    for i in range(m):
        index = bin_search(Arr2, n, Arr1[i])
        print(index + 1,end=" ")
        

m = len(Arr1)
n = len(Arr2)
countElements(Arr2, Arr1, n, m)