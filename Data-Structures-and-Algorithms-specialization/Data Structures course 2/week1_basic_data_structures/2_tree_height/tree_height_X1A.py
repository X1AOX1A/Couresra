# python3

import sys
import threading
def find_childs(array, index, parent):
    childs = [i for a,i in zip(array, index) if a==parent]
    if childs != []:
        for child in childs:
            array.remove(array[index.index(child)])
            index.remove(child)
    return childs, array, index


def recusion(parent, height, array, index):
    childs, array, index = find_childs(array, index, parent)
    if childs==[]:
        return height
    if childs!=[]:
        height += 1
        heights = []
        for child in childs:
            heights.append(recusion(child, height, array, index)) 
        return max(heights)


def compute_height(n, array):
    root = array.index(-1)
    height = 1
    index = [i for i in range(0, n)]
    array.remove(-1)
    index.remove(root)
    return recusion(root, height, array, index)
    

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
