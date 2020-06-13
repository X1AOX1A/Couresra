def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(M, m, i, j, op):
    Min = 10**6
    Max = -10**6
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        Min = min(Min, a, b, c, d)
        Max = max(Max, a, b, c, d)
    return (Min, Max)

def get_maximum_value(dataset):
    numbers, operations = list(map(int,dataset[::2])),dataset[1::2] # get numbers and operations from provided string input
    n = len(numbers)
    # two matrices store minimum and maximum numbers
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]

    #calculate only half part of the matrix, the upper part
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operations) #find min and max from min_max function

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
