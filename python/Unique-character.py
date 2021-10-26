"""
You are given a string S of length N.
Print "YES" if the string contains any repeated character, otherwise print "NO".

Input Format

First and only line of input contains string S.
Constraints

N<=100000

Output Format

Print "YES" or "NO"

Sample Input 0

abc
Sample Output 0

NO
Sample Input 1

abcbt
Sample Output 1

YES
Submissions: 34
Max Score: 20
Difficulty: Easy
Rate This Challenge:

    
More

"""
def check(str):
    
    dict={}
    
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for character, frequency in dict.items():
        if frequency > 1:
            return "YES"
    
    return "NO"

str = input()

result =check(str)

print(result)