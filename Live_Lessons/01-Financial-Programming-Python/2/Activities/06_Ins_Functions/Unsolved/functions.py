def hello():
    print("Hi! This is the hello function.")

def main(stock_ticker):
    print(stock_ticker + " is booming right now!")

hello()
main("apple")

print("======================")

def calculate_market_cap(market_price, number_of_shares):
    cap = market_price * number_of_shares
    return cap

# Initilize some variables to use later.
stock_ticker = "SBUX"
market_price = 114.68
number_of_shares = 1243600000

market_cap = calculate_market_cap(market_price, number_of_shares)
print(f"{stock_ticker} Market Capitalization: {market_cap}")
print(f"Data type of market_cap variable is: {type(market_cap)}")
