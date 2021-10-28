"""
 ___      ___     ________     _______    ____________   ________    ___         ________    __________    ________
|\  \  __|\  \   |\   ___ \   |\   ___\  |\____   ____\ |\  _____\  |\  \       |\   ___ \  |\   ____  \  |\  ____ \
\ \  \|\ \ \  \  \ \  \__\ \  \ \  \____ \|___|\  \___| \ \ \_____  \ \  \      \ \  \__\ \ \ \  \__|\  \ \ \ \___|\\
 \ \  \ \ \ \  \  \ \   __  \  \ \____  \     \ \  \     \ \  ____\  \ \  \      \ \   __  \ \ \  \ \ \  \ \ \ \  \ \\
  \ \  \_\ \_\  \  \ \  \|\  \  \|____\  \     \ \  \     \ \ \_____  \ \  \_____ \ \  \|\  \ \ \  \ \ \  \ \ \ \__\/ \
   \ \___________\  \ \__\ \__\   |\______\     \ \  \     \ \______\  \ \_______\ \ \__\ \__\ \ \__\ \ \__\ \ \_______\
    \|___________|   \|__|\|__|   \|______|      \|__|      \|______|   \|_______|  \|__|\|__|  \|__|  \|__|  \|_______|

 ____________    ________    _______    ___  ___    ________    __________    __________   _______ 
|\   __  __  \  |\  _____\  |\  ____\  |\  \ \  \  |\   ___ \  |\   ____  \  |\___   ___\ |\  ____\
\ \  \ \ \|\  \ \ \ \_____  \ \ \___|  \ \  \_\  \ \ \  \__\ \ \ \  \__|\  \ \|__|\  \__| \ \ \___|
 \ \  \ \_\ \  \ \ \  ____\  \ \ \      \ \   __  \ \ \   __  \ \ \  \ \ \  \    \ \  \    \ \ \
  \ \  \|_|\ \  \ \ \ \_____  \ \ \_____ \ \  \ \  \ \ \  \|\  \ \ \  \ \ \  \   _\_\  \___ \ \ \_____
   \ \__\   \ \  \ \ \______\  \ \______\ \ \  \ \  \ \ \__\ \__\ \ \__\ \ \__\ |\_________\ \ \______\
    \|__|    \|__|  \|______|   \|______|  \|__|\|__|  \|__|\|__|  \|__|  \|__| \|_________|  \|______|
"""

#Made by Flint
#Project start: August 26, 2021
#Project end: Not any time soon ;-;
#Version number: v0.1 (PRERELEASE)

"""
Commenting conventions in this program:
I didn't fuckin make any comments lol
Good luck figuring out what the hell this does because I sure can't
"""

"""
v0.1 has:
- Car modification system
- Graphical system for managing and printing ASCII-styled vehicles
- Graphical depiction of broken or fixed parts
- Work order generation
- Money system for buying parts and fixing cars
"""

import random
import time
rand = 0
loop = 0
remove = 0
plrinput = 0
#If something fucks up set debug to 1 and it'll print debug statements as the program runs
debug = 0
#If you don't wanna waste 10 seconds of your life each time you run this thing make this have a value of 1
bypassIntro = 1
money = 500

def changeCarGraphics():
    global plrinput
    global carID
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carEngine
    global carRadiator
    global carTransmission
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2

    if debug == 1:
        print("changeCarGraphics() run!")
        
    if carID == "CAV_ALM1":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine6 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine6 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine6 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine6 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine7 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine7 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine7 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine7 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_ALM2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine6 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine6 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine6 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine6 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine7 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine7 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine7 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine7 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_TRACER":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")
                
        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_OMEGA":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAP":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_SAT1":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_SAT2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")    
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_GEM":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")

        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_M7":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌┬────┬┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌┬────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x────┬┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_M9":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌┬────┬┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌┬────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x────┬┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_M11":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭┬────┬╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭┬────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x────┬╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_MSS":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║  --  ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║  --  x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x  --  ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x  --  x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭┬────┬╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭┬────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x────┬╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_C4":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_RO1":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_RO2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAM2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAM3":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAM4":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")



