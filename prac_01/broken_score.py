"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
#               SCORE RANGE
#       Bad       Passable            Excellent
# 0<--------------->50<------------>90<------->100
score = float(input("Enter score: "))
if score < 0 or score > 100:   #Any score below 0 and above 100 is invalid
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")     #Excellent score range from 90 to 100
    elif score >= 50:
        print("Passable")      #Passable score range from 50 to 89
    else:
        print("Bad")           #Bad score range from 0 to 49