'''
Write a function reverse that accepts a string text as a parameter. 
It returns the reverse of text by reversing all characters in the string.

Here are the tests:

def test_reverse_word():
    assert reverse("cat") == "tac"


def test_reverse_single_character():
    assert reverse("a") == "a"


def test_reverse_empty_string():
    assert reverse("") == ""

'''
def reverse(text):
    # new_string =""
    if text == "":
        return ""
    
    return text[-1]+ reverse(text[:-1])

print(reverse("word"))

def reverse_2(text):
    if text== "":
        return ""
    
    return reverse(text[1:]) + text[0]


print(reverse_2("word"))










# ####SOLUTION#######
# def reverse(text):
#     if len(text) <= 1:
#         return text
#     # Use Python string slicing to get the
#     # first character of text and the
#     # remaining characters
#     first_char = text[:1]
#     remaining_chars = text[1:]
#     return reverse(remaining_chars) + first_char


# def reverse2(text):
#     if text == "":
#         return text
#     else:
#         return text[-1] + reverse(text[:-1])
# # print(reverse2("cat"))
# # print(reverse2("a"))
# # print(reverse2("racecar"))


# def reverse3(text):
#     if text == "":
#         return text
#     else:
#         return reverse(text[1:]) + text[0]
    
# # print(reverse3("cat"))
# # print(reverse3("a"))
# # print(reverse3("racecar"))