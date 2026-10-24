rent=int(input("Enter your hostel/flat rent ="))
food=int(input("Enter the amount of food ordered ="))
electricity_spent=int(input("Enter the total of electricity spent ="))
charge_per_unit=int(input("Enter the charge per unit ="))
persons=int(input("Enter the number of persons living in room/flat ="))

total_bill=electricity_spent*charge_per_unit

output=(food+rent+total_bill)//persons

print("Each person will pay = ",output)