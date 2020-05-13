# 思路：由前一题已经知道 mod 10 的周期，所以可以利用周期来加速运算
def last_digit_of_the_sum_of_fibonacci_numbers(n):
    fibonacci = [0]
    curr, prev = 1, 0
    if n<1:
        return 0
    
    for i in range(101):
        prev, curr = curr, (prev+curr)%10
        if len(fibonacci) == n+1:
            return int(sum(fibonacci)%10)
        
        if (prev, curr) == (0, 1):
            period = i+1
            sum1 = sum(fibonacci) * (n - n%period)/period
            sum2 = sum(fibonacci[:int(n%period +1)])
            return int((sum1+sum2)%10)
        fibonacci.append(prev)

if __name__ == "__main__":
    print(last_digit_of_the_sum_of_fibonacci_numbers(int(input())))