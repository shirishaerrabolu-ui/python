print("======================================")
print("      🏫 CLASSROOM POINT CALCULATOR")
print("======================================")

team1 = input("Enter Team 1 name: ")
points1 = int(input("Enter Team 1 points: "))

team2 = input("Enter Team 2 name: ")
points2 = int(input("Enter Team 2 points: "))

team3 = input("Enter Team 3 name: ")
points3 = int(input("Enter Team 3 points: "))

total_points = points1 + points2 + points3
average_points = total_points / 3

print()
print("======================================")
print("          CLASSROOM SCOREBOARD")
print("======================================")

print(team1, ":", points1, "points")
print(team2, ":", points2, "points")
print(team3, ":", points3, "points")

print("--------------------------------------")
print("Total Points   :", total_points)
print("Average Points :", average_points)

if points1 > points2 and points1 > points3:
    print("🏆 Winner:", team1)
elif points2 > points1 and points2 > points3:
    print("🏆 Winner:", team2)
elif points3 > points1 and points3 > points2:
    print("🏆 Winner:", team3)
else:
    print("🤝 It's a tie!")

print("======================================")