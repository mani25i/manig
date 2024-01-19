#Problem Statement
#If we just want to find out whether an element is there in a list, we need not iterate through the list. Instead we can check using if..in syntax. Try out the code and observe the results.

list_of_airlines=["AI","EM","BA"]

airline="AI"
if airline in list_of_airlines:
    print("Airline found")
else:
    print("Airline not found")
                                  