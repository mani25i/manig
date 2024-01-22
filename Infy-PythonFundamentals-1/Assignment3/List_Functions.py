""""
Problem Statement
List data type in Python also have many inbuilt functions.
Consider a list, num_list=[10,20,30,40,50]

Function

Output

Explanation

num_list.append(60)

[10,20,30,40,50,60]

Adds an element to end of list

num_list.index(10)

0

Returns the index position of the element.
In case of multiple occurrence of the element, returns the index of the first occurrence.
Throws ValueError, if the element is not found

num_list.insert(3,60)

[10,20,30,60,40,50]

Inserts an element at a given position

num_list.pop(3)

40

Removes and returns the element at given index position from the list

num_list.remove(30)

[10,20,40,50]

Removes the first occurring element whose value is 30

num_list.sort()

[10,20,30,40,50]

Sorts the list in ascending order

num_list.reverse()

[50,40,30,20,10]

Reverses the list

 

Try out the code which uses the List built-in functions and observe the results.
"""

mark_list=[78,90,90,95,83,95]

mark_pos=mark_list.index(90)
print("Index position of mark 90:", mark_pos)

mark_list.append(54)
print("After adding new marks:",mark_list)

mark_list.insert(2, 98)
print("After inserting 98 at the 2nd index position:",mark_list)

mark_list.pop(1)
print("After removing the marks at the 1st index position:",mark_list)

mark_list.remove(95)
print("After removing the first occurence of 95 from the list:",mark_list)

mark_list.sort()
print("After sorting the marks in the given list:",mark_list)

mark_list.reverse()
print("After reversing the marks in the given list:",mark_list)