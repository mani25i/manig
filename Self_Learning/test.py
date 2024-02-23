print(bool("Hello"))
print(bool(15))
print(bool(-1.5))

print("The following will return False:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("##########################################")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Python also has many built-in functions that return a boolean value, like the isinstance() function, 
#which can be used to determine if an object is of a certain data type:
print("Check if an object is an integer or not:")
x = 200
print(isinstance(x, int))
