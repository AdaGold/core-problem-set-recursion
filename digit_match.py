'''
Write a recursive function named digit_match. It accepts two non-negative integers as parameters. It returns the number of digits that match in the two integers.

Two digits match if they are equal and have the same position relative to the end of the number (i.e. starting with the ones digit).

In other words, the function should compare the last digits of each number, 
the second-to-last digits of each number, the third-to-last digits of each number, and so fort, counting how many pairs match.

Example:

First number: 1072503891
Second number: 62530841
Number of matches: 4
Matching pairs: 2-2, 5-5, 8-8, 1-1
1 0 7 2 5 0 3 8 9 1
    | | | | | | | |
    6 2 5 3 0 8 4 1
Here are the tests:

'''


def digit_match(num1,num2):
    count = 0
    
    if num1 == 0 and num2 == 0:
        count = 1
    
    elif num1 == 0 or num2 == 0:
        return count
    
    elif num1%10 == num2%10:
        count+=1
      
    return count+digit_match(num1//10,num2//10)
    
print(digit_match(0,0))



####SOLUTION#####

apples = 0
oranges = 0
def digit_match2(num1,num2):
    count = 0
    # print(num1)
    # print(num2)
    if num1 == 0 or num2 == 0:
        return 0
    
    elif num1%10 == num2%10:
        count = 1
        # print(f"{num1%10}, {num2%10}")
        
    # print("return count here")
    return count + digit_match2(num1//10,num2//10)

# print(digit_match2(apples,oranges))