'''
You are given two integers L and R.
Check whether the binary representation of both L and R have equal number of 0s and 1s.

Input Format

First line of input contains only two integers L and R

Constraints

1 <= L , R <= 1000000

Output Format

Print "YES" or "NO"

Sample Input 0

5 6
Sample Output 0

YES
Explanation 0

5-> 101
6-> 110
Both 5 and 6 have same number of 0s and 1s
'''
from collections import Counter
  
def check(num1,num2):
  
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
  
   
    zeros = abs(len(bin1)-len(bin2))
    if (len(bin1)>len(bin2)):
         bin2 = zeros * '0' + bin2
    else:
         bin1 = zeros * '0' + bin1
  
   
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)
  
  
    if dict1 == dict2:
         print('YES')
    else:
         print('NO')
 
num1,num2=list(map(int,input().split()))[:2]

check(num1,num2)
#################################################
from collections import Counter
  
def checkAnagram(num1,num2):
  
    # convert numbers into in binary
    # and remove first two characters of 
    # output string because bin function 
    # '0b' as prefix in output string
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
  
    # append zeros in shorter string
    zeros = abs(len(bin1)-len(bin2))
    if (len(bin1)>len(bin2)):
         bin2 = zeros * '0' + bin2
    else:
         bin1 = zeros * '0' + bin1
  
    # convert binary representations 
    # into dictionary
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)
  
    # compare both dictionaries
    if dict1 == dict2:
         print('YES')
    else:
         print('NO')
 
num1,num2=list(map(int,input().split()))[:2]

checkAnagram(num1,num2)