def modifyCar():
    global money
    global moneySpent
    global plrinput
    global tiresChanged
    global carID
    global carName
    global carLoad
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carStorage1
    global carStorage2
    global carStorage3
    global carStorage4
    global carStorage5
    global carStorage6
    global carStorage7
    global carStorage8
    global carStorage9
    global carStorage10
    global carStorage11
    global carStorage12
    global carStorage13
    global carStorage14
    global carStorage15
    global carStorage16
    global carEngine
    global carRadiator
    global carTransmission
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    plrinput = int(plrinput)

    print("  " + "Select a vehicle slot.")
    print("  " + " 1. Engine")
    print("  " + " 2. Radiator")
    print("  " + " 3. Transmission")
    print("  " + " 4. FL suspension")
    print("  " + " 5. FR suspension")
    print("  " + " 6. RL suspension")
    print("  " + " 7. RR suspension")
    print("  " + " 8. FL tire")
    print("  " + " 9. FR tire")
    print("  " + "10. RL tire")
    print("  " + "11. RR tire")
    print("  " + "12. Battery")
    print("  " + "13. Fuel tank")
    print("  " + "14. L headlight")
    print("  " + "15. R headlight")
    print("  " + "16. L tail light")
    print("  " + "17. R tail light")
    print("  " + "18. Radio")
    print("\n  " + "19. Check manual")
    print("  " + "20. Exit")
    
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    if plrinput == 1:
        print("  " + "Select an engine.")
        print("  " + " 1. Low liter engine  - 150$")
        print("  " + " 2. Economy engine    - 300$")
        print("  " + " 3. Regular engine    - 500$")
        print("  " + " 4. Sport engine      - 750$")
        print("  " + " 5. Heavy duty engine - 850$")
        print("  " + " 6. Remove engine")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carEngine = "Low liter engine"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 2:
            carEngine = "Economy engine"
            money = money - 300
            moneySpent = moneySpent + 300
        if plrinput == 3:
            carEngine = "Regular engine"
            money = money - 500
            moneySpent = moneySpent + 500
        if plrinput == 4:
            carEngine = "Sport engine"
            money = money - 750
            moneySpent = moneySpent + 750
        if plrinput == 5:
            carEngine = "Heavy duty engine"
            money = money - 850
            moneySpent = moneySpent + 850
        if plrinput == 6:
            carEngine = "None"
        plrinput = 0
    if plrinput == 2:
        print("  " + "Select a radiator.")
        print("  " + " 1. Economy radiator     - 100$")
        print("  " + " 2. Regular radiator     - 200$")
        print("  " + " 3. Performance radiator - 350$")
        print("  " + " 4. Heavy duty radiator  - 400$")
        print("  " + " 5. Remove radiator")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carRadiator = "Economy radiator"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carRadiator = "Regular radiator"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carRadiator = "Performance radiator"
            money = money - 350
            moneySpent = moneySpent + 350
        if plrinput == 4:
            carRadiator = "Heavy duty radiator"
            money = money - 400
            moneySpent = moneySpent + 400
        if plrinput == 5:
            carRadiator = "None"
        plrinput = 0
    if plrinput == 3:
        print("  " + "Select a transmission.")
        print("  " + " 1. Regular automatic    - 300$")
        print("  " + " 2. Sport automatic      - 500$")
        print("  " + " 3. Heavy duty automatic - 600$")
        print("  " + " 4. Regular manual       - 250$")
        print("  " + " 5. Sport manual         - 400$")
        print("  " + " 6. Heavy duty manual    - 500$")
        print("  " + " 7. Remove transmission")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTransmission = "Regular automatic"
            money = money - 300
            moneySpent = moneySpent + 300
        if plrinput == 2:
            carTransmission = "Sport automatic"
            money = money - 500
            moneySpent = moneySpent + 500
        if plrinput == 3:
            carTransmission = "Heavy duty automatic"
            money = money - 600
            moneySpent = moneySpent + 600
        if plrinput == 4:
            carTransmission = "Regular manual"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 5:
            carTransmission = "Sport manual"
            money = money - 400
            moneySpent = moneySpent + 400
        if plrinput == 6:
            carTransmission = "Heavy duty manual"
            money = money - 500
            moneySpent = moneySpent + 500
        if plrinput == 6:
            carTransmission = "None"
        plrinput = 0
    if plrinput == 4:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension1 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carSuspension1 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
        if plrinput == 3:
            carSuspension1 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 4:
            carSuspension1 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
        if plrinput == 5:
            carSuspension1 = "None"
        plrinput = 0
    if plrinput == 5:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension2 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carSuspension2 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
        if plrinput == 3:
            carSuspension2 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 4:
            carSuspension2 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
        if plrinput == 5:
            carSuspension2 = "None"
        plrinput = 0
    if plrinput == 6:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension3 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carSuspension3 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
        if plrinput == 3:
            carSuspension3 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 4:
            carSuspension3 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
        if plrinput == 5:
            carSuspension3 = "None"
        plrinput = 0
    if plrinput == 7:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension4 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carSuspension4 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
        if plrinput == 3:
            carSuspension4 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 4:
            carSuspension4 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
        if plrinput == 5:
            carSuspension4 = "None"
        plrinput = 0
    if plrinput == 8:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire1 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
        if plrinput == 2:
            carTire1 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
        if plrinput == 3:
            carTire1 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
        if plrinput == 4:
            carTire1 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
        if plrinput == 5:
            carTire1 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
        if plrinput == 6:
            carTire1 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
        if plrinput == 7:
            carTire1 = "None"
        plrinput = 0
    if plrinput == 9:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire2 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
        if plrinput == 2:
            carTire2 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
        if plrinput == 3:
            carTire2 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
        if plrinput == 4:
            carTire2 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
        if plrinput == 5:
            carTire2 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
        if plrinput == 6:
            carTire2 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
        if plrinput == 7:
            carTire2 = "None"
        plrinput = 0
    if plrinput == 10:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire3 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
        if plrinput == 2:
            carTire3 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
        if plrinput == 3:
            carTire3 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
        if plrinput == 4:
            carTire3 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
        if plrinput == 5:
            carTire3 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
        if plrinput == 6:
            carTire3 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
        if plrinput == 7:
            carTire3 = "None"
        plrinput = 0
    if plrinput == 11:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire4 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
        if plrinput == 2:
            carTire4 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
        if plrinput == 3:
            carTire4 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
        if plrinput == 4:
            carTire4 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
        if plrinput == 5:
            carTire4 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
        if plrinput == 6:
            carTire4 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
        if plrinput == 7:
            carTire4 = "None"
        plrinput = 0
    if plrinput == 12:
        print("  " + "Select a battery.")
        print("  " + " 1. Economy battery     - 100$")
        print("  " + " 2. Low charge battery  - 150$")
        print("  " + " 3. Regular battery     - 200$")
        print("  " + " 4. High charge battery - 300$")
        print("  " + " 5. Heavy duty battery  - 350$")
        print("  " + " 6. Remove battery")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carBattery = "Economy battery"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carBattery = "Low charge battery"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 3:
            carBattery = "Regular battery"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 4:
            carBattery = "High charge battery"
            money = money - 300
            moneySpent = moneySpent + 300
        if plrinput == 5:
            carBattery = "Heavy duty battery"
            money = money - 350
            moneySpent = moneySpent + 350
        if plrinput == 6:
            carBattery = "None"
        plrinput = 0
    if plrinput == 13:
        print("  " + "Select a fuel tank.")
        print("  " + " 1. Low capacity tank  - 75$")
        print("  " + " 2. Regular tank       - 150$")
        print("  " + " 3. High capacity tank - 300$")
        print("  " + " 4. Heavy duty tank    - 325$")
        print("  " + " 5. Remove tank")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carFuelTank = "Low capacity tank"
            money = money - 75
            moneySpent = moneySpent + 75
        if plrinput == 2:
            carFuelTank = "Regular tank"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 3:
            carFuelTank = "High capacity tank"
            money = money - 300
            moneySpent = moneySpent + 300
        if plrinput == 4:
            carFuelTank = "Heavy duty tank"
            money = money - 325
            moneySpent = moneySpent + 325
        if plrinput == 5:
            carFuelTank = "None"
        plrinput = 0
    if plrinput == 14:
        print("  " + "Select a headlight.")
        print("  " + " 1. Regular headlight    - 50$")
        print("  " + " 2. Xenon headlight      - 200$")
        print("  " + " 3. Reinforced headlight - 250$")
        print("  " + " 4. Remove headlight")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carHeadlight1 = "Regular headlight"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carHeadlight1 = "Xenon headlight"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carHeadlight1 = "Reinforced headlight"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carHeadlight1 = "None"
        plrinput = 0
    if plrinput == 15:
        print("  " + "Select a headlight.")
        print("  " + " 1. Regular headlight    - 50$")
        print("  " + " 2. Xenon headlight      - 200$")
        print("  " + " 3. Reinforced headlight - 250$")
        print("  " + " 4. Remove headlight")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carHeadlight2 = "Regular headlight"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carHeadlight2 = "Xenon headlight"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carHeadlight2 = "Reinforced headlight"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carHeadlight2 = "None"
        plrinput = 0
    if plrinput == 16:
        print("  " + "Select a tail light.")
        print("  " + " 1. Regular tail light    - 50$")
        print("  " + " 2. LED tail light        - 200$")
        print("  " + " 3. Reinforced tail light - 250$")
        print("  " + " 4. Remove tail light")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTailLight1 = "Regular tail light"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carTailLight1 = "LED tail light"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carTailLight1 = "Reinforced tail light"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carTailLight1 = "None"
        plrinput = 0
    if plrinput == 17:
        print("  " + "Select a tail light.")
        print("  " + " 1. Regular tail light    - 50$")
        print("  " + " 2. LED tail light        - 200$")
        print("  " + " 3. Reinforced tail light - 250$")
        print("  " + " 4. Remove tail light")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTailLight2 = "Regular tail light"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carTailLight2 = "LED tail light"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carTailLight2 = "Reinforced tail light"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carTailLight2 = "None"
        plrinput = 0
    if plrinput == 18:
        print("  " + "Select a radio.")
        print("  " + " 1. Commuter radio - 150$")
        print("  " + " 2. CB radio       - 325$")
        print("  " + " 3. Military radio - 1000$")
        print("  " + " 4. Remove radio")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carRadio = "Commuter radio"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 2:
            carRadio = "CB radio"
            money = money - 325
            moneySpent = moneySpent + 325
        if plrinput == 3:
            carRadio = "Military radio"
            money = money - 1000
            moneySpent = moneySpent + 1000
        if plrinput == 4:
            carRadio = "None"
        plrinput = 0
    if plrinput == 19:
        checkManual(carID, 1)
    if plrinput == 20:
        if money < 0:
            print("\n  You leave the scrap yard after giving the manager an I.O.U.")
            time.sleep(1)
        drawInspectionMenu()



