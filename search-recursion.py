'''
Write a function search that accepts an unsorted array of integers, array, and an integer value to find, query. 
It returns True if query is found in array, and False otherwise. Make the algorithm recursive.

Be sure to implement search using recursion.

Here are the tests:

def test_search_success_unsorted():
    assert search(["b", "c", "a"], "a")


def test_search_empty_array():
    assert not search([], "a")


def test_search_success_first_item():
    assert search(["a", "b", "c"], "a")


def test_search_not_found():
    assert not search(["a", "b", "c"], "🌈")

'''


def search3(array,value):
    #base case
    if len(array) == 0:
        return False
    elif array[0] == value:
        return True
    #recurrsion starts
    return search3(array[1:],value)

print(search3(["a", "b", "c"], "a"))
    
    








def search(array,num):
    if len(array) == 0:
        return False
    elif 1 + search(array[1:], num) == num:
        return True
     
# print(search(["a", "b", "c"], "a")) 

def search2(array,query):
    if len(array) == 0:
        return False
    
    elif array[0] == query:
        return True
    
    return search(array[1:],query)