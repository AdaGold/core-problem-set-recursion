'''
Given two arrays, create your own concatenation function. Return a new array containing the first array's values, then the second array's values. Try not to use built-in methods.  Don't forget edge cases!

Example Input: ["a", "b", "c"], [1, 2, 3]
Example Output: ["a", "b", "c", 1, 2, 3]
'''
array1 = ["a", "b", "c"]
array2 = [1, 2, 3]


def create_array2(array1, array2):
    new_array = (len(array1)+len(array2))*[0]

    counter = 0
    for idx in range(len(array1)):
        new_array[idx] = array1[idx]
        counter+=1

    for idx2 in range(len(array2)):
        new_array[counter] = array2[idx2]
        counter+=1

    return new_array

print(create_array2(array1,array2))    

def create_array(array1,array2):
    new_array =[]
    for item in array1:
        new_array.append(item)
    
    for item in array2:
        new_array.append(item)
    return new_array

# print(create_array(array1,array2))
