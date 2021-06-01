
# search
def search(array, query):
  if len(array) == 0:
    return False
  if array[-1] == query:
    return True
  return  search(array[:-1], query)



# is_palindrome
def is_palindrome(text):
  return len(text) < 2 or text[0] == text[-1] and is_palindrome(text[1:-1])



# digit_match
def digit_match(x, y, match=0):
  strfiedx = str(x)
  strfiedy = str(y)
  if len(strfiedx) == 0 or len(strfiedy) == 0:
        return match
  if strfiedx[-1] == strfiedy[-1]:
    return digit_match(strfiedx[:-1], strfiedy[:-1], match+1) 
  elif strfiedx[-1] != strfiedy[-1]:
    return digit_match(strfiedx[:-1], strfiedy[:-1], match)


