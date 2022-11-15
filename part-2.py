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
    else:
        return search(array[1:], query)
        


# is_palindrome
def is_palindrome(text):
    if text == "":
        return True
    elif text[0] != text[-1]:
        return False
    else: 
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    #base case: if either of apples or oranges has 1 digit
    if apples < 10 or oranges < 10:
        if apples % 10 == oranges %10:
            return 1
        else:
            return 0
    
    if apples % 10 == oranges % 10:
        #test last digit, and add one if they match. 
        return 1 + digit_match(apples // 10, oranges // 10)
    else:
        return digit_match(apples // 10, oranges // 10)
        

