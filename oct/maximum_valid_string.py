"""
You are given a valid parenthesis string S containing "(" and ")".
Split them into the maximum number of balanced parenthesis string groups.Print the maximum number of such groups.

Input Format

First and only line of input contains a string S

Constraints

|S| <=100000
Output Format

Print maximum number of groups in which the orignal string can be split such that each group is valid parenthesis string

Sample Input 0

()()(()())
Sample Output 0

3
Explanation 0

The given string can be split into 3 groups. ["()", "()", "(()())"]

Sample Input 1

()()
Sample Output 1

2
Explanation 1

The above valid string can be split into maximum 2 balanced parenthesis strings. ["()", "()"]
"""
def check(s):
        
        parenthesis= 0
        count =0
        for i in string: 
            if i == '(':
                parenthesis += 1
            else:
                parenthesis -= 1
                if parenthesis == 0:
                    count = count+1
                
        return count

string= input()

result =check(string)
print(result)