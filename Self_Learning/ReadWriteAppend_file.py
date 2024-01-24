"""
############### Read File ######################

emp_file = open ("d:/Python/Self_Learning/employee.txt", "r")      #r=read, w=write(Overwrite), a=append, r+= read and write
print(emp_file.readable())
print(emp_file.read())    
print(emp_file.readline())  
print(emp_file.readlines())

emp_file.close()        #To close the opened file



###################### Write/Append a File ####################
emp_file = open("d:/Python/Self_Learning/employee1.txt", "w")       #Create new File
emp_file.write("\nMani\nNishu\nBavisha")

emp_file.close() 

"""

##################Append a File ####################
emp_file = open("d:/Python/Self_Learning/employee.txt", "a")
emp_file.write("\nMani\nNishu\nBavisha")

emp_file.close() 