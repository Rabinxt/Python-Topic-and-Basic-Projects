#Python Slots Machine

def spin_row():
    pass

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
        
    

if __name__ == '__main__':
    main()