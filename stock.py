stock_price = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 140,
    "MSFT" : 330,
    "AMZN" : 130

}

print("Available stocks:",list(stock_price.keys()))

total = 0
result = ""

n = int(input("How many different stocks do you have?"))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity:"))

    if name in stock_price:
        value = stock_price[name] * quantity
        total = total + value
        line = name + ": " +  str(quantity) + " x $" + str(stock_price[name]) + " = $" + str(value)
        print(line)
        result = result + line + "\n"

    else:
        print("Stock not found!")

print("Total Investment : $" + str(total))


result = result + "Total Investment: $" + str(total)
file = open("portfolio_result.txt","w")
file.write(result)
file.close()
print("Result saved in portfolio_result.txt")