def generateWorkCar():
    global moneySpent
    global plrinput
    global carID
    global carName
    global carLoad
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carEngine
    global carRadiator
    global carTransmission
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    if debug == 1:
        print("generateWorkCar variables globalized!")
    rand = random.randint(1, 18)
    if debug == 1:
        print("rand randomized!")

    if rand == 1:
        carID = "CAV_ALM1"
        carName = "1st GEN CAVICE ALMADA"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│      │"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "║      ║"
        carLine7 = "└──────┘"
        carLine8 = "        "
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Economy engine"
        carRadiator = "Economy radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Economy tire"
        carTire2 = "Economy tire"
        carTire3 = "Economy tire"
        carTire4 = "Economy tire"
        carBattery = "Economy battery"
        carFuelTank = "Low capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")


    if rand == 2:
        carID = "CAV_ALM2"
        carName = "2nd GEN CAVICE ALMADA"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│┌─┐┌─┐│"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "║      ║"
        carLine7 = "└──────┘"
        carLine8 = "        "
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "
        
        carEngine = "Economy engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Economy tire"
        carTire2 = "Economy tire"
        carTire3 = "Economy tire"
        carTire4 = "Economy tire"
        carBattery = "Economy battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 3:
        carID = "CAV_TRACER"
        carName = "CAVICE TRACER"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌────┐│"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 4:
        carID = "CAV_OMEGA"
        carName = "CAVICE OMEGA"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 5:
        carID = "CAV_CAP"
        carName = "CAVICE CAPACITY"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│┌────┐│"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 6:
        carID = "CAV_SAT1"
        carName = "1st GEN CAVICE SATELLITE"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Sport tire"
        carTire2 = "Sport tire"
        carTire3 = "Sport tire"
        carTire4 = "Sport tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 7:
        carID = "CAV_SAT2"
        carName = "2nd GEN CAVICE SATELLITE"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Sport tire"
        carTire2 = "Sport tire"
        carTire3 = "Sport tire"
        carTire4 = "Sport tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 8:
        carID = "CAV_GEM"
        carName = "CAVICE GEMINI"
        carLoad = [ ]
        carLine1 = "╭──────╮"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│ ┌──┐ │"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Sport tire"
        carTire2 = "Sport tire"
        carTire3 = "Sport tire"
        carTire4 = "Sport tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 9:
        carID = "CAV_M7"
        carName = "7th GEN CAVICE M-SERIES"
        carLoad = [ ]
        carLine1 = "┌┬────┬┐"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "│└────┘│"
        carLine5 = "├──────┤"
        carLine6 = "│┌────┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "└──────┘"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Regular manual"
        carSuspension1 = "Offroad suspension"
        carSuspension2 = "Offroad suspension"
        carSuspension3 = "Offroad suspension"
        carSuspension4 = "Offroad suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "None"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 10:
        carID = "CAV_M9"
        carName = "9th GEN CAVICE M-SERIES"
        carLoad = [ ]
        carLine1 = "┌┬────┬┐"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "││┆┆┆┆││"
        carLine5 = "├┴────┴┤"
        carLine6 = "│┌────┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "└──────┘"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "Offroad suspension"
        carSuspension2 = "Offroad suspension"
        carSuspension3 = "Offroad suspension"
        carSuspension4 = "Offroad suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 11:
        carID = "CAV_M11"
        carName = "11th GEN CAVICE M-SERIES"
        carLoad = [ ]
        carLine1 = "╭┬────┬╮"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "││┆┆┆┆││"
        carLine5 = "├┴────┴┤"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Heavy duty engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Heavy duty automatic"
        carSuspension1 = "Heavy duty suspension"
        carSuspension2 = "Heavy duty suspension"
        carSuspension3 = "Heavy duty suspension"
        carSuspension4 = "Heavy duty suspension"
        carTire1 = "Heavy duty tire"
        carTire2 = "Heavy duty tire"
        carTire3 = "Heavy duty tire"
        carTire4 = "Heavy duty tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 12:
        carID = "CAV_MSS"
        carName = "CAVICE M-SERIES SUPER SWAMPER"
        carLoad = [ ]
        carLine1 = "╭┬────┬╮"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "││┆┆┆┆││"
        carLine5 = "├┴────┴┤"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║  --  ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "Heavy duty suspension"
        carSuspension2 = "Heavy duty suspension"
        carSuspension3 = "Heavy duty suspension"
        carSuspension4 = "Heavy duty suspension"
        carTire1 = "Offroad tire"
        carTire2 = "Offroad tire"
        carTire3 = "Offroad tire"
        carTire4 = "Offroad tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 13:
        carID = "CAV_C4"
        carName = "4th GEN CAVICE C-SERIES"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "│      │"
        carLine3 = "║      ║"
        carLine4 = "│      │"
        carLine5 = "│      │"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Heavy duty engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "CB radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 14:
        carID = "CAV_RO1"
        carName = "1st GEN CAVICE ROAMER"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "│┌────┐│"
        carLine3 = "║      ║"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│      │"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 15:
        carID = "CAV_RO2"
        carName = "2nd GEN CAVICE ROAMER"
        carLoad = [ ]
        carLine1 = "╭──────╮"
        carLine2 = "│┌────┐│"
        carLine3 = "║      ║"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│      │"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"

    if rand == 16:
        carID = "CAV_CAM2"
        carName = "2nd GEN CAVICE CAMBIO"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "│      │"
        carLine3 = "╟──────╢"
        carLine4 = "│┌────┐│"
        carLine5 = "├──────┤"
        carLine6 = "│  --  │"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Sport manual"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"


    if rand == 17:
        carID = "CAV_CAM3"
        carName = "3rd GEN CAVICE CAMBIO"
        carLoad = [ ]
        carLine1 = "┌──────┐"
        carLine2 = "│ ==== │"
        carLine3 = "╟──────╢"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"

    if rand == 18:
        carID = "CAV_CAM4"
        carName = "4th GEN CAVICE CAMBIO"
        carLoad = [ ]
        carLine1 = "╭──────╮"
        carLine2 = "│      │"
        carLine3 = "╟──────╢"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│  ==  │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"

    moneySpent = 0
    makeWorkOrder()



