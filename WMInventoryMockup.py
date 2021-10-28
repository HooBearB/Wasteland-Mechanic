import time
menu = "inv"
inventory = ["Regular engine", "Economy tire", "Economy tire", "Regular tire", "Commuter radio", "Sport manual"]
trunk = ["Low capacity tank", "Bulletproof tire"]

time.sleep(5)
while 1 == 1:
    if menu == "inv":
        print("┌ < Inventory > ──────────┐")
        x = len(inventory)
        if x == 0:
            print("│ Empty                   │")
        else:
            y = 1
            while x >= y:
                z = 20 - len(inventory[y - 1])
                print("│ " + str(y) + " - " + inventory[y - 1], end = "")
                while z > 0:
                    print(" ", end = "")
                    z = z - 1
                print("│ ")
                y = y + 1
    if menu == "car":
        print("┌ < Car trunk > ──────────┐")
        x = len(trunk)
        if x == 0:
            print("│ Empty                   │")
        else:
            y = 1
            while x >= y:
                z = 20 - len(trunk[y - 1])
                print("│ " + str(y) + " - " + trunk[y - 1], end = "")
                while z > 0:
                    print(" ", end = "")
                    z = z - 1
                print("│ ")
                y = y + 1
            
    print("└─────────────────────────┘")
    print("")
    print("< > Switch inventories")
    print("1. Install item in vehicle")
    print("2. Discard item")
    print("3. Exit menu")
    plr_dec = input(">>> ")
    print("")

    if plr_dec == "1":
        print("Choose part")
        plr_dec = int(input(">>> "))
        print("")
        if menu == "inv":
            print("The " + inventory[plr_dec - 1].lower() + " has been installed in the Fortuna Jet\n")
            inventory.remove(inventory[plr_dec - 1])
        if menu == "car":
            print("The " + trunk[plr_dec - 1].lower() + " has been installed in the Fortuna Jet\n")
            trunk.remove(trunk[plr_dec - 1])
            
    if plr_dec == "2":
        print("Choose part")
        plr_dec = int(input(">>> "))
        print("")
        if menu == "inv":
            print("The " + inventory[plr_dec - 1].lower() + " has been discarded\n")
            inventory.remove(inventory[plr_dec - 1])
        if menu == "car":
            print("The " + trunk[plr_dec - 1].lower() + " has been discarded\n")
            trunk.remove(trunk[plr_dec - 1])

    if plr_dec == "3":
        print("Wasteland Mechanic integration is still in progress.")
        time.sleep(10)

    if plr_dec == ">" or plr_dec == "<":
        if menu == "inv":
            menu = "car"
        else:
            menu = "inv"
