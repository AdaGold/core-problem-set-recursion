# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(list,query):
  if len(list) == 0:
    return False
  if not query == list[0]:
    return search(list[1:],query)
  return True

# is_palindrome

def is_palindrome(word):
  if len(word) <= 1:
    return True
    
  if not word[0] == word[-1]:
    return False

  return is_palindrome(word[1:-1])

# digit_match

def digit_match(first,second):
  match = 0
  if first == "" or second == "":
    return match
  
  if str(first)[-1] == str(second)[-1]:
    match += 1
  
  return match + digit_match(str(first)[:-1],str(second)[:-1])
