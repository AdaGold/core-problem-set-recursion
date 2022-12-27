
'''
Given an array, find the smallest value and move it to the front of the array. Return the same array. Try not to use built-in methods. Don't forget edge cases!

Example Input: [3, 4, 2, 9, 1, 8, 7, 6]
Example Output: [1, 3, 4, 2, 9, 8, 7, 6]

Example Input: [3, 4, 2, 9, 1, 8, 1, 7, 6]
Example Output: [1, 3, 4, 2, 9, 8, 1, 7, 6]

'''
# n = 4
# for i in range(n)[::-1]:
#     print(i)
#     print(range(n-1)[::-1])

arr = [3, 4, 2, 9, 1, 8, 1, 7, 6]


def find_replace(arr):

    smallest = find_smallest(arr)
    
    for idx in range(smallest[1])[::-1]:         

        arr[idx+1] = arr[idx]

    arr[0] = smallest[0]
        
    return arr

def find_smallest(arr):
    smallest = None
    smallest_idx = None
    for i in range(len(arr)):
        if smallest == None or arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest,smallest_idx

# print(find_smallest(arr))
# print(find_replace(arr))