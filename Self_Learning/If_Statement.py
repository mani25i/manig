print("###########IF/ELSE############")
is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

print("#############IF/ELIF/ELSE#############################")
    
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("You are tall but not male")
else:
    print("You are neither tall nor male")

print("####################COMPARISON##################")

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2> num1 and num2 > num3:
        return num2
    elif num3> num1 and num3 > num2:
        return num3
    else:
        print("Either ALL or atleast two numbers are same")
    
print(max_num(1, 8, 6))