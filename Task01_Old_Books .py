wanted_book = input()
next_book = " "
checked_books = 0


while next_book != "No More Books" and next_book != wanted_book:
    next_book = input()
    checked_books += 1

if next_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {checked_books - 1} books.")
else:
    print(f"You checked {checked_books - 1} books and found it.")

