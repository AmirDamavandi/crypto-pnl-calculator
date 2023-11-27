# This program calculates crypto profit and loss

# Long Profit Calculator
def long_profit_calculator():
    Quantity = float(input("Quantity (USDT) "))
    Leverage = int(input("Leverage "))
    Entry_price = float(input("Entry Price: "))
    Exit_price = float(input("Exit Price: "))
    if Exit_price < Entry_price:
        return "\nExit price can't be lower than entry price in long positions"
    Calculator = Quantity * Leverage + (Exit_price - Entry_price) / (Entry_price) * 100 - Quantity * Leverage
    Profit = Quantity * Leverage + Calculator / 100 * Quantity * Leverage - Quantity * Leverage
    Result = int(Profit) - 0.05 / 100 * Profit
    return f"\nYour profit including fee will be {round(Result, 3)} USDT plus your quantity your new balance will be {round(Result + Quantity, 3)} USDT"


# Long Loss Calculator
def long_loss_calculator():
    Quantity = float(input("Quantity (USDT) "))
    Leverage = int(input("Leverage "))
    Entry_price = float(input("Entry Price: "))
    Stop_loss = float(input("Exit Price: "))
    if Stop_loss > Entry_price:
        return "\nStop loss can't be higher than entry price in long positions"
    Calculator = Quantity * Leverage - (Stop_loss - Entry_price) / (Entry_price) * 100 - Quantity * Leverage
    Loss = Quantity * Leverage + Calculator / 100 * Quantity * Leverage - Quantity * Leverage
    Result = int(Loss) - 0.05 / 100 * Loss
    if Loss > Quantity:
        Result = 0
        return f"\nYour account will be liquidated"
    else:
        return f"\nYour loss including fee will be {round(Result, 3)} USDT minus your quantity your new balance will be {round(Quantity - Result, 3)} USDT"


# Short Profit Calculator
def short_profit_calculator():
    Quantity = float(input("Quantity (USDT) "))
    Leverage = int(input("Leverage "))
    Entry_price = float(input("Entry Price: "))
    Exit_price = float(input("Exit Price: "))
    if Exit_price > Entry_price:
        return "\nExit price can't be higher than entry price in short positions"
    Calculator = Quantity * Leverage - (Exit_price - Entry_price) / (Entry_price) * 100 - Quantity * Leverage
    Profit = Quantity * Leverage + Calculator / 100 * Quantity * Leverage - Quantity * Leverage
    Result = int(Profit) - 0.05 / 100 * Profit
    return f"\nYour profit including fee will be {round(Result, 3)} USDT plus your quantity your new balance will be {round(Quantity + Result, 3)} USDT"


# Short Loss Calculator
def short_loss_calculator():
    Quantity = float(input("Quantity (USDT) "))
    Leverage = int(input("Leverage "))
    Entry_price = float(input("Entry Price: "))
    Stop_loss = float(input("Exit Price: "))
    if Stop_loss < Entry_price:
        return "\nStop loss can't be lower than entry price in short positions"
    Calculator = Quantity * Leverage + (Stop_loss - Entry_price) / (Entry_price) * 100 - Quantity * Leverage
    Loss = Quantity * Leverage + Calculator / 100 * Quantity * Leverage - Quantity * Leverage
    Result = int(Loss) - 0.05 / 100 * Loss
    if Loss > Quantity:
        Result = 0
        return f"\nYour account will be liquidated"
    else:
        return f"\nYour loss including fee will be {round(Result, 3)} USDT plus your quantity your new balance will be {round(Quantity - Result, 3)} USDT"


def calculate():
    ask_user = input(
        "What do you want to calculate? 1 'long profit', 2 'long loss', 3 'short profit', 4 'short loss'? ")
    if ask_user == "1" or ask_user == "long profit".lower():
        print(long_profit_calculator())
    elif ask_user == "2" or ask_user == "long loss".lower():
        print(long_loss_calculator())
    elif ask_user == "3" or ask_user == "short profit".lower():
        print(short_profit_calculator())
    elif ask_user == "4" or ask_user == "short loss".lower():
        print(short_loss_calculator())
    else:
        print("Invalid choice or please spell it in lowercase character")


calculate()
