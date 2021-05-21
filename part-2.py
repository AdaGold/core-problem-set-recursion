# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if array[-1] == query:
      return True
    return search(array[:-1], query)


# is_palindrome
def is_palindrome(text):
    if not len(text):
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
  n = str(apples)
  m = str(oranges)
  if not n or not m:
    return 0
  if n[-1] != m[-1]:
    return digit_match(n[:-1], m[:-1])
  return 1 + digit_match(n[:-1], m[:-1])


