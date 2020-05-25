# 思路：为了使硬币数量最少，优先使用面额较大的硬币
def money_change(money):
    remain = money
    ten_num = remain // 10
    remain -= 10*ten_num
    five_num = remain // 5
    remain -= 5*five_num
    return(ten_num+five_num+remain)

print(money_change(int(input())))