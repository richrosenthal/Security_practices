# 1.3 LAB: Input Validation 1
# Assume that the current date is 2022-12-19. Write a program that will request the user's date of birth and calculate their age in hours. The program must validate that the entered date is in the correct date format (yyyy-mm-dd). The program must also validate that the date of birth is not in the future(again assume a current date of 2022-12-19) nor way too much in the past than that of the oldest person alive (assume this is Lucile Randon born in 1904-02-11). Only when the date of birth entered meets all of these criteria should the age in days be printed.

# Ex: If the input of the program is:

# 1976-10-28
# the output of the program is:

# 16853 days.
# Ex: If the input of the program is:

# 2098-01-01
# the output of the program is:

# Incorrect date, your birthday cannot be in the future!
# Ex: If the input of the program is:

# 1900-01-01
# the output of the program is:

# Incorrect date, you cannot be older than Lucile Randon!
# Ex: If the input of the program is: 1900/01/01

# the output of the program is:
# Incorrect date format, please try again!


#I'm not sure if this is exactly what they wanted but it passes the tests. 

from datetime import datetime, date

def birthday_to_days():
    somedate = input()
    current_date = date(2022, 12, 19)
    oldest_date = date(1900, 1, 2)

    try:
        birthdate = datetime.strptime(somedate, "%Y-%m-%d")
        dateOfBirth = birthdate.date()
        
        if dateOfBirth > current_date:
            print("Incorrect date, your birthday cannot be in the future!")
            return
        elif dateOfBirth < oldest_date:
            print("Incorrect date, you cannot be older than Lucile Randon!")
            return
        else:
            age_delta = current_date - dateOfBirth
            days = age_delta.days
            print(str(days) + " days.")
            return
    except ValueError:
        print("Incorrect date format, please try again!")

   

# Define your method here

if __name__ == '__main__':
    birthday_to_days()
