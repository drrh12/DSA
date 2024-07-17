# Linear Arrays
linear_array = [1, 2, 3, 4, 5, 1]
print(f"Linear Array: {linear_array}")
# Multi-dimensional Arrays
multi_array = [[1, 2, 3], 
               [4, 5, 6], 
               [7, 8, 9]]
print(f"Multi-dimensional Array: {multi_array[0][0]}")
# Dynamic Arrays & Operations
dynamic_array = [1, 2, 3]
print(f"Dynamic Array: {dynamic_array}")
#add elements (append)
dynamic_array.append(4) 
print(f"Dynamic Array append: {dynamic_array}")
#extend the list by appending all the items from an iterable
dynamic_array.extend([5, 6, 7])
print(f"Dynamic Array extend: {dynamic_array}")
#find the first element in the list and return its index
print(f"Dynamic Array index: {dynamic_array.index(3)}")
# return the number of times x appears in the list
print(f"Dynamic Array count: {dynamic_array.count(1)}")
# sort the items of the list in place
sort_array = [3, 1, 2, 4]
sort_array.sort()
print(f"Dynamic Array sort: {sort_array}")
#reverse the elements of the list in place
sort_array.reverse()
print(f"Dynamic Array reverse: {sort_array}")
dynamic_array.pop() #remove elements
print(f"Dynamic Array pop: {dynamic_array}")
dynamic_array.pop(1) #remove elements at index
print(f"Dynamic Array pop at index: {dynamic_array}")
dynamic_array.insert(1, 2) #insert elements at index
print(f"Dynamic Array insert at index: {dynamic_array}")
# Jagged (irregular) Arrays
jagged_array = [[1, 2, 3], 
                [4, 5], 
                [6, 7, 8, 9]]
print(f"Jagged Array: {jagged_array[0][0], jagged_array[1][0], jagged_array[2][0]}") 
# shallow copy the list
copy_array = dynamic_array.copy()
print(f"Copy Array: {copy_array}")

# Time 
# O(1) - add/remove at the end
# O(n) - insert/remove elsewhere
