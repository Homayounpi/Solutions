year, month, day = list(map(int, input("Enter your date: ").split('/')))

if month <= 6:
    if day < 31:
        day += 1
    elif day == 31:
        month += 1
        day = 1
elif month > 6:
    if year % 4 == 3:
        if day < 30:
            day += 1
        elif day == 30:
            year += 1
            month = 1
            day = 1
    else:
        if day < 29:
            day += 1
        elif day == 29:
            year += 1
            month = 1
            day = 1

print(str(year), str(month), str(day), sep='/')
