# Part 2


# search 🔍
def search(unsorted_array, query):
    if len(unsorted_array) == 0:
        return False

    if unsorted_array[-1] == query:
        return True

    return search(unsorted_array[:-1:], query)


# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️


# is_palindrome? 👯‍♀️
def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False

print(is_palindrome("rats live on no evil star"))


# or also 👯‍♀️💡:
def is_palindrome_no_slice(text, first, last):  # helper 🦄
    if (first >= last):
        return True

    if (text[first] == text[last]):
        return is_palindrome_no_slice(text, first+1, last-1)
    else:
        return False


# is_palindrome 👯‍♀️:
def is_palindrome_two(text):
    return is_palindrome_no_slice(text, 0, len(text)-1)

print(is_palindrome_two("rats live on no evil star"))


# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️


# digit_match ✅
def digit_match(num1, num2):
    if (num1 == 0 and num2 == 0):
        return 1
    else:
        return digi_matcher(num1, num2)


def digi_matcher(num1, num2):  # helper 🦄
    if (num1 == 0 or num2 == 0):
        return 0

    num1_mod = num1 % 10
    num2_mod = num2 % 10

    if num1_mod == num2_mod:          
        return 1 + digi_matcher(num1//10, num2//10)

    return digi_matcher(num1//10, num2//10)
