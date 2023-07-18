# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if len(array) == 0:
        return False

    if array[0] == query:
        return True

    return search(array[1:], query)

# is_palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

# digit_match

def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1  
    
    def count_matching_digits(apples, oranges, count):
        if apples == 0 or oranges == 0:
            return count

        last_digit_apples = apples % 10
        last_digit_oranges = oranges % 10

        if last_digit_apples == last_digit_oranges:
            count += 1

        return count_matching_digits(apples // 10, oranges // 10, count)

    return count_matching_digits(apples, oranges, 0)
