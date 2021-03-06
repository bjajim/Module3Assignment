# Demonstrate conditional statement

# if True:
#   Do something
# else:
#   Do something else

driverless_car = False

if driverless_car == False:
    # something
    print("Oh no! The driver's asleep! What do we do?!")
    print("Engaging autopilot")
else:
    print("The car is not driverless.")

print("--------------------------")
# Demonstrate conditional with print statement for weather?
# What if it rains?
is_raining = True

if is_raining:
    print("Bring an umbrella!")
else:
    print("Don't forget sunglasses.")

print("-------------------------------")
pedestrian = False

if not pedestrian:
    # do something
    immediate_action = "drive"
else:
    # do other thing
    immediate_action = "stop"

print(immediate_action)
print("-----------------")
x = 1
if x == 1:
    print("x is equal to 1")

print("-----------------")
y = 5
if y == 1:
    print("y is equal to 1")

print("-----------------")
# Or inequality
z = 9
if z != 1: #TRUE
    print("y is not equal to 1")

print("-----------------")
# Declare variables and values for evaluation
x = 1
y = 10

# Multiple conditional can be utilized
if x == 1 and y == 10: 
    print("Both values returned True")

print("-----------------")
# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

print("-----------------")
accident = True
at_fault = False
accident_forgiveness = True
elite_status = True

# eventually change!????
increase_insurance_premium = False

if accident:
    # do something
    if at_fault and accident_forgiveness:
        increase_insurance_premium = False
    elif at_fault and not accident_forgiveness and not elite_status:
        increase_insurance_premium = True
    else:
        increase_insurance_premium = False
elif not accident and elite_status:
    # something
    increase_insurance_premium = False
else: #catch all
    # do something else
    increase_insurance_premium = False

# green if you think insurance will increase TRUE
# red if you think it will not FALSE
print(f"Prediction: {increase_insurance_premium}")