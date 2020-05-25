def maximum_advertisement_revenue(n, profit_of_click, number_of_click):
    profit_sort = sorted(profit_of_click, reverse=True)
    number_sort = sorted(number_of_click, reverse=True)
    return sum([profit_sort[i]*number_sort[i] for i in range(n)])

import sys
if __name__ == "__main__":
    n = int(input())    
    profit_of_click = list(map(int, sys.stdin.readline() .split()) )
    number_of_click = list(map(int, sys.stdin.readline() .split()) )
    print(maximum_advertisement_revenue(n, profit_of_click, number_of_click))