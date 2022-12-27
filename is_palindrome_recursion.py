'''Write a recursive function is_palindrome that accepts a string text as a parameter. 
It returns a boolean value indicating whether or not that string is a palindrome .

Input text	Return value
"racecar"	True
"raecar"	False
Here are the tests:

def test_is_palindrome_success():
    assert is_palindrome("racecar")


def test_is_palindrome_not_palindrome():
    assert not is_palindrome("raecar")'''
    
def is_palindrome_loop(word):
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] == word[right]:
            left+=1
            right-=1
        else:
            return False
    return True    
    
# print("Result for loop fuction: ",is_palindrome_loop("raceca"))

def is_palindrom_recursion(word):
    if len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrom_recursion(word[1:-1]) 
    elif word[0] != word[-1]:
        return False
        
print("Result for recursion fuction: ",is_palindrom_recursion("mommmm")) 
        
    

    
#SOLUTION 1
def is_palindrome(text):
    if reverse(text) == text:
        return True
    return False
    
def reverse(text):
    if text == "":
        return text
    else:
        return text[-1] + reverse(text[:-1])
    
#LEARN's SOLUTION

def is_palindrome(text):
    if len(text) <= 1:
        return True
    # Use Python slicing to check if
    # the first character is equal to
    # the last character
    elif text[:1] != text[-1:]:
        return False
    else:
        # Use Python slicing to pass in
        # the substring between the first
        # and last characters of text
        return is_palindrome(text[1:-1])
    