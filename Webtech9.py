print("=== Welcome to Ride Builder! ===")

print("1 - Bike")
print("2 - Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Choose your bike:")
    print("1 - Scooty")
    print("2 - Mountain Bike")

    bike_type = int(input("Enter your choice: "))

    if bike_type == 1:
        print("Scooty - Top speed: 40 km/h")
    else:
        print("Mountain Bike - Top speed: 80 km/h")

elif choice == 2:
    print("Choose your car:")
    print("1 - Sedan")
    print("2 - SUV")                
        
    car_type = int(input("Enter your choice: "))
    
    if car_type == 1:
           print("Sedan - 5 Seats: Useful for Family Trips")
    else:
           print("SUV - 7 Seats: Useful for off-road adventure")

else:
     print("That was not a valid choice")

print("=== Your custom ride is ready! ===")        