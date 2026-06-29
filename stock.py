stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}
total_value = 0
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_value += investment
        print(f"{stock}: ${investment}")
    else:
        print("Stock not found!")
print("\nTotal Portfolio Value: $", total_value)
with open("portfolio.txt", "w") as file:
    file.write(f"Total Portfolio Value: ${total_value}")
print("Result saved in portfolio.txt")
