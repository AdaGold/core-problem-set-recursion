# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    
    if array == []:    # base case 
        return False
     
    if query == array[-1]:
        return True
    else:
        array.pop()
        return search(array, query)

# is_palindrome
def is_palindrome(string):
    if len(string) <= 1: # base case 
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1]) # recursive case 
    
    return False


# digit_match


def digit_match(num1, num2):
    
    if num1 == 0 and num2 == 0:
        return 1

    if num1 / 10 < 1 or num2 / 10 < 1: 
        if num1 % 10 == num2 % 10:
            return 1
        else:#base case 
            return 0

        
    if num1 % 10  == num2 % 10: # increase count of matches somehow 
        return 1 +  digit_match(num1//10, num2//10) #recursive case 
    # elif num1 == 0 and num2 != 0:
    #     return 0 
    # elif num1 != 0 and num2 == 0: 
    #     return 0 
    else:
            
        return digit_match(num1//10, num2//10)