# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if array == []:
        return False
    result = array[-1] == query
    if result:
        return True
    return search(array[:-1],query)
    



# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    if len(text)==1:
        return True 
    result = text[0]==text[-1]
    if result == False:
        return False
    return result and is_palindrome(text[1:-1])# decreasing last and first element each time
    


# digit_match
#i cant spot where i am going wrong here
def digit_match(num1,num2):
    count = 0
    if num1 == 0 and num2 == 0:
        return 1
    if num1 == 0 or num2 == 0:
        return 0
    
    result = num1 % 10 == num2 % 10
    if result:
        count = 1
    
    return count + digit_match(num1 // 10, num2 // 10)
