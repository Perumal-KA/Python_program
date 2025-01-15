# from array import array
#
# arr=array("i",[1,2,4,6,6])
# arr1=array("i",[4,6,78,6,8])
#
# res=list(set(arr)&set(arr1))
# print(res)

from array import array

# Example array
arr = array('i', [1, 2, 4,4,5,6, 6, 8, 5])

# Remove duplicates by converting the array to a set
unique_elements = set(arr)

# Check if there are at least two unique elements
if len(unique_elements) < 2:
    print("Array does not have a second largest element")
else:
    # Sort the unique elements in descending order
    unique_elements = sorted(unique_elements,reverse=True)
    print(unique_elements)
    second_largest=unique_elements[1]
    print(second_largest)

