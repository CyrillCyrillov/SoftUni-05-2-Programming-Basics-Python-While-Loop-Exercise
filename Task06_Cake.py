width = int(input())
length = int(input())
all_pieces = width * length
next = " "

while all_pieces > 0 and next != "STOP":
    next = input()
    if next != "STOP":
        next_pieces = int(next)
        all_pieces -= next_pieces

if next == "STOP":
    print(f"{all_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(all_pieces)} pieces more.")
