def DP_Change(money):
    coins = [1, 3, 4]
    MinNumCoins = [1000000]*(money+1)
    MinNumCoins[0] = 0
    for m in range(1,(money+1)):
        for coin in coins:
            if(m>=coin):
                NumCoins = MinNumCoins[m-coin] + 1
                if(NumCoins <MinNumCoins[m]):
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]


import sys
if __name__ == '__main__':
    m = int(input())
    print(DP_Change(m))
