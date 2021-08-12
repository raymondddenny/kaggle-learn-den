# q1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 

    >>> round_to_two_places(3.14159)
    3.14
    """
#     help(round)
    return round(num, ndigits=2)


print(round(2166.086, ndigits=-1))

# q2


def to_smash(total_candies, number_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    If no second argument is provided, it should assume 3 friends, as before.
    >>> to_smash(91)
    1
    """
    return total_candies % number_friends


print(to_smash(101))
print(to_smash(101), 5)

# q3 optional
# cell 1
round_to_two_places(9.9999)

# cell 2
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
# help(abs)

# cell 3
