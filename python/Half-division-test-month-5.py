'''
Leet Code 416


You are given an integer array A of size N.
Return whether you can partition A into two groups such that:

Each element is present in exactly 1 group
Sum of element in both the groups are same
Input Format

The first line contains integers N(the size of the arrays).
The second line contains N integers A[i], elements of the array A
Constraints

N <= 250
1 ≤ A[i] ≤ 100
Output Format

Print "YES" or "NO"

Sample Input 0

4
1 2 5 4
Sample Output 0

YES
Explanation 0

We can have these partitions: [1, 5] and [2, 4].

  
def solve(nums):
    
    if sum(nums)%2 !=0:
        return "NO"
    dp = set()
    
    dp.add(0)
    
    target = sum(nums) // 2
    
    for i in range (0,len(nums)-1):
        
        nextDp = set()
        
        for t in dp:
            if t +nums[i]==target:
                return "YES"
            nextDp.add(t+nums[i])
            nextDp.add(t)
        dp=nextDp
    
    if target in dp :
        return "YES"
    else:
        return "NO"
    
        
#n = int(input())
#nums= list(map(int, input().split()))
nums=[1,5,5,11]
result=solve(nums)
print(result)

'''

# ####### ######
def check(list1):
    sum1 = sum(list1)
    if sum1 % 2 != 0:
        return "NO"
    sum1 //= 2
    set1 = set()
    set1.add(0)
    #print(set1)
    for i in range(0,len(list1)-1):
        list2 = [j + list1[i] for j in set1]
        #print(list2)
        list2=set(list2)
        set1 = set1.union(list2)
        #print(set1)
        if sum1 in set1:
            return "YES"
    return "NO"

list1=list(map(int,input().split()))
#list1=[1,5,5,11]
#result=check(list1)

print(list1)
