'''
You have given a list of N dishes numbered from 1 to N. The tastiness of ith dish is A[i] .
Choose longest sequence of consecutive dishes such that tastiness of all the dishes in the sequence is unique.
In other words, find out the longest sequence of successive dishes with no duplicate tastiness.

Input Format

The first input line contains an integer N: the number of dishes.
The next line has N integers A[1],A[2] ... A[N]: the tastiness of each dish.
Constraints

1 <= N <= 2 x 105
1 <=A[i] <= 109
Output Format

Print the length of the longest sequence.

Sample Input 0

8
1 2 1 3 2 7 4 2
Sample Output 0

5
Explanation 0

The sequence [1, 3, 2, 7, 4] is the longest contigous sequence with no duplicates
'''
def lengthOfLongestSubstring(s):
  i =0
  j = 0
  d={}
  ans = 0
  while j < len(s):
     if s[j] not in d or i>d[s[j]]:
        ans = max(ans,(j-i+1))
        d[s[j]] = j
     else:
        i = d[s[j]]+1
        ans = max(ans,(j-i+1))
        j-=1
     #print(ans)
     j+=1
  return ans
n = int(input())
s = list(map(int, input().split()))

print(lengthOfLongestSubstring(s))