def makeWorkOrder():
    global requirement
    global formRequirement
    global reqCode
    global carEngine
    global carRadiator
    global carTransmission
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    ##I roll up to garaaaage yeeeeah
    global rollUp
    global tiresChanged
    
    rand = random.randint(1,100)
    if rand != 1:
        rollUp = "drives up to"
    if rand == 1:
        rollUp = "rolls up to"
    rand = random.randint(1, 10)
    
    if rand == 1:
        rand = random.randint(1,4)
        requirement = "replace one of the tires."
        formRequirement = "replace the flat tire."
        reqCode = "oneTire"
        tiresChanged = 0
        if rand == 1:
            carTire1 = "None"
        if rand == 2:
            carTire2 = "None"
        if rand == 3:
            carTire3 = "None"
        if rand == 4:
            carTire4 = "None"

    if rand == 2:
        rand = random.randint(1,4)
        requirement = "replace some of the tires."
        formRequirement = "replace the two flat tires."
        reqCode = "oneTire"
        tiresChanged = 0
        if rand == 1:
            carTire1 = "None"
        if rand == 2:
            carTire2 = "None"
        if rand == 3:
            carTire3 = "None"
        if rand == 4:
            carTire4 = "None"
        rand = random.randint(1,4)
        if rand == 1:
            carTire1 = "None"
        if rand == 2:
            carTire2 = "None"
        if rand == 3:
            carTire3 = "None"
        if rand == 4:
            carTire4 = "None"
        rand = random.randint(1,10)
        if rand == 1:
            rollUp = "is towed into"
        if rand != 1:
            rollUp = "is pushed into"
        
    if rand == 3:
        requirement = "replace the battery."
        formRequirement = "replace the dead battery."
        reqCode = "battery"
        carBattery = "Dead battery"
        
    if rand == 4:
        requirement = "install a two way radio."
        formRequirement = "install a CB radio."
        reqCode = "cb"
        carRadio = "None"
        
    if rand == 5:
        requirement = "replace the radiator."
        formRequirement = "replace the broken radiator."
        reqCode = "badRad"
        carRadiator = "Broken radiator"
        
    if rand == 6:
        requirement = "replace the headlight."
        formRequirement = "replace the broken headlight."
        reqCode = "smashedHeadlamp"
        rand = random.randint(1,2)
        if rand == 1:
            carHeadlight1 = "None"
        if rand == 2:
            carHeadlight2 = "None"

    if rand == 7:
        requirement = "replace the tail light."
        formRequirement = "replace the broken tail light."
        reqCode = "smashedTailLamp"
        rand = random.randint(1,2)
        if rand == 1:
            carTailLight1 = "None"
        if rand == 2:
            carTailLight2 = "None"
            
    if rand == 8:
        requirement = "fix the engine."
        formRequirement = "replace the broken engine."
        reqCode = "bustEngine"
        carEngine = "Busted engine"
        rand = random.randint(1,10)
        if rand == 1:
            rollUp = "is towed into"
        if rand != 1:
            rollUp = "is pushed into"
            
    if rand == 9:
        requirement = "replace the transmission."
        formRequirement = "replace the broken transmission."
        reqCode = "badTransmission"
        carTransmission = "Broken transmission"
        
    if rand == 10:
        requirement = "replace the leaking fuel tank."
        formRequirement = "replace the punctured fuel tank."
        reqCode = "leaker"
        carFuelTank = "Punctured fuel tank"
        rand = random.randint(1,10)
        if rand == 1:
            rollUp = "is towed into"
        if rand != 1:
            rollUp = "is pushed into"

    if rand == 11:
        requirement = "replace the broken radio."
        formRequirement = "replace the broken radio."
        reqCode = "badRadio"
        carRadio = "Broken radio"

    changeCarGraphics()

    print("\n  A car " + rollUp + " the garage.")
    time.sleep(2)
    print("\n  It is a")

    print("  " + carName + "\n")
    print("  " + "The customer says to " + requirement + " You write this down.\n")
    print("  " + carLine1)
    print("  " + carLine2 + "       From initial inspection")
    print("  " + carLine3 + "       it appears that the car")
    print("  " + carLine4 + "       has the following parts:")
    print("  " + carLine5 + "            FL tire: " + carTire1)
    print("  " + carLine6 + "            FR tire: " + carTire2)
    print("  " + carLine7 + "            RL tire: " + carTire3)
    print("  " + carLine8 + "            RR tire: " + carTire4)
    print("  " + carLine9 + "        L headlight: " + carHeadlight1)
    print("  " + carLine10 + "        R headlight: " + carHeadlight2)
    print("  " + carLine11 + "       L tail light: " + carTailLight1)
    print("  " + carLine14 + "       R tail light: " + carTailLight2)
    print("  " + carLine15)
    print("  " + carLine16)
    print("  " + carLine17)
    print("  " + carLine18)
    print("")
    print("  " + "You have " + str(money) + "$")

    print("\n1. Inspect the vehicle further")
    print("2. Check work order")
    print("3. Modify vehicle")
    print("4. Send vehicle off")
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    if plrinput == 1:
        drawInspectionMenu()
    if plrinput == 2:
        checkWorkOrder()
    if plrinput == 3:
        while plrinput != 20:
            modifyCar()
    if plrinput == 4:
        checkVehicle()



