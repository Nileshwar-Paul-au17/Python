'''

There are N trains scheduled on a particular train station. You know the arrival time T1 and Departure time T2 for each train beforehand.
Find the maximum number of trains present at the station at any moment of time.

Input Format

First line contains a single integer N. Next N lines contains 2 integers per line T1 and T2.

Constraints

1 <= N <= 2.105
1 ≤ T1 < T2 <= 1012
Output Format

Print one integer: the maximum number of Trains present at the station at a particular moment of time.

Sample Input 0

3
5 8
2 4
3 9
Sample Output 0

2
Explanation 0

From time 3 to 8 , 2 trains are available . SO maximum number of trains available at some point of time is 2.
'''
def trains(lst):
    arr = []
    dep = []
    for start, end in lst: 
        arr.append(start)
        dep.append(end)
    arr.sort()
    dep.sort()
    plat_req = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (arr[i] < dep[j]):
            plat_req += 1
            i += 1
            if (plat_req > result):
                result = plat_req
        else:
            plat_req -= 1
            j += 1
    return result
    
n = int(input())     
result = list()      
for i in range(n):
    array = list(map(int, input().split()))
    result.append(array)   

print(trains(result))