max_bad_grades = int(input())
number_of_problems = 0
last_problem = " "
sum_grades = 0
bad_grades = 0
next_problem = " "
# grades = 0

while next_problem != "Enough" and bad_grades < max_bad_grades:
    next_problem = input()
    if next_problem != "Enough":
        next_grade = int(input())
        sum_grades += next_grade
        number_of_problems += 1
        last_problem = next_problem
        if next_grade <= 4:
            bad_grades += 1

if next_problem == "Enough":
    print(f"Average score: {sum_grades / number_of_problems:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades} poor grades.")
