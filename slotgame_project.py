import random

MAX_LINES = 3
MAX_BET = 1000000000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": {"count": 3, "value": 5},
    "B": {"count": 3, "value": 4},
    "C": {"count": 3, "value": 3},
    "D": {"count": 3, "value": 2}
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, data in symbols.items():
        all_symbols.extend([symbol] * data["count"])

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def get_deposit():
    while True:
        try:
            amount = int(input("Please enter the amount you would like to deposit: $"))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Please enter a valid number")
    return amount


def get_number_of_lines():
    while True:
        try:
            number_of_lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES}): "))
            if 1 <= number_of_lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a valid number between 1 and {MAX_LINES}")
        except ValueError:
            print("Please enter a valid number")
    return number_of_lines


def get_bet(balance):
    while True:
        try:
            bet_amount = int(input(f"Enter your bet amount (Min: {MIN_BET}, Max: {min(MAX_BET, balance)}): $"))
            if MIN_BET <= bet_amount <= min(MAX_BET, balance):
                break
            else:
                print(f"Bet must be between {MIN_BET} and {min(MAX_BET, balance)}")
        except ValueError:
            print("Please enter a valid number")
    return bet_amount


def main():
    balance = get_deposit()
    while True:
        number_of_lines = get_number_of_lines()
        bet_amount = get_bet(balance)
        total_bet = bet_amount * number_of_lines

        if total_bet > balance:
            print("You do not have sufficient funds. Please try again.")
        else:
            break

    print(f"You are betting ${bet_amount} on {number_of_lines} lines. Total bet: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, number_of_lines, bet_amount, symbols)
    print(f"You won ${winnings}!")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("Better luck next time!")

main()
