#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    fivec_needed = rupees_to_make//5 
    if(fivec_needed<=no_of_five):
        five_needed = fivec_needed
    else:
        five_needed=no_of_five
    
    if(rupees_to_make==5*five_needed):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", 0)
    else:
        one_needed=rupees_to_make-(5*five_needed)
        if(one_needed<=no_of_one):
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
            
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)