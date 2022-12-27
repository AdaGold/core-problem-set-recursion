'''
Write a function factorial that accepts an integer parameter n. It uses recursion to compute and return the value of n factorial (also written as n!).

Here are the tests:

def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positive_num():
    assert factorial(5) == 5 * 4 * 3 * 2 * 1


def test_factorial_negative_num():
    with pytest.raises(ValueError):
        factorial(-1)


'''
def factorial(n):
    
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1        
    return n*factorial(n-1)

print(factorial(0))


####SOLUTION######

def factorial(n):
    if n < 0:
        raise ValueError
    elif n <= 1:
        return 1

    return n * factorial(n-1)

# print(factorial(0))
# print(factorial(0))
# print(factorial(-1))