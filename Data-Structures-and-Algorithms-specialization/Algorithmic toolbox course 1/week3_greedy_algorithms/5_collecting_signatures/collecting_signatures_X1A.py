def recursion(points, count, n, left_sorted, right_sorted):
    count += 1
    point = right_sorted[0]    
    points.append(point)
    left_sorted.pop(0)
    right_sorted.pop(0)
    for i in range(len(left_sorted)):
        if(left_sorted[0] <= point):
            left_sorted.pop(0)
            right_sorted.pop(0)
            if(right_sorted==[]):
                return count, points
        else:
            return recursion(points, count, n, left_sorted, right_sorted)

def collecting_signatures(n, left, right):
    count = 0
    right_sorted = sorted(right, reverse=False)
    left_sorted = [ left[ right.index(right_sorted[i]) ] for i in range(0, n) ]
    points = []
    count, points = recursion(points, count, n, left_sorted, right_sorted)
    print(count)
    for point in points:
        print(point, end=' ')
    print('\n', end='')

import sys
if __name__ == "__main__":
    n = int(input())
    lefts = []
    rights = []
    for i in range(n):
        left, right = map(int, sys.stdin.readline() .split())
        lefts.append(left)
        rights.append(right)
    collecting_signatures(n, lefts, rights)