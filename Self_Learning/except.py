#number = int(input("Enter a number "))          # If not int then error "ValueError: invalid literal for int() with base 10: 'dd'"
#print(number)

################### Error Handling (TRY-EXCEPT) ################

try:
    number = int(input("Enter a number "))         
    print(number)
except:
    print("Invalid Input")    

