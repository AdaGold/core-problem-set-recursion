# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
        
    if num < 0:
        raise ValueError("Num must be greater than 0")
    else:
        return num * factorial(num - 1)


# reverse
def reverse(text):
    
    if not text or len(text) == 1:
        return text 
    
    else:
        first_element= text[-1]
        last_element = text[0]
        
        small_text = text[1:-1]
        middle_string = reverse(small_text)
        return first_element + middle_string + last_element

# bunny
def bunny(count):
    
    if count == 1:
        return 2
    elif count == 0:
        return 0
    else:
        return 2 + bunny(count -1)


# is_nested_parens
def validate_two_strings(string):

    if string[0] == "(" and string[-1] == ")":
            return True
    

def is_nested_parens(parens):
    if parens == "":
        return True
    else:
        two_strings = parens[0] + parens[-1]
        check_string = validate_two_strings(two_strings)

        if check_string:
            smaller_paren = parens[1:-1]
            return is_nested_parens(smaller_paren)
        else:
            return False

