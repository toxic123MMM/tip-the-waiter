print("welcome to the tip calculator")
bill=float(input("enter the the total bill $"))
tip=int(input("how much tip would you like to give? 10,12,15,20 " ))
num_split=int(input("how many people to split the bill "))
calc_bill=bill*(1+(tip/100))/num_split
final_amount="{:.2f}".format(calc_bill,2)
if tip == 10:
    print(f"each person should pay: ${final_amount}")
elif tip == 12:
    print(f"each person should pay: ${final_amount}")
elif tip == 15:
    print(f"each person should pay: ${final_amount}")
elif tip == 20:
    print(f"each person should pay: ${final_amount}")
else:
    print(f"each person should pay: ${final_amount}")