# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    # base case 
    if query in array:
        return True
    # recursive case



# is_palindrome
def is_palindrome(text):
    # base case # a #ends the recursion # wow # radar # ada 
    # simple problem, cant divide into smaller problems # noon 
    if len(text) == 1 or text == "":
        return True
    # recursive case
    elif first_letter(text):
        return is_palindrome(shrink_input(text))
        # shrink input, pass input back into program 
    else:    
        return False 
    
    
def shrink_input(text):
    return text[1:-1]
    
def first_letter(text):
    return text[0] == text[-1]


# digit_match


def digit_match(apples, oranges):
    # base case 
    # end it if the number is only 0 
    #  apples and oranges are 0 return 1
    if apples == 0 and oranges == 0:
        return 1
    # one or both are 1-digit numbers
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        return 0
    # Recursive Cases
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    return digit_match(apples // 10, oranges // 10)


# return compare each number by checking the remainder and repeat 
# number of matches = 0 
# if num_1[i]% 10 == num_2[i]% 10 
    # 1 += number_of_matches 
# else:     
    # 0 += number_of_matches 
    #return digit_match(move on to the next number) apples[::-1]
    # oranges[::-1]