def checkVehicle():
    global money
    global rand

    print("")
    if reqCode == "oneTire":
        if carTire1 == carTire2 == carTire3 == carTire4 != "None":
            print("  The customer says thanks and leaves after paying.")
            if carTire1 == "Economy tire":
                rand = random.randint(75, 125)
                rand = rand * tiresChanged
            if carTire1 == "Regular tire":
                rand = random.randint(125, 200)
                rand = rand * tiresChanged
            if carTire1 == "Sport tire":
                rand = random.randint(200, 350)
                rand = rand * tiresChanged
            if carTire1 == "Heavy duty tire":
                rand = random.randint(250, 425)
                rand = rand * tiresChanged
            if carTire1 == "Offroad tire":
                rand = random.randint(300, 525)
                rand = rand * tiresChanged
            if carTire1 == "Bulletproof tire":
                rand = random.randint(400, 700)
                rand = rand * tiresChanged
        if carTire1 == "None" or carTire2 == "None" or carTire3 == "None" or carTire4 == "None":
            print("  The customer says that there are still missing tires,\n  and they leave without paying.")
        if carTire1 != carTire2 or carTire2 != carTire3 or carTire3 != carTire4 or carTire1 != carTire4:
            print("  The customer says the tires are mismatched,\n  and they leave after paying half price.")

    if reqCode == "twoTires":
        if carTire1 == carTire2 == carTire3 == carTire4 != "None":
            print("  The customer says thanks and leaves after paying.")
            if carTire1 == "Economy tire":
                rand = random.randint(75, 125)
                rand = rand * tiresChanged
            if carTire1 == "Regular tire":
                rand = random.randint(125, 200)
                rand = rand * tiresChanged
            if carTire1 == "Sport tire":
                rand = random.randint(200, 350)
                rand = rand * tiresChanged
            if carTire1 == "Heavy duty tire":
                rand = random.randint(250, 425)
                rand = rand * tiresChanged
            if carTire1 == "Offroad tire":
                rand = random.randint(300, 525)
                rand = rand * tiresChanged
            if carTire1 == "Bulletproof tire":
                rand = random.randint(400, 700)
                rand = rand * tiresChanged
        if carTire1 == "None" or carTire2 == "None" or carTire3 == "None" or carTire4 == "None":
            print("  The customer says that there are still missing tires,\n  and they leave without paying.")
        if carTire1 != carTire2 or carTire2 != carTire3 or carTire3 != carTire4 or carTire1 != carTire4:
            print("  The customer says the tires are mismatched,\n  and they leave after paying half price.")

    if reqCode == "battery":
        if carBattery != "None" and carBattery != "Dead battery":
            print("  The customer says thanks and leaves after paying.")
            if carBattery == "Economy battery":
                rand = random.randint(100, 200)
            if carBattery == "Low charge battery":
                rand = random.randint(150, 275)
            if carBattery == "Regular battery":
                rand = random.randint(200, 350)
            if carBattery == "High charge battery":
                rand = random.randint(300, 500)
            if carBattery == "Heavy duty battery":
                rand = random.randint(350, 575)
        if carBattery == "None" or carBattery == "Dead battery":
            print("  The customer says that the car still won't start,\n  and they leave without paying.")

    if reqCode == "cb":
        if carRadio == "CB radio":
            print("  The customer says thanks and leaves after paying.")
            rand = random.randint(325, 475)
        if carRadio != "CB radio":
            print("  The customer says that the car still doesn't have a CB radio,\n  and they leave without paying.")

    if reqCode == "badRad":
        if carRadiator != "None" and carRadiator != "Broken radiator":
            print("  The customer says thanks and leaves after paying.")
            if carRadiator == "Economy radiator":
                rand = random.randint(100, 225)
            if carRadiator == "Regular radiator":
                rand = random.randint(200, 325)
            if carRadiator == "Performance radiator":
                rand = random.randint(350, 475)
            if carRadiator == "Heavy duty radiator":
                rand = random.randint(400, 650)
        if carRadiator == "None" or carRadiator == "Broken radiator":
            print("  The customer says that the car still overheats,\n  and they leave without paying.")

    if reqCode == "smashedHeadlamp":
        if carHeadlight1 != "None" and carHeadlight2 != "None":
            print("  The customer says thanks and leaves after paying.")
            if carHeadlight1 == "Regular headlight":
                rand = random.randint(50, 150)
            if carHeadlight1 == "Xenon headlight":
                rand = random.randint(200, 350)
            if carHeadlight1 == "Reinforced headlight":
                rand = random.randint(250, 400)
        if carHeadlight1 == "None" or carHeadlight2 == "None":
            print("  The customer says that there are still missing headlights,\n  and they leave without paying.")
        if carHeadlight1 != carHeadlight2 and carHeadlight1 != "None" and carHeadlight2 != "None":
            print("  The customer says the headlights are mismatched,\n  and they leave after paying half price.")

    if reqCode == "bustEngine":
        if carEngine != "None" and carEngine != "Busted engine":
            print("  The customer says thanks and leaves after paying.")
            if carEngine == "Low liter engine":
                rand = random.randint(150, 250)
            if carEngine == "Economy engine":
                rand = random.randint(300, 475)
            if carEngine == "Regular engine":
                rand = random.randint(500, 650)
            if carEngine == "Sport engine":
                rand = random.randint(750, 900)
            if carEngine == "Heavy duty engine":
                rand = random.randint(850, 1050)
        if carEngine == "None" or carEngine == "Busted engine":
            print("  The customer says that the car still doesn't have a working engine,\n  and they leave without paying.")

    if reqCode == "badTransmission":
        if carTransmission != "None" and carTransmission != "Broken transmission":
            print("  The customer says thanks and leaves after paying.")
            if carTransmission == "Regular automatic":
                rand = random.randint(300, 450)
            if carTransmission == "Sport automatic":
                rand = random.randint(500, 675)
            if carTransmission == "Heavy duty automatic":
                rand = random.randint(600, 750)
            if carTransmission == "Regular manual":
                rand = random.randint(250, 350)
            if carTransmission == "Sport manual":
                rand = random.randint(400, 525)
            if carTransmission == "Heavy duty manual":
                rand = random.randint(500, 650)
        if carTransmission == "None" or carTransmission == "Broken transmission":
            print("  The customer says that the car still doesn't shift right,\n  and they leave without paying.")

    if reqCode == "leaker":
        if carFuelTank != "None" and carFuelTank != "Punctured fuel tank":
            print("  The customer says thanks and leaves after paying.")
            if carFuelTank == "Low capacity tank":
                rand = random.randint(75, 125)
            if carFuelTank == "Normal tank":
                rand = random.randint(150, 225)
            if carFuelTank == "High capacity tank":
                rand = random.randint(300, 425)
            if carFuelTank == "Heavy duty tank":
                rand = random.randint(325, 450)
        if carFuelTank == "None" or carFuelTank == "Punctured fuel tank":
            print("  The customer says that the car still leaks fuel,\n  and they leave without paying.")

    if reqCode == "badRadio":
        if carRadio != "None" and carRadio != "Broken radio":
            print("  The customer says thanks and leaves after paying.")
            if carRadio == "Commuter radio":
                rand = random.randint(150, 350)
            if carRadio == "CB radio":
                rand = random.randint(325, 550)
            if carRadio == "Military radio":
                rand = random.randint(1000, 1300)
        if carRadio == "None" or carRadio == "Punctured fuel tank":
            print("  The customer says that the car still leaks fuel,\n  and they leave without paying.")

    print("  + " + str(rand) + "$")
    print("  This is a " + str(rand - moneySpent) + "$ profit.")
    money = money + rand
        
    time.sleep(1.5)
    print("\n")
    print("  You wait a while. \n")
    time.sleep(1.5)
    generateWorkCar()



