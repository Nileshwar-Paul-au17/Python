'''
Given two lowercase alphabet strings S and T.
Return the minimum amount of operations on S required to make T a substring of S.
In each operation, you can choose any position in S and change the character at that position to any other character.

Input Format

First line of input contains string S.
Second line of input contains Sting T.
Constraints

1 <= N , M < =100

Output Format

Print a single integer, i.e minimum number of operations

Sample Input 0

foobar
oops
Sample Output 0

2
Explanation 0

We can take the substring "ooba" and change 'b' to 'p' and 'a' to 's'.

Sample Input 1

ssaaba
aab
Sample Output 1

0
Explanation 1

"aab" is already a substring of "ssaaba". So, minimum number of operations required=0

Contest ends in 20 minutes
Submissions: 12
Max Score: 25
Difficulty: Medium
Rate This Challenge:

    
More
 

'''
def solve( s, t):
  k, n = len(t), len(s)
  ans = 10**10
  for i in range(n - k + 1):
     ss = s[i:i+k]
     ans = min(ans, sum(ss[j]!=t[j] for j in range(k)))
  return ans

s = input().strip()
t = input().strip()
print(solve(s,t))