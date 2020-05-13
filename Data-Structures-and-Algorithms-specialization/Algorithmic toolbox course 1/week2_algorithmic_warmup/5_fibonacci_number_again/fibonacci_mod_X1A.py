import sys
def fibonacci_mod(n, m):
    fibonacci = [0]
    curr, prev = 1, 0
    if n<1:
        return 0
    
    for i in range(m*m+1):
        prev, curr = curr, (prev+curr)%m
        if len(fibonacci) == n:
            return prev
        
        if (prev, curr) == (0, 1):
            period = i+1
            return fibonacci[n%period]
        fibonacci.append(prev)
        

if __name__ == "__main__":
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(fibonacci_mod(n, m))