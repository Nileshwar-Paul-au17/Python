'''
You are given an array A of size N. It is known that in this array, all the numbers except one are the same.
(for example, in the array [4,11,4,4] all numbers except one are equal to 4).

Print the index of the element that does not equal others. The numbers in the array are indexed from 1.

Input Format

The first line of each test case contains a single integer N.
The Second line contains N integers A[1], A[2] ,…,A[n].
It is guaranteed that all the numbers except one in the array are the same.
Constraints

3 <= N <=100
1 <= A[i] <=100
Output Format

print index of the element which is different from others

Sample Input 0

4
11 13 11 11
Sample Output 0

2
Sample Input 1

5
1 4 4 4 4
Sample Output 1

1
Sample Input 2

10
3 3 3 3 10 3 3 3 3 3
Sample Output 2

5
Sample Input 3

3
20 20 10
Sample Output 3

3
'''
l = int(input())
a = list(map(int,input().split()))
# print(l)
# print(a)
d = {}
def checkOdd():
    for num in a:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    for k,v in d.items():
        if(v==1):
            return k
key = checkOdd()

for i in range(l):
    if key == a[i]:
        print(i+1)
#print(key,d)