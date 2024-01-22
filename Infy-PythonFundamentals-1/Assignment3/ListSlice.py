"""
Problem Statement
Assume that the name of the airlines operating from an airport are stored in a list as shown below.
Suppose we need to extract the airlines from the 1st to the 3rd index positions in the list. How can we do that?

List of airlines

AI

SJ

JA

EM

AA

Index

0

1

2

3

4

Negative Index

-5

-4

-3

-2

-1

Python offers a simple solution in the form of slicing:

sub_list = list_of_airlines[1:4]
The above line provides a sub list from index position 1 to 3 (i.e., 1 to (4-1)). 

Indices may also be considered negative as shown above. This is normally used to count from right.
For example: To fetch the second last airline in the list, we can write list_of_airlines[-2]. 
This is equivalent to list_of_airlines[len(list_of_airlines)-2]. 

Negative indices can also be used for slicing.
For example: list_of_airlines[-4:-1] will give us the same output as list_of_airlines[1:4]

Try out the below code and observe the result. 
Also, assign the following to new_list and observe the results.

list_of_airlines[1:]
list_of_airlines[:2]
list_of_airlines[:-2]
list_of_airlines[-5:]

Also, try out
list_of_airlines[1:-2]
list_of_airlines[:5]
list_of_airlines[-6:]
list_of_airlines[-6:2]
list_of_airlines[-3:5]
"""

list_of_airlines=["AI","SJ","JA","EM","AA"]
new_list=list_of_airlines[1:4]
print(new_list)
new_list=list_of_airlines[-4:-1]
print(new_list)

print(list_of_airlines[1:-2])
print(list_of_airlines[:5])
print(list_of_airlines[-6:])
print(list_of_airlines[-6:2])
print(list_of_airlines[-3:5])

print(list_of_airlines[1:])
print(list_of_airlines[:2])
print(list_of_airlines[:-2])
print(list_of_airlines[-5:])