day_target = 10000
steps = 0
next_steps = " "

while steps <= day_target and next_steps != "Going home":
    next_steps = input()
    if next_steps == "Going home":
        last_step = int(input())
        steps += last_step
    else:
        next_steps = int(next_steps)
        steps += next_steps

if steps >= day_target:
    print("Goal reached! Good job!")
    print(f"{steps - day_target} steps over the goal!")
else:
    print(f"{day_target - steps} more steps to reach goal.")
