#####
#Tip Calculator
#####
#Calculates cost of total meal including tax and tip
#Completed by Anthony Lee
#from Unit1: "Python Syntax" on Codecademy

#Change inputs as needed
meal = 44.50 #raw cost
tax = 0.0675 #tax %
tip = 0.15	 #tip %

meal = meal + meal * tax
total = meal + meal * tip

#print to console
print("Your total is $ %.2f" % total)