sandwich_orders = ['pastrami', "hamburger", "cheese burger", 'pastrami', "chicken sandwich", 'pastrami', "big mac", "whopper burger" ]
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + " is done\n")