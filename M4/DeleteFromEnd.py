"""
You are given a string S of size N containing 0s and 1s only.
You can delete numbers from the front or from the back.

Return the minimum number of deletions such that the remaining string(after removal from front and back) has an equal number of 0s and 1s.

Input Format

First and only line of input contains string S of size N.

Constraints

N<=100000

Output Format

Print a single integer

Sample Input 0

111100
Sample Output 0

2
Explanation 0

We can delete the first two 1s so that there's two 1s and two 0s.
"""
S = input()
nums=[]
nums[:0]=S
maximum = 0
d = {0 : -1}
currSum = 0
for i in range(len(nums)):
    if nums[i] == "0": 
        currSum -= 1 
    else: 
        currSum += 1 
    if currSum in d: 
        maximum = max(maximum, i - d[currSum]) 
    else: 
        d[currSum] = i 
print(len(nums) - maximum)