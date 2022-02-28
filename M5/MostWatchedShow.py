''' 
You are given two arrays A and B of size N.
A[i] represents the ith show name and B[i] represents the number of people who watched ith show.

Print the K Most watched show.
Print show names in lexicographical order.

NOTE:

It is guaranteed that all elements of array A and B are unique
Input Format

First line of input contains two integers N and K.
Second line of input contains N space seperated integers (elements of array A).
Third line of input contains N space seperated integers (elements of array B).
Constraints

1 <= N <=1000
Output Format

Print show names in lexicographical order

Sample Input 0

5 2
topgun aviator top roma logan
5 3 4 2 6
Sample Output 0

logan topgun

'''
def mostWatched(N,K,A,B):
    
    res = []
    
    while len(res) < K :
        
        Max = float('-inf')
        
        idx = 0
        for i in range (len(B)):
            
            if B[i] > Max :
                
                Max = B[i]
                
                idx = i
                
                
        res.append(A[idx])
        
        A.pop(idx)
        
        B.pop(idx)
        
    
    res.sort()
    
    res = ' '.join(map(str, res))
    
    return res



N , K = map(int, input().split())

A = list(map(str, input().split()))

B = list(map(int, input().split()))

print(mostWatched(N,K,A,B))