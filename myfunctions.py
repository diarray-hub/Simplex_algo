# A function to insert multiple items at precise indexes in a list
def multinsert(list1, indexes, items):
    if type(items) is list:
        for (index, item) in zip(indexes, items):
            list1.insert(index, item)
        return list1
    else:
        for index in indexes:
            list1.insert(index, items)
        return list1

# A function which return all divisor of a positive number
def list_div(n):
    listdiv = []
    for i in range(1,n+1):
        if(n%i==0):
            listdiv.append(i)
    return listdiv

# A function which check if a number is prime or no
def is_prime(n):
    if(list_div(n) == 2):
        return True
    else:
        return False

# A function which return a list of all prime numbers <= number
def primelist(n):
    liste_de_nbresprem = []
    for i in range(1,n+1):
        if len(list_div(i)) == 2:
            liste_de_nbresprem.append(i)

# A function which return the sum of all digits in a number
def digitsum(n):
    if n//10==0:
        return n
    else:
        return n%10 + digitsum(n//10)

# A print function variation
def print_2D(matrix):
    for rows in matrix:
        for columns in rows:
            print(f"{columns:0>16d}", end=" ")
        print()

# A function which check if all items in an iterable is less than 0
def all_negative(iterable):
    for item in iterable:
        if item > 0:
            return False
    return True

# A function which check if all items in an iterable is grater than 0
def all_positive(iterable):
    for item in iterable:
        if item < 0:
            return False
    return True

# An implementation of Zeller's algorithm
def Zeller_algorithm(day, month, year):
    """ 
    These formulas are based on the observation that the day of the week progresses in a predictable manner 
    based upon each subpart of that date. Each term within the formula is used to calculate the offset needed to obtain the correct day of the week.
    Zeller's algorithm is an well known algorithm created by Cristian Zeller
    which permit to find the day of the week corresponding to a given date
    the original formula of Zeller look like below:
    day_of_week = (d + floor(13 * (m + 1) / 5) + y + floor(y / 4) - floor(y / 100) + floor(y / 400)) % 7
    where floor(x) mimic a function whom round the nearest integer less or equal to x (the base number or integer part).
    In python we've got the built-in module function math.floor.
    Note that some details are changed in my interpretation of Zeller's algo
    In the original algo mapping look like below after Gregorian calendar
        0:Saturday
        ...
        ...
        6:Friday
    In mine I will manage to get a natural ISO-day mapping like
        1:Monday
        ...
        ...
        7:Sunday
    If the given year has a number of digits less than 3 then we will add 1900 to it
    since day of the week repeats in a fixed cycle of 7 days, so adding or subtracting 
    a multiple of 7 to the year will not change the day of the week.
    We need to do so cause of century's presence in the formula and cannot get 0 there.
    In this algorithm January and February are counted as months 13 and 14 of the previous year 
    """
    from math import floor
    
    twodigits = str(year)
    if (len(twodigits) == 2): year += 1900
    if (month == 1 or month == 2):
        year -= 1
        month += 12
    year_in_century = year % 100 # year in the century
    century = year // 100   # to find the  zero-based century of the given year
    
    day_of_week = (day + floor(2.6 * month + 2.6) + year_in_century + floor(year_in_century / 4) + floor(century / 4) - 2 * century)% 7
    return ((day_of_week + 5) % 7) +1
