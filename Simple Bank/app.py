#simple banking project
balance = 100

def show_balance():
    print(f"Your balance is BDT {balance:.2f}")

def deposit():
    new_balance = float(input("Enter deposit amount: "))
    if new_balance == 0:
        print("Deposit one Taka minimum") 

    print(f"You deposited BDT{new_balance:.2f}")
    print(f"Your balance is BDT {new_balance:.2f}")
    
    return new_balance

def withdraw():
    new_balance = float(input("Enter withdraw amount: "))
    if new_balance > balance:
        print("Insufficient balance") 
        
    print(f"You have withdrawn BDT{new_balance:.2f}")
    print(f"Your balance is BDT {new_balance:.2f}")

    
    return new_balance


# is_running = True

while True:
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance()
    
    elif choice == "2":
        balance += deposit()

    elif choice == "3":
        balance -= withdraw()

    elif choice == "4":
        print("Program Terminated")
        break

    else:
        print("invalid option")
    

