# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    
    if query!= array[0]:
        return search(array[1:], query)
    else:
        return True


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    first_letter= text[0]
    last_letter = text[len(text)-1]

    if first_letter == last_letter:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(int1, int2):
    if int1==0 and int2 == 0:
        return 1 
    if int1 <10 or int2 <10:
        if int1%10 == int2%10:
            return 1
        else:
            return 0
    if int1%10 == int2%10:
        return digit_match(int1//10, int2//10)+1
    else:
        return digit_match(int1//10, int2//10)

