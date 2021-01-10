money = float(input())
rest = int(money * 100)
coins = 0

while rest > 0:
    if rest >= 200:
        next_coins = rest // 200
        coins += next_coins
        rest = rest % 200
    elif rest >= 100:
        next_coins = rest // 100
        coins += next_coins
        rest = rest % 100
        # print(coins)
        # print(rest)
    elif rest >= 50:
        next_coins = rest // 50
        coins += next_coins
        rest = rest % 50
        # print(coins)
        # print(rest)
    elif rest >= 20:
        next_coins = rest // 20
        coins += next_coins
        rest = rest % 20
        # print(coins)
        # print(rest)
    elif rest >= 10:
        next_coins = rest // 10
        coins += next_coins
        rest = rest % 10
        # print(coins)
        # print(rest)
    elif rest >= 5:
        next_coins = rest // 5
        coins += next_coins
        rest = rest % 5
        # print(coins)
        # print(rest)
    elif rest >= 2:
        next_coins = rest // 2
        coins += next_coins
        rest = rest % 2
        # print(coins)
        # print(rest)
    else:
        coins += 1
        rest = 0

print(coins)