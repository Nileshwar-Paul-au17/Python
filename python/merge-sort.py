# Merge Sort

"""
Given 2 arrays sorted array A and B. we need to merge then and get 
sorted array C.
A =[1,4,6,7,8,9]
B =[3,5,14,18]
C =[]
"""

def Merge2sortarray(A,B):

    n = len(A)
    m = len(B)

    p1 = 0
    p2 = 0

    c = list()

    while p1 < n and p2 < m:
        if A[p1] < B[p2]:
            c.append(A[p1])
            p1 += 1
        else:
            c.append(B[p2])
            p2+=1

    while p1 < n:
        c.append(A[p1])
        p1 += 1

    while p2 < m:
        c.append(B[p2]) 
        p2 +=1

    return c    
list1=[9,7,22,1,88,2,6,100,8,2,11]
mid=(0+len(list1))//2
A = sorted(list1[:mid])
B = sorted(list1[mid:])
#print(mid,A,B)

print(Merge2sortarray(A,B))       