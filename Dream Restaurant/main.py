# Menu = {
#     "Kabuli Polao" : 200,
#     "Plain Polao" : 150,
#     "Morog Polao" : 200,
#     "Simple Salad" : 50,
#     "Borhani" : 70,
#     "Badam Shorbbot" : 70,
#     "Soft Drinks" : 25
# }

Kabuli_Polao = 200
Plain_Polao = 150
Morog_Polao = 200
Simple_Salad = 50
Borhani = 70
Badam_Shorbot = 70
Soft_Drinks = 25

total_order = 0

print("Welcome to Python Food Corner!")
print("Here is our menu:\n")

while True:
    print("1. Kabuli Polao: BDT 200")
    print("2. Plain Polao: BDT 150")
    print("3. Morog Polao: BDT 200")
    print("4. Simple Salad: BDT 50")
    print("5. Borhani: BDT 70")
    print("6. Badam Shorbot: BDT 70")
    print("7. Soft Drinks: BDT 25")

    choice = input("\nwhat would you like to take, sir? ")

    if choice == "1":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            print("Enjoy your meal!")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break
    elif choice == "2":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            print("Enjoy your meal!")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break
    elif choice == "3":
        availability = False
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            continue
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            print("Enjoy your meal!")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break
    elif choice == "4":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            print("Enjoy your meal!")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break
    elif choice == "5":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            print("Enjoy your meal!")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break
    elif choice == "6":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            print("Enjoy your meal!")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break
    elif choice == "7":
        availability = False
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            continue
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Kabuli_Polao + total_order
        choice = input("\nAnything else sir? (Yes/No)")
    
        if(choice == "no"):
            print(f"Your tolal bill is BDT {total_order}")
            break

        elif(choice == "yes"):
            pass
    
        else:
            print("Invalid choice")
            print("Make the order again!")
            print(f"Your tolal bill is BDT {total_order}")
            break

    else:
        print("Invalid choice")
        print("Make the order again!")
        break


print("5% off with bkash")
bkash_payment = input("Do you want to pay with bkash? (yes/no)")

if(bkash_payment == "yes"):
    bkash_payment = (total_order - total_order * 0.05)
    print(f"Please pay BDT {bkash_payment} with 5% off")
    print("Enjoy your meal!")
else:
    print(f"Please pay BDT {total_order}")
    print("Enjoy your meal!")
    

    
    




