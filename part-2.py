# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def compare(iterable, n,query):
    if n==len(iterable):
        return False
    if iterable[n] == query:
        return True
    return compare(iterable, n+1, query)

def search(to_search, query):
    return compare(to_search,0,query)


# is_palindrome
def compare(string, a, b):
    if a >=b:
        return True
    if string[a] != string[b]:
        return False
    return compare(string, a+1, b-1)

def is_palindrome(string):
    if len(string)==0:
        return True
        
    b=len(string)-1
    return compare(string, 0, b)
    



# digit_match
def digit_match(apples,oranges):
    if apples==oranges: return len(str(apples))
    elif apples==0 or oranges ==0: return 0
    elif apples<10 and oranges<10:
        if apples== oranges:return 1
        return 0

    a=apples%10
    b=oranges%10
    num = 0
    if a==b:
        num +=1
    return num+ digit_match(apples//10, oranges//10)