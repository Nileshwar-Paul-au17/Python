
def selection_sort(A):

    n = len(A)
    for i in range(n):
        
      
        for j in range(i,len(A)):
            if A[j] < A[i]:
                 
                
                A[i],A[j] = A[j],A[i]
                 
        print(A)
    return A

if __name__=="__main__":
    
     #A = [64,25,12,22,11]
     A = [2,0,1]

     print(selection_sort(A)) 
