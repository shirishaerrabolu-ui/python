def calculate_change(paid, price):
    return paid - price


ticket_price = 25
total_paid = 0


print("Parking ticket price: $25")
print("Accepted coins: 1$, 5$, 10$, 20$")


while True:
    coin = int(input("\nInsert a coin: $"))

    if coin != 1 and coin != 5 and coin != 10 and coin != 20:
        print("Invalid coin!! Please try again.")
        continue

    total_paid += coin
    print("Total paid: $" + str(total_paid))


    if total_paid >= ticket_price:
        break


change = calculate_change(total_paid, ticket_price) 




print("     PAYMENT COMPLETED   ")
print("Ticket price: $" + str(ticket_price))
print("Amount paid: $" + str(total_paid))



if change == 0:
    pass
else:
    print("Change returned: $" + str(change))


print("Parking ticket payment successful1")
print("Thank you!!")



