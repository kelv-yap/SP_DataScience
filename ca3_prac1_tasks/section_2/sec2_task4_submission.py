number_of_months = 6
title = "Calculate the average of your last " + str(number_of_months) + "-months electricity bills"
print("*" * len(title))
print(title)
print("*" * len(title))

bills = []
bill_number = 1
while bill_number <= number_of_months:
    try:
        input_bill = float(input("Enter Bill #{}: ".format(bill_number)))
        bills.append(input_bill)
        bill_number += 1
    except ValueError:
        print("Please enter a numeric value")

print("Your electricity bills for the past " + str(number_of_months) + " months are:")

bill_str_list = []
for bill in bills:
    bill_str_list.append("$" + str(bill))
print(*bill_str_list, sep=", ")

average = sum(bills) / number_of_months
print("The average of your electricity bill is ${:.2f}".format(average))
