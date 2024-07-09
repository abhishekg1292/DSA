
def merge(A, left, mid, right):
    i = left
    j = mid+1
    B = []
    
    while (i<=mid) and (j <= right):
        if A[i] <= A[j]:
            B.append(A[i])
            i = i+1
        else:
            B.append(A[j])
            j = j+1
    
    while i<=mid:
        B.append(A[i])
        i=i+1
    
    while j<=right:
        B.append(A[j])
        j = j+1
    
    for i in range(left, right+1):
        A[i] = B[i-left]
        
def mergeSort(A, left, right):
    if left < right:
        mid = (left+right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A, left, mid, right)

A = [3, 5, 8, 9, 6, 2, 0]
print('Original Array:',A)
mergeSort(A,0,len(A)-1)
print('Sorted Array:',A)