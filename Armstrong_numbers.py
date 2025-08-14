#Problem: Find All Armstrong Numbers Between 100 and 999

for items in range (100,1000):
    hundreds = items // 100
    tens = (items // 10) % 10
    units = items % 10

    sum_of_items =  (hundreds ** 3) + (tens ** 3 ) + (units ** 3)

    if sum_of_items == items:
        print(items) 