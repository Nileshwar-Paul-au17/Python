'''
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that satisfies both these two conditions:

All characters of this string are vowels ('a', 'e', 'i', 'o', and 'u')
The string has all five vowels present in it.
You are given a string S, Count the number of vowel substrings in S.

Input Format

First line of input contains single integer T , i.e Number of Test cases
Next T lines consists of T strings. (1 String on one line)
Constraints

T <= 100
|S| <= 100 where |S| represents length of S
Output Format

Print T lines, answer for each Test case

Sample Input 0

2
aeiouu
unicornarihan
Sample Output 0

2
0
Explanation 0

Test case 1: The vowel substrings of word are as follows (underlined):

"aeiou u"
"aeiouu"
Test case 2: Not all 5 vowels are present, so there are no vowel substrings.

****************************************************************************

Refrence:- https://leetcode.com/problems/count-vowel-substrings-of-a-string/
'''
def subString(str):
    count=0
    for i in range(len(str)-4):
        for j in range(i+5,len(str)+1):
            if((set(str[i:j]) == set('aeiou'))):
                count+=1
    return count


T = int(input())
for i in range(0,T):
    str = input()
    print(subString(str))