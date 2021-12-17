# # # AGAIN an example of a for loop in pseudocode:
# # # for stock in portfolio:
# # #   Evaluate performance
# # #   Calc Beta
# # #   Calc Ann PN

# # print("-----------------------------------------")

# # # Loop through a range of numbers (0 through 4)
# # for number in range(5):
# #     print(number)

# # print("-----------------------------------------")
# # # Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
# # for x in range(2,7):
# #     print(x)

# # print("-----------------------------------------")
# # word = "bLuE"
# # for letter in word: 
# #     print(letter.swapcase())

# print("-----------------------------------------")
# # Maybe you went on a shopping spree...
# shopping_spree_charges = [117.95, 17, 35, 77.83, 345.67, 45.39, 117.95, 17, 35, 77.83, 345.67, 45.39]
# spending_total = 0.00

# # for charge in shopping_spree_charges:
# #     spending_total += charge # spending_total = spending_total + charge
# #                             # charge = charge + spending_total
# #     print("Inside this loop: $", spending_total)

# for n in range(0, len(shopping_spree_charges)):
#     current_charge = shopping_spree_charges[n]
#     spending_total += current_charge # spending_total = spending_total + charge
#                             # charge = charge + spending_total
#     print(f"Inside this loop ({n}): ${spending_total}")

# print("---------------------------------------------")

# Remember that PL trading log? Lets use it here:
trading_pnl = {
    "03-18-2019": -224,
    "03-19-2019": 352,
    "03-20-2019": 252,
    "03-21-2019": 354,
    "03-22-2019": -544,
    "03-23-2019": -650,
    "03-24-2019": 56,
    "03-25-2019": 123,
    "03-26-2019": -43,
    "03-27-2019": 254,
    "03-28-2019": 325,
    "03-29-2019": -123,
    "03-30-2019": 47,
    "03-31-2019": 321,
    "04-01-2019": 123,
    "04-02-2019": 133,
    "04-03-2019": -151,
    "04-04-2019": 613,
    "04-05-2019": 232,
    "04-06-2019": -311
}

# for key in trading_pnl: #defaults to just the keys
#     print(key)

for key in trading_pnl: #defaults to just the keys
    print(trading_pnl[key])

net_pnl = 0.00

for key in trading_pnl:
    # summing all the trading pnl VALUE
    net_pnl += trading_pnl[key] #Value!
    # inside the for loop
    print("Inside loop:", net_pnl) #this is a global variable

#this is outside the for loop
print("The net pnl for the period was $", round(net_pnl, 2))
