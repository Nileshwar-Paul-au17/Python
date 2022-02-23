
def selection_sort(A):

    n = len(A)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min=j
        A[i],A[min]=A[min],A[i]
        print(A)
    return A

if __name__=="__main__":
    
    #A = [64,25,12,22,11]
    A=[2,0,1]

    print("After Sorting:",selection_sort(A)) 