def checkManual(entry, read):
    if entry == "CAV_ALM1":
        manualCarName = "1st GEN CAVICE ALMADA"
        manualCarEngine = "Economy engine"
        manualCarRadiator = "Economy radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Economy tire"
        manualCarBattery = "Economy battery"
        manualCarFuelTank = "Low capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_ALM2":
        manualCarName = "2nd GEN CAVICE ALMADA"
        manualCarEngine = "Economy engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Economy tire"
        manualCarBattery = "Economy battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_TRACER":
        manualCarName = "CAVICE TRACER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_OMEGA":
        manualCarName = "CAVICE OMEGA"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAP":
        manualCarName = "CAVICE CAPACITY"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_SAT1":
        manualCarName = "1st GEN CAVICE SATELLITE"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Sport tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_SAT2":
        manualCarName = "2nd GEN CAVICE SATELLITE"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Sport tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_GEM":
        manualCarName = "CAVICE GEMINI"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Sport tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_M7":
        manualCarName = "7th GEN CAVICE M-SERIES"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Regular manual"
        manualCarSuspension = "Offroad suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "None"

    if entry == "CAV_M9":
        manualCarName = "9th GEN CAVICE M-SERIES"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "Offroad suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_M11":
        manualCarName = "11th GEN CAVICE M-SERIES"
        manualCarEngine = "Heavy duty engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Heavy duty automatic"
        manualCarSuspension = "Heavy duty suspension"
        manualCarTire = "Heavy duty tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_MSS":
        manualCarName = "CAVICE M-SERIES SUPER SWAMPER"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "Heavy duty suspension"
        manualCarTire = "Offroad tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_C4":
        manualCarName = "4th GEN CAVICE C-SERIES"
        manualCarEngine = "Heavy duty engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "CB radio"

    if entry == "CAV_RO1":
        manualCarName = "1st GEN CAVICE ROAMER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_RO2":
        manualCarName = "2nd GEN CAVICE ROAMER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAM2":
        manualCarName = "2nd GEN CAVICE CAMBIO"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Sport manual"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAM3":
        manualCarName = "3rd GEN CAVICE CAMBIO"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAM4":
        manualCarName = "4th GEN CAVICE CAMBIO"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"
        
    if read == 1:
        print("  " + manualCarName + " OPERATOR'S MANUAL")
        print("  " + "      Engine: " + manualCarEngine)
        print("  " + "    Radiator: " + manualCarRadiator)
        print("  " + "Transmission: " + manualCarTransmission)
        print("  " + "  Suspension: " + manualCarSuspension)
        print("  " + "       Tires: " + manualCarTire)
        print("  " + "     Battery: " + manualCarBattery)
        print("  " + "   Fuel tank: " + manualCarFuelTank)
        print("  " + "  Headlights: " + manualCarHeadlight)
        print("  " + " Tail lights: " + manualCarTailLight)
        print("  " + "       Radio: " + manualCarRadio)

    time.sleep(4)

    drawInspectionMenu()



