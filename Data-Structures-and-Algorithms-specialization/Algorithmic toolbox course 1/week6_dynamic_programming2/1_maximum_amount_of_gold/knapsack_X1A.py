# Uses python3
import sys
def optimal_weight(Capacity, items):
    n = len(items)
    values = [ [0 for _ in range(Capacity+1)] for _ in range(n+1) ]
    
    for current in range(1, Capacity+1):
        for idx in range(1, n+1):
            item = items[idx-1]
            previous_value = values[idx-1][current]
            if item > current:
                values[idx][current] = previous_value
            else:
                current_value = item + values[idx-1][current-item] # add item
                values[idx][current] = max(current_value, previous_value)
    return values[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    Capacity, n, *items = list(map(int, input.split()))
    print(optimal_weight(Capacity, items))