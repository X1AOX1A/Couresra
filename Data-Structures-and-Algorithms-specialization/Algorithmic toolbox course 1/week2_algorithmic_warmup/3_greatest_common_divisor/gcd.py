# Uses python3
import sys

def gcd(a, b):
    m = max(a,b)
    n = min(a,b)
    if m%n ==0 :
        return n
    
    return gcd(n,m%n)

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd(a, b))