'''
Consider an infinite one dimensional axis(X-axis).
Initially, you are present at position X and your destination is at posititon Y on the X-axis.
If You are currently at position k, You can perform following types of moves:

Type1: Move to position k+2, or
Type2: Move to position k−1
Find the minimum number of moves required for you to reach the destination.

Input Format

First line will contain a single integer T, the number of testcases. Then the description of T testcases follows.
Each testcase contains a single line with two space-separated integers X,Y, representing the initial positions of Chef and his dance partner, respectively.
Constraints

1 <= T <=1000
−10000 <= X,Y <= 1000
Output Format

For each testcase, print in a separate line, a single integer, the minimum number of moves required to reach destination.

Sample Input 0

4
3 8
-11 -5
57 492
-677 913
Sample Output 0

4
3
219
795
Explanation 0

Test Case 1: You will perform move of type 1 thrice, followed by one move of type 2 reaching at position 8. This makes 4 dance steps in total.
Test Case 2: Performing move of type 1 thrice will take you to the destination
'''
n = int(input())
for i in range(n):
    x,y=map(int,input().split())
    ans = 0
    while(x!=y):
        ans+= 1
        if(x<y):
            x+=2
        elif(x>y):
            x-=1
    print(ans)