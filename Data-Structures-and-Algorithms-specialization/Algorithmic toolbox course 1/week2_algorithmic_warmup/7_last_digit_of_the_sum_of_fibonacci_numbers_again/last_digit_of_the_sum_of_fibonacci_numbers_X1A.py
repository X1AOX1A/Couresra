import sys

# 思路：由前一题已经知道前 n 个的和的最后一位，因此在此基础上修改即可
def last_digit_of_the_sum_of_fibonacci_numbers_again(n1, n2):
    fibonacci = [0]
    curr, prev = 1, 0
    if n2<1:
        return 0
    
    for i in range(101):
        prev, curr = curr, (prev+curr)%10
        
        if (prev, curr) == (0, 1):
            period = i+1
            sum1 = sum(fibonacci) * (n2 - n2%period)/period
            sum2 = sum(fibonacci[:int(n2%period +1)])
            
            n1 = n1-1
            sum3 = sum(fibonacci) * (n1 - n1%period)/period
            sum4 = sum(fibonacci[:int(n1%period +1)])
            return int(sum1+sum2-sum3-sum4)%10
        fibonacci.append(prev)

if __name__ == "__main__":
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(n, m))