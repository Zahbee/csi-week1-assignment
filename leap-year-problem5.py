def is_leap(year):
    leap = False
    

    # The year can be evenly divided by 4, is a leap year, unless:
    if (year % 4 == 0):
        # The year can be evenly divided by 100, it is NOT a leap year, unless:
        if (year % 100 == 0):
            # The year is also evenly divisible by 400. Then it is a leap year.
            if (year % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
