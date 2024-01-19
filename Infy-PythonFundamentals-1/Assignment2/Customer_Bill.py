
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0.0
    if distance_in_kms >= 0.0 and distance_in_kms <= 3.0:
        if food_type == "V" and quantity_ordered >= 1:
            bill_amount = 120*quantity_ordered
        elif food_type =="N" and quantity_ordered >= 1:
            bill_amount = 150*quantity_ordered
        else:
            bill_amount = -1

    elif distance_in_kms > 3.0 and distance_in_kms <= 6.0:
        if food_type == "V" and quantity_ordered>=1:
            bill_amount = 120*quantity_ordered + 3*distance_in_kms
        elif food_type == "N" and quantity_ordered>=1:
            bill_amount = 150*quantity_ordered + 3*distance_in_kms
        else:
            bill_amount = -1
    elif distance_in_kms > 6.0:
        if food_type == "V" and quantity_ordered>=1:
            bill_amount = 120*quantity_ordered + 6*distance_in_kms
        elif food_type == "N" and quantity_ordered>=1:
            bill_amount = 150*quantity_ordered + 6*distance_in_kms
        else:
            bill_amount = -1
    else:
        bill_amount = -1
    return bill_amount

bill_amount=calculate_bill_amount("N",2,7.0)
print(bill_amount)