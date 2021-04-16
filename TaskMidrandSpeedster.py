driver = int(input("Your current speed in km/h: "))
road = int(input("Average allowed speed of the road: "))

points = (driver-road)/5

print("Points: ", points)

if points > 12:
    print("Time to go to jail!")
if driver < 60:
    print("OK")
