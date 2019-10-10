#Xueying Chen
#OUID: 113366600
#DSA4413 – Fall 2019
#Homework #3-6


import math
import random

found = False
threshold = 40 

# merge 2 sorted array
# This function uses inplace
def merge(arr, l, m, r):

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray

    while i < len(L) and j < len(R) :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr


# sort arr using insertion sort.
def insertionSort(arr, begin_index, end_index):
    for i in range(begin_index + 1, end_index+1):
        key = arr[i]
        j = i-1
        while j >= begin_index and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key


# sort array using merge sort
def mergeSort(arr,l,r):
    # if number of element in sub array less than threshold (40) 
    if (r - l) <= threshold:
       insertionSort(arr, l, r)
    elif l < r:

        m = int(math.floor((l+r)/2))

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

mergeSort(arr,0,n-1)
print(arr)

arr2 = random.sample(range(1, 1000), 500)

mergeSort(arr2,0,len(arr2)-1)
print(arr2)

