def car_fueling(destination, fuel_max, n, gas_station):
    '''
    Idea:
      The length between now and next station have three cases:
      for i from 0 to num_station+1:
          1. X[i+1] - X[i] <= fuel_left 
              --> fule_left -= X[i+1] - X[i]
          2. fuel_left < X[i+1] - X[i] <= fuel_max
              --> add fule
              --> fuel_left = fuel_max
          3. X[i+1] - X[i] > fuel_max
              --> that is impossible
    
    Input:
      destination -- the distance between the cities
      fuel_max -- a car can travel an most m miles on a full tank
      n -- the num of gas stations
      gas_station -- the distances of n gas stations
      
    Output:
      num_Refills -- the min num of refills
    '''
    gas_station.insert(0, 0)
    gas_station.append(destination)
    num_Refills = 0     # the num of Refills
    fuel_left = fuel_max
    for i in range(n+1):
        # print('\n现在是第',i,'站')
        length = gas_station[i+1] - gas_station[i]
        # print('距离下一站还有：',length)
        # print('还剩油量：', fuel_left)
        if(length <= fuel_left):
            # print('油还够')
            fuel_left -= length
        elif(length <= fuel_max):
            num_Refills += 1
            fuel_left = fuel_max - length
            # print('油不够啦，加了第',num_Refills ,'次油')
        else:
            # print('加满油也跑不到下一站啦')
            return -1
        # print('\n|\n开了', length ,'公里\n|')
    return num_Refills

import sys
if __name__ == "__main__":
    destination = int(input())
    fuel_max = int(input())
    station_num = int(input())
    gas_station = list(map(int, sys.stdin.readline() .split()) )
    print(car_fueling(destination, fuel_max, station_num, gas_station))