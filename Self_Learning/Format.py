"""
 we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string 
where the placeholders {} are:
"""

age = 36.5
txt = "My name is John, and I am {}"
print(txt.format(age))

print("######################################################")

# The format() method takes unlimited number of arguments, and are placed into 
#the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print("######################################################")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))