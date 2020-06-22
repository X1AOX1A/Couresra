# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            index.append(i)
        if next in ")]}":
            if(len(opening_brackets_stack)==0):
                return(i+1)
            if( are_matching(opening_brackets_stack[-1], next) ):
                opening_brackets_stack.pop()
                index.pop()
            else:
                return(i+1)
        if(i==len(text)-1)&(len(opening_brackets_stack)==0):
            return('Success')
        elif(i==len(text)-1)&(len(opening_brackets_stack)!=0):
            return(index[-1]+1)



def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
