# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, c):
	if not array:
		return False

	if c == array[0]:
		return True
	else:
		return search(array[1:], c)


# is_palindrome
def is_palindrome(text):
    if not text:
        return True
        
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
import math 
def helper(num1, num2):
	n1 = num1 // 10**0 % 10
	n2 = num2 // 10**0 % 10
	return n1, n2

def digit_match(apples, oranges, flag=None):
    # couldn't figure how to return 1 if it starts off as 0
    if apples == 0 or oranges == 0:
        if apples == oranges:
            if not flag:
                return 1
        return 0
        
    n1, n2 = helper(apples, oranges)
    if n1 == n2:
        return digit_match(math.floor(apples/10), math.floor(oranges/10), True) + 1
    else:
        return digit_match(math.floor(apples/10), math.floor(oranges/10), True)


