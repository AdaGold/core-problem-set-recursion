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

# bunny
# count = [1,2,3,4]
# def bunny(count):
#     pass


# is_nested_parens


