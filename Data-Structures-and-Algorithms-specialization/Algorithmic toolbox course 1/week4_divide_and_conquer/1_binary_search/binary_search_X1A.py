import math
def binary_search(A, low, high, key):
    if(high < low):
        return -1
    mid = math.floor(low+(high-low)/2)
    if(key == A[mid]):
        return mid
    elif(key < A[mid]):
        return binary_search(A, low, mid-1, key)
    else:
        return binary_search(A, mid+1, high, key)

import sys
if __name__ == '__main__':
    A = list(map(int, sys.stdin.readline().split()))[1:]
    B = list(map(int, sys.stdin.readline().split()))[1:]
    for b in B:
        print(binary_search(A, 0, len(A)-1,  b), end=' ')