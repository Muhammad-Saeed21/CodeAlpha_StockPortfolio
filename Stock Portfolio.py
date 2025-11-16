# Project : Stock Portfolio Tracker
# Author : Muhammad Saeed
# Internship : CodeAlpha - Python Programming Internship
# Description : A simple Python program to calculate and save total stock investment with save confirmation.

# Step 1 : Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

# Step 2 : Load previous total if file exists
total_investment = 0
try:
    with open("portfolio.txt", "r") as f:
        data = f.read()
        if data.strip().isdigit():
            total_investment = int(data.strip())
        print(f" Previous Total Investment Loaded : ${total_investment}\n")
except FileNotFoundError:
    print(" No previous record found. Starting fresh.\n")

# Step 3 : Take new input and convert to uppercase
while True:
    stock = input(" Enter stock symbol (AAPL, TSLA, GOOGL, MSFT) or 'done' to finish : ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f" Enter quantity for {stock} : "))
        price = stock_prices[stock]
        investment = quantity * price
        total_investment += investment
        print(f"{stock}: {quantity} × ${price} = ${investment}\n")
    else:
        print(" Invalid stock name. Try again. \n")

# Step 4 : Show total result
print(f" Total Investment Value : ${total_investment}")

# Step 5 : Ask user whether to save file
choice = input("\n Do you want to save this record? (Y/N) : ").upper()

if choice == "Y":
    with open("portfolio.txt", "w") as f:
        f.write(str(total_investment))
    print(" Portfolio saved successfully in 'portfolio.txt'")
else:
    print(" Data not saved. Program ended without writing to file. ")
