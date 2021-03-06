# Create variables
company_name = "Whole Foods"
years_in_business = 2
hourly_wage = 15.01
expert_status = False

# Print the variables
print(company_name)
print(years_in_business)
print(hourly_wage)
print(expert_status)

# Prints the data type of each declared variable
print("The data type of variable company name is", type(company_name))
print("The data type of variable years is", type(years_in_business))
print("The data type of variable hourly_wage is", type(hourly_wage))
print("The data type of variable expert_status is", type(expert_status))

# Using variable names in calculations
total_miles = 20
gallons_gas = 5 
miles_per_gallon = total_miles / gallons_gas
print(miles_per_gallon)

# Updating variables using assignment
kilometers = 1.60934 * total_miles
print(kilometers)

# Substituting/formatting variable
message = f"Kilometers: {kilometers}."
print(message)

# Two number values will be added
# We can make up anything here.
transaction_1 = 11.75  
'''
Hello

Whatever
'''
transaction_2 = 14.99

total_transation_cost = transaction_1 + transaction_2
print(total_transation_cost)

# Two string values will be concatenated
first_name = "Bill"
last_name = "Stine"

print(first_name, last_name)

full_name = first_name + last_name
print(full_name)
print("My name is " + "" + " " + last_name + ".")
print(f"My name is {first_name} " + last_name + ".")

# Variable naming conventions
mpg = 24 # bad

miles_per_gallon = 24 # BETTER
