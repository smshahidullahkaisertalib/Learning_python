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
        print(f"Your tolal bill is BDT {total_order}")
        choice = input("\nAnything else sir? ")
    
        if(choice == "yes"):
            # choice = input("\nwhat would you like to take, sir? ")
            pass
        elif(choice == "no"):
            print("thanks for your order!")
            break
    
    elif choice == "2":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Plain_Polao + total_order
        print(f"Your tolal bill is BDT {total_order}")
        print("Anything else sir?\n") 

    elif choice == "3":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Morog_Polao + total_order
        print(f"Your tolal bill is BDT {total_order}")
        print("Anything else sir?\n")    

    elif choice == "4":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Simple_Salad + total_order
        print(f"Your tolal bill is BDT {total_order}")
        print("Anything else sir?\n") 

    elif choice == "5":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Borhani + total_order
        print(f"Your tolal bill is BDT {total_order}")
        print("Anything else sir?\n")  

    elif choice == "6":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Badam_Shorbot + total_order
        print(f"Your tolal bill is BDT {total_order}")
        print("Anything else sir?\n") 

    elif choice == "7":
        availability = True
        
        if(availability == False):
            print("Sorry sir! This unavailable for now.")
            break
        quantity = int(input("Enter the quantity you need: "))
        total_order = quantity * Soft_Drinks + total_order
        print(f"Your tolal bill is BDT {total_order}")
        print("Anything else sir?\n")   
    

    
    




