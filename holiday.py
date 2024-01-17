stars = "***********************************************************"
line = "___________________________________________________________"
intro = f"""
{stars}
HOLIDAY COST CALCULATOR
{stars}
Planning your next trip? This holiday cost calculator will
help you budget for it. 

Choose to fly to Edinburgh, Rome or Istanbul, how long you 
would like to stay in a hotel and how long you want to rent 
a car for and will give you your price!

Happy planning!
{line}
"""

print(intro)

while True: 
    city_flight = input("""
We have flights to Edinburgh, Rome and Istanbul. 
Which city would you like to fly to? """).lower()
    if city_flight == "edinburgh" or city_flight =="rome" or city_flight == "istanbul":
        break
    else:
        print("Flights to this destination are unavailable.")

print(line)
while True:
    num_nights = input("How many nights will you be staying in the hotel? ")
    if num_nights.isnumeric():
        num_nights = int(num_nights)
        break
    else:
        print("That is an invalid input. Please enter a whole number of days for your stay.")

print(line)
while True:
    rental_days = input("How many days will you be renting a car for? ")
    if rental_days.isnumeric():
        rental_days = int(rental_days)
        break
    else:
        print("That is an invalid input. Please enter a whole number of days for your car rental.")

def hotel_cost(num_nights):
    if city_flight == "edinburgh":
        return num_nights * 60
    elif city_flight == "rome":
        return num_nights * 100
    elif city_flight == "istanbul":
        return num_nights * 50
    else:
        return "Something went wrong, try again later."


def plane_cost(city_flight):
    if city_flight == "edinburgh":
        return 50
    elif city_flight == "rome":
        return 150
    elif city_flight == "istanbul":
        return 250
    else:
        return "Something went wrong, try again later."


def car_rental(rental_days):
    if city_flight == "edinburgh":
        return 70
    elif city_flight == "rome":
        return 80
    elif city_flight == "istanbul":
        return 40
    else:
        return "Something went wrong, try again later."

def holiday_cost(hotel_cost, plane_cost, car_rental):
    h = hotel_cost(num_nights)
    p = plane_cost(city_flight)
    c = car_rental(rental_days)
    print(f"""
    Cost of flight: £{p}
    Cost of hotel: £{h}
    Cost of car rental: £{c}
    The total cost of your holiday: £{h + p + c}
    """)

holiday_cost(hotel_cost, plane_cost, car_rental)