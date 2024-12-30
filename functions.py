
fruits = ['Bananna', 'Apple', 'Strawberry']
indicies = [0,1,2]
for x in indicies:
    print(x, fruits[x])

def loop_to_ten():

    sum = 0
    while sum < 10:
        print("Keep looping because sum is", sum) 
        sum = sum + 1
loop_to_ten()

def calculate_total_bill(bill, tip_per):
    """Given a bill and a tip percentage, return total amount owed."""

    tip = bill * tip_per
    total = bill+tip
    return total
print(calculate_total_bill(20, 0.10), "$")
my_total=calculate_total_bill(20, 0.2)
print(my_total, "$")

def add(num1, num2):
    """Add two numbers"""
    return num1+ num2
total= add(1,2)
print(total)