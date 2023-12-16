import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "7️": 2,
    "💎": 4,
    "💸": 6,
    "🍒": 8
}

symbol_value = {
    "7️": 5,
    "💎": 4,
    "💸": 3,
    "🍒": 2
}


def check_winning(slots, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = slots[0][line]
        for column in range(len(slots[0])):
            if symbol != slots[column][line]:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # cloning the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # finds the first instance of this value in the list and removes it
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # by default end is equal to "\n"(new line)
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():  # determines if amount contains only digits, and non-negative
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES}): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        bet = input(f'How much would you like to bet on each line? (bet range: {MIN_BET}-{MAX_BET}): $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter a valid bet amount.")

    return bet


def spin(balance):
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winning(slots, lines, bet, symbol_value)
    if len(winning_lines) > 0:
        print(f'You won ${winning}! 💰')
        print('You won on lines: ', *winning_lines)

    return winning - total_bet


def main():
    balance = deposit()
    while balance > 0:
        print(f'Current balance is ${balance}')
        ans = input('Press any key to spin (q to quit): ')
        if ans == 'q':
            break
        balance += spin(balance)

    print(f'\nYou left with ${balance}.')


main()
