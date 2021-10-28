def defineGun():
    global gunID
    global gunBaseLine1
    global gunBaseLine2
    global gunBaseLine3
    global gunBaseLine4
    global gunBaseLine5
    global gunBaseLine6

    global gunBarrelLine1
    global gunBarrelLine2
    global gunBarrelLine3
    global gunBarrelLine4
    global gunBarrelLine5
    global gunBarrelLine6

    global gunSightLine1
    global gunSightLine2
    global gunSightLine3
    global gunSightLine4
    global gunSightLine5

    gunID = "MA44"
    gunBaseLine1 = "┌──────────────────┐ ┌┐  "
    gunBaseLine2 = "│            │===│ ╰┬╯╰┐ "
    gunBaseLine3 = "└────────────┬─╥┐    ╲▔  "
    gunBaseLine4 = "             │ ) ╲    ╲  "
    gunBaseLine5 = "             ▔▔▔▔▔╲    ╲ "
    gunBaseLine6 = "                   ╲____╲"

    gunBarrelLine1 = "                         "
    gunBarrelLine2 = "                         "
    gunBarrelLine3 = "                         "
    gunBarrelLine4 = "                         "
    gunBarrelLine5 = "                         "
    gunBarrelLine6 = "                         "

    gunSightLine1 = "            "
    gunSightLine2 = "            "
    gunSightLine3 = "            "
    gunSightLine4 = "            "
    gunSightLine5 = "            "

