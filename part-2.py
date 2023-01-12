# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr,q):
    if len(arr) == 0:
        return False
    
    elif arr[0] == q:
        return True
    
    arr.pop(0)   
    return search(arr,q)

print(search(["b", "c", "a"], "a"))

# is_palindrome
def is_palindrome(text):
    if type(text) != str:
        raise TypeError("TypeError")
    
    if len(text) == "" or len(text) == 1:
        return True
    elif text[:1] != text[-1:]:
        return False
        
    return is_palindrome(text[1:-1])


print( is_palindrome("racecar"))

# digit_match
def digit_match(num1, num2, count=0):
    if num1 == 0 and num2 == 0:
        return 1
    
    if num1 == 0 or num2 == 0:
        return count
    
    if num1 == num2:
        count += 1
    elif num1 < 10:
        if num1 == (num2 % 10):
            count += 1
    elif num2 < 10:
        if num2 == (num1 % 10):
            count += 1
    elif num1 % 10 == num2 % 10:
            count += 1
        
    return digit_match(num1//10, num2//10, count)



num1 = 1 #=> 107250389.1 => 1
num2 = 12 #=> 6253084.1 => 1
print(digit_match(num1, num2))