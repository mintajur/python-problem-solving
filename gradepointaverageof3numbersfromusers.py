# Student who has the number below 75 to 79 is B, 80 to 84 is B+ and 85-89 is A and 90 to 100 is A+
print("Enter 3 Numbers to calculate the average grade")
number1 = int(input("Enter score 1: "))
if number1 > 100 or number1 < 0:
    print("User Entered a Wrong Score")
    exit()
number2 =  int (input("Enter score 2: "))
if number2 > 100 or number2 < 0:
    print("User Entered a Wrong Score")
    exit()
number3 = int(input("Enter score 3: "))
if number3 > 100 or number3 < 0:
    print("User Entered a Wrong Score")
    exit()

average = (number1 + number2 + number3) / 3

if average < 75:
    print("You have obtained F")
elif 75 <= average <= 79:
    print("You have obtained B")
elif 80 <= average <= 84:
    print("You have obtained B+")
elif 85 <= average <= 89:
    print("You have obtained A")
elif 90 <= average <= 100:
    print("You have obtained A+")
else:
    print("Nothing")


