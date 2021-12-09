# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    else:
        return array[0] == query or search(array[1:], query)


# is_palindrome
def is_palindrome(text):
	if len(text) <= 1:
		return True
	else:
		return text[0] == text[-1] and is_palindrome(text[1:-1])


# digit_match
def digit_match(m,n):
	m = str(m)
	n = str(n)
	if not m or not n:
		return 0
	else:
		return (1 if m[-1] == n[-1] else 0) + digit_match(m[:-1],n[:-1])