def modGun():
    global gunID
    global gunBaseLine1
    global gunBaseLine2
    global gunBaseLine3
    global gunBaseLine4
    global gunBaseLine5
    global gunBaseLine6

    global gunBarrelLine1
    global gunBarrelLine2
    global gunBarrelLine3
    global gunBarrelLine4
    global gunBarrelLine5
    global gunBarrelLine6

    global gunSightLine1
    global gunSightLine2
    global gunSightLine3
    global gunSightLine4
    global gunSightLine5

    print("\nSelect a slot to modify.")
    print("1. Gun")
    print("2. Barrel")
    print("3. Sight")
    print("4. Exit menu")
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    if plrinput == 1:
        print("Select a part.")
        print("1. Mariner .44")
        print("2. Mariner .44 Snub")
        print("3. GFP 9mm")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            gunID = "MA44"
            gunBaseLine1 = "┌──────────────────┐ ┌┐  "
            gunBaseLine2 = "│            │===│ ╰┬╯╰┐ "
            gunBaseLine3 = "└────────────┬─╥┐    ╲▔  "
            gunBaseLine4 = "             │ ) ╲    ╲  "
            gunBaseLine5 = "             ▔▔▔▔▔╲    ╲ "
            gunBaseLine6 = "                   ╲____╲"
            gunBarrelLine1 = "                         "
            gunBarrelLine2 = "                         "
            gunBarrelLine3 = "                         "
            gunBarrelLine4 = "                         "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "
            gunSightLine1 = "            "
            gunSightLine2 = "            "
            gunSightLine3 = "            "
            gunSightLine4 = "            "
            gunSightLine5 = "            "
        if plrinput == 2:
            gunID = "MA44S"
            gunBaseLine1 = "       ┌───────────┐  ▁  "
            gunBaseLine2 = "       │     │===│ ╰┬╯╰┐ "
            gunBaseLine3 = "       └─────┬─╥┐    ╲▔  "
            gunBaseLine4 = "             │ ) ╲    ╲  "
            gunBaseLine5 = "             ▔▔▔▔▔╲    ╲ "
            gunBaseLine6 = "                   ╲____╲"
            gunBarrelLine1 = "                         "
            gunBarrelLine2 = "                         "
            gunBarrelLine3 = "                         "
            gunBarrelLine4 = "                         "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "
            gunSightLine1 = "            "
            gunSightLine2 = "            "
            gunSightLine3 = "            "
            gunSightLine4 = "            "
            gunSightLine5 = "            "
        if plrinput == 3:
            gunID = "GFP"
            gunBaseLine1 = "┌────────────────┐       "
            gunBaseLine2 = "│            /// │       "
            gunBaseLine3 = "└──────────┬─╥┐   ╲      "
            gunBaseLine4 = "           │ ) ╲   ╲     "
            gunBaseLine5 = "           ▔▔▔▔▔╲   ╲    "
            gunBaseLine6 = "                 ╲___╲   "
            gunBarrelLine1 = "                         "
            gunBarrelLine2 = "                         "
            gunBarrelLine3 = "                         "
            gunBarrelLine4 = "                         "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "
            gunSightLine1 = "            "
            gunSightLine2 = "            "
            gunSightLine3 = "            "
            gunSightLine4 = "            "
            gunSightLine5 = "            "

        printGun()
            
    if plrinput == 2:
        print("Select a part")
        print("1. Light suppressor")
        print("2. Heavy suppressor")
        print("3. Compensator")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
                
        if plrinput == 1:
            gunBarrelLine1 = "┌───────────────────────┐"
            gunBarrelLine2 = "│      ╱ OSPL ╱         ="
            gunBarrelLine3 = "└───────────────────────┘"
            gunBarrelLine4 = "                         "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "
        if plrinput == 2:
            gunBarrelLine1 = "┌───────────────────────┐"
            gunBarrelLine2 = "│     ╱ OSPH ╱          ="
            gunBarrelLine3 = "│     ------      ┌─────┘"
            gunBarrelLine4 = "└─===─===─===─===─┘      "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "
        if plrinput == 3:
            gunBarrelLine1 = "                  ╔════─┐"
            gunBarrelLine2 = "                  │|||||="
            gunBarrelLine3 = "                  ╚════─┘"
            gunBarrelLine4 = "                         "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "
        if plrinput == 4:
            gunBarrelLine1 = "                  ╔════─┐"
            gunBarrelLine2 = "                  │|||||="
            gunBarrelLine3 = "                  ╚════─┘"
            gunBarrelLine4 = "                         "
            gunBarrelLine5 = "                         "
            gunBarrelLine6 = "                         "

        printGun()

    if plrinput == 3:
        print("Select a part")
        print("1. Holo sight")
        print("2. Delta sight")
        print("3. Hunting scope")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            gunSightLine1 = "                         "
            gunSightLine2 = "                         "
            gunSightLine3 = "                         "
            gunSightLine4 = "            ┌─┬─┐        "
            gunSightLine5 = "      ┌─────┘ │╬│        "
            if gunID == "MA44":
                gunBaseLine1 = "┌─────┴=========┴──┐ ┌┐  "
            if gunID == "GFP":
                gunBaseLine1 = "┌──────┴=========┤       "
        if plrinput == 2:
            gunSightLine1 = "                         "
            gunSightLine2 = "                         "
            gunSightLine3 = "                         "
            gunSightLine4 = "             ╭┬─╮        "
            gunSightLine5 = "           ┌─┘│┬│        "
            if gunID == "MA44":
                gunBaseLine1 = "┌──────────┴====┴──┐ ┌┐  "
            if gunID == "GFP":
                gunBaseLine1 = "┌──────────┴====┴┐       "
        if plrinput == 3:
            gunSightLine1 = "┌┐                     ┌┐"
            gunSightLine2 = "││      _     _        ││"
            gunSightLine3 = "└┼─────┴─┴───┴─┴───────┼┘"
            gunSightLine4 = " │]                   [│ "
            gunSightLine5 = " └─────┬─┬───┬─┬───────┘ "
            if gunID == "MA44":
                gunBaseLine1 = "┌──────╧═╧───╧═╧──┐ ┌┐   "
            if gunID == "MA44S":
                gunBaseLine1 = "       ├═┴───┴═┴───┐  ▁  "
            if gunID == "GFP":
                gunBaseLine1 = "┌──────╧═╧───╧═╧─┐       "

        printGun()

    if plrinput == 4:
        print("WM integration needed")

        

def printGun():
    print("                           " + gunSightLine1)
    print("                           " + gunSightLine2)
    print("                           " + gunSightLine3)
    print("                           " + gunSightLine4)
    print("                           " + gunSightLine5)
    print("  " + gunBarrelLine1 + gunBaseLine1)
    print("  " + gunBarrelLine2 + gunBaseLine2)
    print("  " + gunBarrelLine3 + gunBaseLine3)
    print("  " + gunBarrelLine4 + gunBaseLine4)
    print("  " + gunBarrelLine5 + gunBaseLine5)
    print("  " + gunBarrelLine6 + gunBaseLine6)

    modGun()

    
defineGun()
printGun()
