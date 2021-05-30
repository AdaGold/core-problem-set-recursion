# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
        
    if query == array.pop(0):
        return True
    else:
        return search(array, query)


# is_palindrome
def is_palindrome(text):
    if text == "":
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
def digit_match(num_1, num_2):
    count = 0
    if num_1 // 10 == 0 or num_2 // 10 == 0:
        if num_1 % 10 == num_2 % 10:
            count += 1
        return count
            
    if num_1 % 10 == num_2 % 10:
        count += 1
    num_1 //= 10
    num_2 //= 10
    return count + digit_match(num_1, num_2)

