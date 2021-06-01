#Recursion Set 

# search
def search(array, query):
    if array == []:
        return False
    if array [0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(str):
    if len(str) <=1:
        return True
    if str [0] != str[-1]:
            return False
    return is_palindrome(str[1:-1])
 


# digit_match
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1
    
    count = 0
    if num1 % 10 == num2 % 10:
        count += 1
    if num1//10 == 0 or num2 //10 == 0:
        return count
    return count + digit_match(num1//10, num2//10)
