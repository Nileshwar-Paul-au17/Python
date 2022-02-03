"""
Given an array A of size N consisting of N integers.
Print "YES" if you can partition the array into two non-empty subarray such that every number in the left subarray is strictly less than every number in the right subarray.

Input Format

First line of input contains integer N (size of the array)
Second line of input contains N space seperated integers (A[0] , A[1] , A[2] ... A[N-1])
Constraints

1 <= N <=100000
1 <= A[i] <=100000
Output Format

Print "YES" or "NO"

Sample Input 0

4
5 3 2 7 9
Sample Output 0

YES
Explanation 0

We can split the list into left = [5, 3, 2] and right = [7, 9] . Every element in left subarray is strictly less than every element in right subarray
"""
import sys

def partitionArray(a, n) :
  Min = [0] * n
  #print(Min)
  Mini = sys.maxsize
  
  for i in range(n - 1, -1, -1):
    print(f'{Mini} ,{a[i]}')
    Mini = min(Mini, a[i])
    #print(Mini)
    Min[i] = Mini
  print(Min)
  Maxi = -sys.maxsize - 1
  index = -1
  for i in range(n - 1):
    Maxi = max(Maxi, a[i])
    if (Maxi < Min[i + 1]) :
       index = i
       break
  if (index != -1) :
    print("YES")
  else :
    print("NO")
 
N=5
arr=[5,3,2,7,9]
print(arr)
partitionArray(arr,N)
# N=int(input())
# arr = list(map(int,input().split()))[:N]

##############################################
#