def checkWorkOrder():
    print("  The work order says to " + formRequirement)
    time.sleep(1.5)
    drawInspectionMenu()



def drawInspectionMenu():
    changeCarGraphics()
    print("\n" + "  " + carName + "\n")
    print("  " + carLine1 + "             Engine: " + carEngine)
    print("  " + carLine2 + "           Radiator: " + carRadiator)
    print("  " + carLine3 + "       Transmission: " + carTransmission)
    print("  " + carLine4 + "      FL suspension: " + carSuspension1)
    print("  " + carLine5 + "      FR suspension: " + carSuspension2)
    print("  " + carLine6 + "      RL suspension: " + carSuspension3)
    print("  " + carLine7 + "      RR suspension: " + carSuspension4)
    print("  " + carLine8 + "            FL tire: " + carTire1)
    print("  " + carLine9 + "            FR tire: " + carTire2)
    print("  " + carLine10 + "            RL tire: " + carTire3)
    print("  " + carLine11 + "            RR tire: " + carTire4)
    print("  " + carLine12 + "            Battery: " + carBattery)
    print("  " + carLine13 + "          Fuel tank: " + carFuelTank)
    print("  " + carLine14 + "        L headlight: " + carHeadlight1)
    print("  " + carLine15 + "        R headlight: " + carHeadlight2)
    print("  " + carLine16 + "       L tail light: " + carTailLight1)
    print("  " + carLine17 + "       R tail light: " + carTailLight2)
    print("  " + carLine18 + "              Radio: " + carRadio)
    print("")
    print("  " + "You have " + str(money) + "$")

    print("\n" + "1. Check work order")
    print("2. Modify vehicle")
    print("3. Send vehicle off")
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    if plrinput == 1:
        checkWorkOrder()
    if plrinput == 2:
        while plrinput != 20:
            modifyCar()
    if plrinput == 3:
        checkVehicle()



def eventHandler():
    generateWorkCar()



if bypassIntro != 1:
    print(" ")
    time.sleep(3)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒┌─────────────────┐▒")
    print("▒│ Wasteland       │▒")
    print("▒│        Mechanic │▒")
    print("▒└─────────────────┘▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("         v0.1        ")
    time.sleep(3)
    print("")
    print("Welcome to the wasteland.")
    time.sleep(4)
    print("Your garage still stands, even after the bombs fell.")
    time.sleep(5)
    print("\nAs a part time mechanic, your job is to repair the vehicles brought")
    print("to you by roaming wastelanders, as well as go out and scavenge or buy")
    print("more car parts.")
    time.sleep(11)
    print("\nGood luck.")
    time.sleep(4)
eventHandler()
