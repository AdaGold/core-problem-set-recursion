# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 1 or n==0:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    if type(text) != str:
        raise TypeError
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]

# print(reverse("cat"))
# output: "tac"

# bunny

def bunny(count):
    if type(count) != int:
        raise TypeError
    if count == 0:
        return 0
    elif count == 1:
        return 2
    return 2 + bunny(count-1)

# print(bunny(50))
# output: 100

# is_nested_parens


