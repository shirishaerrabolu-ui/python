print("======================================")
print("       WEATHER OUTFIT PICKER")
print("======================================")

# Step 1: Ask for temperature
temperature = int(input("Enter today's temperature in °C: "))

if temperature < 20:
    outfit = "Wear a jacket."
else:
    outfit = "Wear a t-shirt."

# Step 2: Ask about rain
rain = input("Is it raining? (yes/no): ").lower()

if rain == "yes":
    umbrella = "Take an umbrella."
else:
    umbrella = "No umbrella needed."

# Step 3: Ask for wind speed
wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed >= 20:
    windbreaker = "Wear a windbreaker."
else:
    windbreaker = "No windbreaker needed."

# Step 4: Ask about puddles
puddles = input("Are there puddles outside? (yes/no): ").lower()

if puddles == "yes":
    shoes = "Wear boots."
else:
    shoes = "Wear sneakers."

# Step 5: Message outside all blocks
print()
print("Here is your weather outfit recommendation!")

# Step 6: Final outfit summary
print()
print("======================================")
print("          OUTFIT SUMMARY")
print("======================================")
print("Temperature :", temperature, "°C")
print("Outfit      :", outfit)
print("Umbrella    :", umbrella)
print("Windbreaker :", windbreaker)
print("Shoes       :", shoes)
print("======================================")
print("Have a great day!")

