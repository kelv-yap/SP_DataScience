print("****************************************************************")
print("Calculate the average of your last 6-months electricity bills")
print("****************************************************************")


bill1 = input("Enter Bill #1: ")
bill2 = input("Enter Bill #2: ")
bill3 = input("Enter Bill #3: ")
bill4 = input("Enter Bill #4: ")
bill5 = input("Enter Bill #5: ")
bill6 = input("Enter Bill #6: ")

average = (float(bill1) + float(bill2) + float(bill3) + float(bill4) + float(bill5) + float(bill6)) / 6

print("Your electricity bills for the past 6 months are:")
print("$"+str(bill1)+", " +
      "$"+str(bill2)+", " +
      "$"+str(bill3)+", " +
      "$"+str(bill4)+", " +
      "$"+str(bill5)+", " +
      "$"+str(bill6))
print("The average of your electricity bill is ${:.2f}".format(average))
