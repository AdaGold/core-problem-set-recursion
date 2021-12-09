# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, target):
    if array == []:
        return False

    if array[0] == target:
        return True
    elif len(array) > 1:
        array = array[1:]
        return search(array, target)
    else:
        return False
    
# print(search(["b", "c", "a"], "a"))
# Output: True

# print(search(["a", "b", "c"], "🌈"))
# Output: False

# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False

# print(is_palindrome("racecar"))
# Output: True

# print(is_palindrome("raecar"))
# Output: False


# digit_match
def digit_match(num1, num2):
    
    num_str1 = str(num1)
    num_str2 = str(num2)

    # base case
    if num_str1 == "" or num_str2 == "":
        return 0

    # recursive step
    if num_str1[-1] == num_str2[-1]:
        match = 1
    elif num_str1[-1] != num_str2[-1]:
        match = 0

    return match + digit_match(num_str1[:-1], num_str2[:-1])

apples = 1072503891
oranges = 62530841
print(digit_match(apples, oranges))
# Output: 

apples = 0
oranges = 62530841
print(digit_match(apples, oranges))
# Output:0


apples = 0
oranges = 0
print(digit_match(apples, oranges))
# Output: 1