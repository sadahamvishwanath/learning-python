
print("WELCOME! to your Personal Budget Tracker :] ")
income = int(input("Enter your monthly income: "))
num_categories = input("How many expense categories: ")
cate1 = input("Category 1 name: ")
cate1_amo = float(input(f"Amount spent on {cate1}: "))
cate2 = input("Category 2 name: ")
cate2_amo = float(input(f"Amount spent on {cate2}: "))
cate3 = input("Category 3 name: ")
cate3_amo = float(input(f"Amount spent on {cate3}: "))

#================================================================

total = cate1_amo + cate2_amo  + cate3_amo 
remaining = income  - total
percentage = (total / income) * 100

float(income)
#================================================================
print("\n\n---- Summary ----")
print(f"Income: ${income}")
print(f"Total Expenses {total}")
print(f"Remaining Balance: {remaining}")
print(f"You spent {percentage}% of your income.")
if income > total:
    print("You are within budget. keep it up")
else:
    print("You are over budget. Consider cutting expenses.")