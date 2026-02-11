import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 3,
    "C" : 4,
    "D" : 6
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []                 
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    
    columns = [[], [] , []]
    for cols in range(cols):
        column = []
        current_symbols = all_symbols[:]                # : is slice operator, without this copy wont work properly
        for rows in range(rows):
            value = random.choice(all_symbols)          #Make a Copy of all symbol list to avoid duplication, e.g, we only 2 As and dont need a third A in teh slot machine
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
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
        lines = input("Enter number of lines to bet on (1- " + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print()
    return lines

def get_bet():
    while True:
        amount = input("Enter amount to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
        return amount

def main():
    balance = deposit()    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet & lines

        if total_bet  >= balance:
            print(f"You donont have enough to bet that amount, your current balance is ${balance}")
        else:
            break
        
    print(f"Your are betting ${bet} on ${lines} lines. Total bet is ${total_bet}")

main()