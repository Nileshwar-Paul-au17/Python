''' 
You are given a string S of length N and two integers X and Y.
You can perform two types of operations any number of times.

Remove substring "ab" and gain x points. For example, when removing "ab" from "cabhbae" it becomes "chbae".
Remove substring "ba" and gain y points. For example, when removing "ba" from "cabhbae" it becomes "cabhe".
Return the maximum points you can gain after applying the above operations on S.

Input Format

First line of input contains String S.
Second line of input contain two space seperated integers X and Y.
Constraints

1 <= N <= 100000
1 <= X, Y <= 10000
S consists of lowercase English letters.
Output Format

Print a single integer

Sample Input 0

cdbcbbaaabab
4 5
Sample Output 0

19
Explanation 0

Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score. Total score = 5 + 4 + 5 + 5 = 19.
'''
def sub(s, x, y):
    a, b = 'ab', 'ba'
    if y > x:
        b, a, y, x = a, b, x, y
    answer = 0        
    for word in [a, b]:
        stack = []
        i = 0
        while i < len(s):
            stack.append(s[i])                
            n = len(stack)
            prefix = stack[n-2] + stack[n-1]
            if prefix == word:
                answer += x
                stack.pop()
                stack.pop()
            i += 1
        x = y
        s = ''.join(stack)
    return answer


s = input()
x, y = map(int, input().split())
print(sub(s, x, y))