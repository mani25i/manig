#Problem Statement
#As elements are stored sequentially in a list, we can use a loop to access the elements.
#Try out the below code and observe the different ways of accessing the elements in a list sequentially.
#Note: Iteration in lists can be done using while loop as well.

list_of_airlines=["AI","EM","BA"]

print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])

print("Iterating the list using keyword in")
for airline in list_of_airlines:
    print(airline)

#Note: Here "airline" is just another user defined variable. It is not a keyword.