from functools import cache
coins = [1,2,5,10,20,50,100,200]
@cache
def get_num_ways(pence_left,coin_limit=201):
    if pence_left == 0:
        return 1
    ans = 0
    for coin in coins:
        if coin >= coin_limit:
            continue
        for num_coins in range(1,int((pence_left/coin)+1)):
            ans += get_num_ways(pence_left-(coin*num_coins),coin)

    return ans

print(get_num_ways(200))