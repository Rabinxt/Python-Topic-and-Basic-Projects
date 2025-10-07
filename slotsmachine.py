#Python Slots Machine
import random
def spin_row():
    symbols = ["🍒", "🍋", "🍉", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    
    
def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    print("*****************************")
    print(" Welcome! to python Slots")
    print(" Symbols : 🍒 🍋 🍉 🔔 ⭐ ")
    print("*****************************")
    while balance > 0 :
        print(f"Current Balance : ${balance}")
        bet = input("Enter Bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number!!!")
            continue
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Funds")
            continue
        if bet <= 0 :
            print("Bet must be greater than 0")
            continue
        balance -= bet
        
        spin = spin_row()
        print(spin)
    

if __name__ == '__main__':
    main()