# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(list,query):
    if not query.isalpha():
        return False
    if list == []:
        return False
        
    if list[0] == query:
        return True
    else:
        return search(list[1:],query)
        


# is_palindrome
def is_palindrome(str):
    length = len(str);
    if length <= 1:
        return True
    if str[0] != str[length-1]:
        return False
    return is_palindrome(str[1:length-1])


# digit_match
def digit_match(num1,num2):
    count = 0
    if num1%10 == num2%10:
        count = 1
    
    num1 = num1//10
    num2 = num2//10

    # base
    if num1 == 0 or num2 == 0:
        return count

    return count + digit_match(num1, num2)


