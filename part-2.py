# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array,query):
  if len(array) == 0:
    return False
  if array[0] == query:
    return True
  return search(array[1:],query)

# is_palindrome
def search(array,query):
  if len(array) == 0:
    return False
  if array[0] == query:
    return True
  return search(array[1:],query)


# digit_match
def search(array,query):
  if len(array) == 0:
    return False
  if array[0] == query:
    return True
  return search(array[1:],query)

