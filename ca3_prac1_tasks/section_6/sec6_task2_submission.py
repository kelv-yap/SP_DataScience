print("Welcome to SPdonalds!")
print("Below is our Breakfast menu:")
menu_list = [["SPMuffin", 5.00], ["SPancakes", 3.00], ["SPHashbrown", 1.50]]

count = 1
for string in menu_list:
    print("{}.{} (${:.2f})".format(str(count), *string), end=" ")
    count += 1

print()
choice = int(input("Enter your choice of food: "))
index = choice - 1

if choice > len(menu_list):
    print("Sorry, you have entered an invalid choice")
else:
    print("{} ${:.2f} added!".format(*menu_list[index]))

    quantity = int(input("How many {} do you want to order?: ".format(menu_list[index][0])))
    total_cost = float(menu_list[index][1]) * quantity

    print("The total cost for {} {} is ${:.2f}".format(quantity, menu_list[index][0], total_cost))
