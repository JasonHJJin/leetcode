def knapsack(weight_value, capacity):

    weight_value = [0] + weight_value
    rows = len(weight_value)
    cols = capacity + 1

    cost = [[0 for _ in range(cols)] for _ in range(rows)]

    #print(cost)

    for row in range(1, rows):
        item_weight = weight_value[row][0]
        item_value = weight_value[row][1]
        for col in range(1, cols):
            lost_it_cost = cost[row-1][col]
            if item_weight <= col:
                cost[row][col] = max(
                    cost[row - 1][col - item_weight] + item_value, lost_it_cost)
            else:
                cost[row][col] = lost_it_cost
    return cost[rows-1][cols-1]

if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        line = input().split()
        capacity, num_items = int(line[0]), int(line[1])
        weight_value = []
        for _ in range(num_items):
            line = input().split()
            weight_value.append((int(line[0]), int(line[1])))
        print(knapsack(weight_value, capacity))
