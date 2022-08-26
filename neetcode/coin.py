from curses import use_default_colors
from sys import argv

def coin_helper_values(coins):
    def coin_row_helper_values(index, memo):
        if index in memo:
            return memo[index]
        if index < 0:
            result = (0, [])
        else:
            use_it = coin_row_helper_values(index-2, memo)
            lose_it = coin_row_helper_values(index-1, memo)
            new_sum = use_it[0] + coins[index]

            #1
            if new_sum > lose_it[0]:
                result = (new_sum, [coins[index]] + use_it[1])
            else:
                result = lose_it

            #2
            # result = (new_sum, [coins[index]] + use_it[1]) \
            #     if new_sum > lose_it[0] else lose_it

        memo[index] = result
        return result
    return coin_row_helper_values(len(coins) - 1, {}) 


lines = []
with open("large_input.txt", 'r') as file:

    lines = [int(x) for x in file.readlines()]
    print(coin_helper_values(lines))