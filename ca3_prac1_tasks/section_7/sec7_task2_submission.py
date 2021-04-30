print("This program prints the sum of a range of numbers from x to y")
print("For example, if x is 10 and y is 50, the program will print the sum of numbers from 10 to 50")
x = input("Please enter the value of x: ")
y = input("Please enter the value of y: ")

if not x.isnumeric() or not y.isnumeric():
    print("One or more of your inputs are not numeric!")

elif not int(x) > 0 or not int(y) > 0:
    print("One or more of your inputs are not greater than 0")

elif not int(y) > int(x):
    print("You did not enter a value of y that is greater than x")

else:
    sum_of_numbers = 0
    for number in range(int(x), int(y)+1):
        sum_of_numbers += number
    print("The sum of numbers between {} and {} is {}".format(x, y, sum_of_numbers))
