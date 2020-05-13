# Uses python3
import sys

def gcd(a, b):
    m = max(a,b)
    n = min(a,b)
    if m%n ==0 :
        return n
    
    return gcd(n,m%n)

def lcm(a, b):
    if min(a,b) == 0:
        return 0
    
    return int((a*b) / gcd(a, b))

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))