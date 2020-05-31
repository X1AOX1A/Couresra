def majority_element(A):
    n = len(A)
    A_count = {}
    for value in A:
        if str(value) in A_count.keys():
            A_count[str(value)] += 1
            if(A_count[str(value)]>n/2):
                return 1
        else:
            A_count[str(value)] = 1
    return 0

import sys
if __name__ == "__main__":
    a = input()
    A = list(map(int, sys.stdin.readline().split()))
    print(majority_element(A))