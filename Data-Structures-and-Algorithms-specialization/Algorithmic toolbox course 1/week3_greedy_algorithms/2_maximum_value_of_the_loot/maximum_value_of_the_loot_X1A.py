def maximum_value_of_the_loot(n, W, dic):
    '''
    Idea: 
     Firstly sort the ratio of items, 
     and then take the most valued items until
     reach the capacity of bag's weight
    
    Input:
     n   -- the num of items
     W   -- the total weight(capacity) of bag
     dic -- dictornary contains key [value] and [weight] for n items
           
    Output:
     V   -- the max value of bag
    '''
    # 计算 value/weight 的比率
    dic['ratio'] = [float(dic['value'][i]) / float(dic['weight'][i])  for i in range(0,n)]
    # 将比率按从大到小排列
    ratio_sorted = sorted(dic['ratio'], reverse=True)
    # 按比率的排列顺序重排 weight
    weight_sorted = [ dic['weight'][dic['ratio'].index(ratio_sorted[i])] for i in range(0, n) ]
    
    i = 0 # index of item
    V = 0 # the total value of bag
    weight_used = [0 for i in range(0, n)] # the used weight of itme i
    while(W>0):
        a = min(weight_sorted[i], W) # take a weight of item i 
                                 # (no more than the remain weight of bag)
        weight_used[i] += a          # the used weight of item i
        weight_sorted[i] -= a    # the remain weight of item i
        W -= a                   # the remain weight of bag
        V = V + a*ratio_sorted[i]# the total value of bag
        i += 1                   # to the next item
        if weight_sorted[n-1]==0:# if last item is no left, break
            break
        
    return round(V, 4)

import sys
if __name__ == "__main__":
    n, W = map(int, sys.stdin.readline() .split()) 
    dic = {'value':[], 'weight':[]}
    for i in range(0, n):
        v, w = map(int, sys.stdin.readline() .split()) 
        dic['value'].append(v)
        dic['weight'].append(w)
    Value = maximum_value_of_the_loot(n, W, dic)
    print("{:.4f}".format(Value))