print("Welcome to the Tip Calculator.")
total_bill=input("The total bill is: $  ")
percentage_tip=input("What percentage of tip would you like to give,10,12 or 15 : ")
number_of_persons=input("Between how many people would you like to split the bill: ")
tip_calculation=(float(total_bill)*int(percentage_tip))/int(100)+float(total_bill)
final_bill_splitting=round(float(tip_calculation)/int(number_of_persons),2)
final_bill_splitting="{:.2f}".format(float(tip_calculation)/int(number_of_persons))
print(f"Each person should pay  $ {final_bill_splitting}")