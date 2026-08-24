print("=============================")
print("    FARM HARVEST CALCULATOR")
print("=============================")


field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

total = field1 + field2 + field3 + field4 + field5
print("Total harvest:", total, "kg")


average = total / 5
print("Average yeild", average,"kg")


price_per_kg = 15
earnings = total * price_per_kg
print("Earning: $", earnings)


bags = total // 25
print("Full bags:", bags)


leftover = total % 25
print("Leftover grain:", leftover, "kg")



last_year = 500

print("This year's harvest > last year:", total > last_year)
print("This year's harvest == last year:", total ==last_year)
print("This year's harvest >= last year:", total >= last_year)



total += 30
print("After bonus crop:", total, "kg")


total -= 15
print("After seed reserve:", total, "kg")


bags = total // 25
print("Final number of bags:", bags)


print("==================================")
print("           CALCULATOR COMPLETE")
print("")