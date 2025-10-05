#Python Slots Machine

def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    print("*******************************************************")
    print(" Welcome! to python Slots")
    print(" Symbols : Cherry | Lemon | Watermelon | Bell | Star")
    print("*******************************************************")
    while balance > 0 :
        print(f"Current Balance : ${balance}")
        bet = input("Enter Bet amount " )

if __name__ == '__main__':
    main()