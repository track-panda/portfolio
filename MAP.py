import random

greeting = print("Welcome to South America! For reference, you started in Brazil!")
def brazil(greeting): 
    print("Welcome to Brazil! The capital of Brazil is Brasilia and the primary spoken language is Portuguese.")

def french_guiana():
    print("Welcome to French Guiana! The Capital of French Guiana is Cayenne and the primary spoken language is French.")

def suriname():
    print("Welcome to Suriname! The Capital of Suriname is Paramaribo and the primary spoken language is Dutch.")

def guyana():
    print("Welcome to Guyana! The Capital of Guyana is Georgetown and the primary spoken language is English.")

def venezuela():
    print("Welcome to Venezuela! The Capital of Venezuela is Caracas and the primary spoken language is Spanish.")

def colombia():
    print("Welcome to Colombia! The Capital of Colombia is Bogota and the primary spoken language is Spanish.")

def ecuador(): 
    print("Welcome to Ecuador! The Capital of Ecuador is Quito and the primary spoken language is Spanish.")

def peru():
    print("Welcome to Peru! The Capital of Peru is Lima and the primary spoken language is Spanish.")

def bolivia():
    print("Welcome to Bolivia! The Capital of Bolivia is Sucre and the primary spoken language is Spanish.")

def paraguay():
    print("Welcome to Paraguay! The Capital of Paraguay is Asuncion and the primary spoken language is Spanish.")

def uruguay():
    print("Welcome to Uruguay! The Capital of Uruguay is Montevideo and the primary spoken language is Spanish.")

def argentina():
    print("Welcome to Argentina! The Capital of Argentina is Buenos Aires nd the primary spoken language is Spanish.")

def chile():
    print("Welcome to Chile! The Capital of Chile is Santiago and the primary spoken language is Spanish.")



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "North":
    destinations = [guyana, suriname, french_guiana]
    random.choice(destinations)()
elif travel_direction == "NorthWest":
    places = [colombia, venezuela]
    random.choice(places)()
elif travel_direction == "West":
    peru()
elif travel_direction == "South":
    areas = [bolivia, paraguay, uruguay]
    random.choice(areas)()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "West":
    suriname()
elif travel_direction == "South":
    brazil()
else:
    french_guiana()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "East":
    french_guiana()
elif travel_direction == "West":
    guyana()
elif travel_direction == "South":
    brazil()
else: 
    suriname()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "East":
    suriname()
elif travel_direction == "West":
    venezuela()
elif travel_direction == "South":
    brazil()
else:
    guyana()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "East":
    guyana()
elif travel_direction == "West":
    colombia()
elif travel_direction == "South":
    brazil()
else:
    venezuela()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "North":
    venezuela()
elif travel_direction == "SouthEast":
    brazil()
elif travel_direction == "South":
    peru()
elif travel_direction == "SouthWest":
    ecuador()
else:
    colombia()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "North":
    colombia()
elif travel_direction == "South":
    peru()
else:
    ecuador()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "North":
    colombia()
elif travel_direction == "Northwest":
    ecuador()
elif travel_direction == "East":
    brazil()
elif travel_direction == "Southeast":
    bolivia()
else:
    peru()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "North":
    brazil()
elif travel_direction == "Southeast":
    paraguay()
elif travel_direction == "South":
    argentina()
elif travel_direction == "West":
    peru()
elif travel_direction == "Southwest":
    chile()
else: bolivia()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "NorthWest":
    bolivia()
elif travel_direction == "NorthEast":
    brazil()
elif travel_direction == "South":
    argentina()
else:
    paraguay()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest").strip()

if travel_direction == "North":
    brazil()
elif travel_direction == "West":
    argentina()

else:
    uruguay()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest.").strip()

if travel_direction == "North":
    bolivia()
elif travel_direction == "Northeast":
    paraguay() or brazil()
elif travel_direction == "East":
    uruguay()
elif travel_direction == "West":
    chile()
else:
    argentina()



travel_direction = input("Where would you like to travel to? Options include: North, South, East, West, NorthEast NorthWest, SouthEast, SouthWest.").strip()

if travel_direction == "North":
    peru()
elif travel_direction == "NorthEast":
    bolivia()
elif travel_direction == "East":
    argentina()
else:
    chile()