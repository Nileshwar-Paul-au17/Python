''' 
Given a string S of size N.
Print the index of the character which is unique (appears exactly once in the string). If there are multiple solutions , print the minimum possible index.
If there are no solutions , print -1.

Input Format

First and only line of input contains string S.

Constraints

N<=100000

Output Format

Print the required answer

Sample Input 0

hackherrank
Sample Output 0

2
Explanation 0

c is the left most character which appears exactly once. index of c is 2.

Sample Input 1

aabb
Sample Output 1

-1
Submissions: 10
Max Score: 25
Difficulty: Medium
Rate This Challenge:

    
More
'''
s = input()
d = {}

for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
        
newK = []
for k,v in d.items():
    if v == 1:
        newK.append(k)

def func():
    if len(newK) == 0:
        return -1
    for i in range(len(s)):

        if newK[0] == s[i]:
            return i
print(func())