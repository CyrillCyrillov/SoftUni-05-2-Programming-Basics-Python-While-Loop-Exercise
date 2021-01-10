needed_money = float(input())
money = float(input())
spend_day = 0
days = 0

while money < needed_money and spend_day < 5:
    action = input()
    next_money = float(input())
    days += 1
    if action == "save":
        money += next_money
        spend_day = 0
    else:
        spend_day += 1
        money -= next_money
        if money < 0:
            money = 0

if spend_day == 5:
    print("You can't save the money.")
    print(days)
else:
    print(f"You saved the money for {days} days.")

