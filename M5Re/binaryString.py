'''
You are given a binary string S consisting of only '0' and '1'.
you can delete any two adjacent character if they are different.
Print the minimum length of the string that you can make by deletion if you are allowed to perform the above operation as many times as possible.

Input Format

First and only line of input contains string S.

Constraints

|S|<=100000

Output Format

Print the minimum achievable length of string.

Sample Input 0

11000
Sample Output 0

1
Explanation 0

After deleting "10" we get "100" and we can delete another "10" to get "0" which has a length of 1.
'''
def finalString(st):

    x , y = 0 , 0
 
    n = len(st)
 

    for i in range( n):
        if (st[i] == '1'):
            x += 1
        else:
            y += 1

    if (x > y):
        left = 1
    else:
        left = 0

    length = n - 2 * min(x, y);
    return length

 
 
st = input()
print(finalString(st))