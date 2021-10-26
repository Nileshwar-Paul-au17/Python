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
        for j in range(0,n-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
               
                swapped = True
            
        if swapped == True:
            break

    return A

A = [5,1,4,2,8]

print(bubble_sort(A))   