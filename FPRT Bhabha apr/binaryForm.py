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


def check(num1, num2):

    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]

    print(bin1, bin2)
    zeros = abs(len(bin1)-len(bin2))
    if (len(bin1) > len(bin2)):
        bin2 = zeros * '0' + bin2
    else:
        bin1 = zeros * '0' + bin1

    print(bin1, bin2)
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)

    if dict1 == dict2:
        print('YES')
    else:
        print('NO')


num1, num2 = list(map(int, input().split()))[:2]

check(num1,num2)
#################################################

# L,R=list(map(int,input().split()))[:2]
# L=bin(L).replace("0b", "")
# R=bin(R).replace("0b", "")
# print(L,R)
# a,b,c,d=0,0,0,0
# for i in range(0,len(L)):
#     if L[i]=='0':
#         a+=1
#     else:
#         b+=1
# for i in range(0,len(R)):
#     if R[i]=='1':
#         c+=1
#     else:
#         d+=1

# if(a==d and b==c):
#     print("YES")
# else:
#     print("NO")
