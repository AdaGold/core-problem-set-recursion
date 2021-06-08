# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    
    if array == []:
        return False

    if array[0] == query:

        return True

    return search(array[1:], query)


# is_palindrome

def is_palindrome(text): # Returns True or False
    
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

# digit_match

def digit_match(first_number, second_number):

    def rec_digit_match(first_number, second_number):

        if first_number == 0:
            return 0
        if second_number == 0:
            return 0
        
        result = 0

        first_last = first_number % 10
        second_last = second_number % 10

        if first_last == second_last:
            result = result + 1

        return result + rec_digit_match(first_number // 10, second_number // 10)

    if first_number == 0 and second_number == 0:
        return 1    

    return rec_digit_match(first_number, second_number)
