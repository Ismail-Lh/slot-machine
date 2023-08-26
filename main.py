import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    # Step 1: Creating a list of all symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    # Step 2: Generating each column for the slot machine
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Creating a copy of all symbols list

        # Step 3: Generating symbols for each row in the current column
        for _ in range(rows):
            value = random.choice(
                current_symbols
            )  # Choosing a random symbol from the remaining symbols

            current_symbols.remove(value)  # Removing the chosen symbol from the list
            column.append(value)  # Adding the chosen symbol to the current column

        columns.append(column)  # Adding the column to the list of columns

    return columns  # Returning the list of columns


def deposit():
    while True:
        amount = input("What would like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The deposit amount should be greater than 0!")
        else:
            print("Pleas enter a number!")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the numbers of lines to bet (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Pleas enter a number!")

    return lines


def get_bet():
    while True:
        bet_amount = input("What would like to bet on each line? $")

        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Pleas enter a number!")

    return bet_amount


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet_amount = get_bet()
        total_bet = bet_amount * lines

        if total_bet > balance:
            print(
                f"You do not have enough amount to bet, your current balance is ${balance}"
            )
        else:
            break

    print(
        f"Your are betting ${bet_amount} on {lines} lines. Total bet is equal to ${total_bet}"
    )


main()
