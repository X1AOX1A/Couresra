def Primitive_Cal(Num):
    MinOper = [100000]*(Num)
    MinOper[0] = 1
    sequence = []
    for num in range(1,(Num+1)):
        if(num % 3 ==0):
            num = num // 3
            

