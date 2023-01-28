

bill = 0

print("Welcome to Python Pizza Deliveries!")

size_pizza = input("What size pizza do you want? S, M, or L ")
if size_pizza == "S":
    bill +=15
elif size_pizza == "M":
    bill +=20
elif size_pizza == "L":
    bill +=25

pepperoni = input("Do you want pepperoni? Y or N ")
if pepperoni == "Y":
    if size_pizza == "S":
        bill+=2
    elif size_pizza == "M" or size_pizza == "L":
        bill+=3

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is: ${bill}")
