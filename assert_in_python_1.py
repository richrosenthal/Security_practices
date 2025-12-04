def process_grades():
    user_input = input()
    entered_grades = user_input.split(',')
    grades = []
    total = 0
    for grade in entered_grades:
        grades.append(int(grade))
        total += int(grade)
        
    try:
        assert all(0 <= g <= 100 for g in grades), "All values need to be greater than 0 but less than 100"
        assert (total <= 100), "One of the grades is wrong, total needs to be less than 100!"
        print(total)
    except AssertionError as e:
        print(e)

if __name__ == '__main__':
    process_grades()

# Write a program that will accept four grades and place them in a list. The sum of the 4 grades should be less or equal to 100. Each individual grade should be greater or equal to 0, but less or equal to 100. Include an assert statement that will display a message if any of these conditions are not met. The assert statements should display the messages "All values need to be greater than 0 but less than 100" and "One of the grades is wrong, total needs to be less than 100!", as appropriate.

# Ex: If the input of the program is:

# 25, 10, 15, 25
# the output of the program is:

# 75
# Ex: If the input of the program is:

# 25, 30, 20, 40
# the output of the program is:

# One of the grades is wrong, total needs to be less than 100!
# Ex: If the input of the program is:

# 25, 30, -1, 40
# the output of the program is:

# All values need to be greater than 0 but less than 100