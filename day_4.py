from collections import defaultdict
# day 4 - secure container
#
# pw is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only
# ever increase or stay the same (like 111123 or 135679).


def is_a_valid_pw(password, only_two_repeated=False):
    print(f'checking pw {password}')
    # cast to a string for comparisons
    password = str(password)

    # pw has to be 6 chars
    if len(password) != 6:
        return False

    # check for adjacent and decreasing digits
    last_digit = password[0]
    repeating_digits = defaultdict(int)
    for i in range(1, len(password)):
        if int(password[i]) < int(last_digit):
            return False
        if password[i] == last_digit:
            repeating_digits[last_digit] += 1
        last_digit = password[i]

    if not repeating_digits:
        return False

    if only_two_repeated:
        # the value 1 means "1 repeat of a digit" here
        if 1 not in repeating_digits.values():
            return False

    # if we made it here, its all good!
    return True


def count_valid_pws_in_range(start, end, only_two_repeated=False):
    return sum(1 for pw in range(start, end)
               if is_a_valid_pw(pw, only_two_repeated))


assert is_a_valid_pw(111111) is True
assert is_a_valid_pw(223450) is False
assert is_a_valid_pw(123789) is False

# part 1 answer
# print(count_valid_pws_in_range(235741, 706948))

assert is_a_valid_pw(112233, only_two_repeated=True) is True
assert is_a_valid_pw(123444, only_two_repeated=True) is False
assert is_a_valid_pw(111122, only_two_repeated=True) is True

# part 2 answer
print(count_valid_pws_in_range(235741, 706948, only_two_repeated=True))
