# Write a python program to check whether it contains same number in adjacent position. 
# Display the count of such adjacent occurrences

def get_count(num_list):
    count=0

    # Write your logic here
   
    for i in range (0,len(num_list)-1):
        if (num_list[i]==num_list[i+1]):
            count=count+1
            
        else:
            continue
    return count

num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))