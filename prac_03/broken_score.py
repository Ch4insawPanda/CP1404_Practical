"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

#               SCORE RANGE
#       Bad       Passable            Excellent
# 0<--------------->50<------------>90<------->100


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)


def get_result(score):
    """Get the result of the user by use of the score."""
    if score < 0 or score > 100:  # Any score below 0 and above 100 is invalid
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"  # Excellent score range from 90 to 100
        elif score >= 50:
            return "Passable"   # Passable score range from 50 to 89
        else:
            return "Bad"        # Bad score range from 0 to 49

main()