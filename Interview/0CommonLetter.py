# Program to find common letters b/w 2 strings

def common_letters():
    str1=input("enter 1st string:\n")
    str2=input("enter 2nd string:\n")
    s1=set(str1)                            #remove duplicate letters and store unique only
    s2=set(str2)
    print(s1)
    print(s2)
    lst = s1 & s2                           # Unique common letters
    print(lst)

common_letters()