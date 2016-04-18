####
#Vacation Cost Calculator
####
#Calculates total cost of vacation
#Completed by Anthony Lee
#from Unit4: "Functions" on Codecademy

#Hotel cost function
def hotel_cost(nights):
    return 140*nights
    
#Plane ride cost function
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
 
#Rental car cost function       
def rental_car_cost(days):
    if days >= 7: #discount of 50$ if over 7 days
        return 40*days - 50
    elif days >= 3: #discount of 20$ if over 3 days
        return 40*days - 20
    else: #if no discount
        return 40*days

#Total cost of trip
def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
    
print trip_cost("Los Angeles", 5, 600)