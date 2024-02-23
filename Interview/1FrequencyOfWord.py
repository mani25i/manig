"""
# Program to find frequency of words in a string.   e.g:"I love you and you love me too"
def freq_words():
    str=input("Enter String:\n")
    li = str.split()
    d={}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)   
 
freq_words()

"""
# Second Way for same program

def freq_words():
    str=input("Enter String:\n")
    li = str.split()
    d={}

    for i in li:
        d[i]=d.get(i,0)+1
    print(d)   
 
freq_words()
