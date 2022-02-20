# Bubble Sort
"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly
swapping the adjacent elements if they are in wrong order.
"""

# [5,4,3,2,1]

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        
        
        for j in range(0,n-i-1):
            print(j)
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                swapped = True
                if(i==0):

                    print(A)
                
       
    return A
A = [5,3,1,9,8,2,4,7]
print(bubble_sort(A))   
