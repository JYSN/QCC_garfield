"""Write a function that will return a letter 
    grade when given a number. :


Check a number against two ifs:

receive a given number
    * prompt the user for a value
    * save it as a float variable

the first digit determines the letter
 * divide var by ten to get first digit
 * if >= 9 it's A, if >= 8 it's B, 7..6... else F

the second digit (modulo 10) determines the symbol (+, -, n/a)
 * if it's >=7 ->"+", >=4 -> " ", else "-"
 * hardcode that if original number = 100, mod = "+"

Display the combination of the letter and the symbol
"""

# Global Variables
# _________________
"""Set DEBUG to True to run test() function instead of main().
    To return input values Comment out the lines "test() else:" at end of file,
    like below:
            if DEBUG == True:
            #         test()
            # else:
                main()   
                """

DEBUG = False



# Functions
# ____________


# Letter Determination
def letter(num):
    """Returns a letter, by dividing input number by 10,
        then checking if result meets a series of diminishing 
        thresholds
"""
    val = num/10 
	# if expression:
	# elif expression:
	# else:
    if val >= 9:
    
        return "A"
        
    elif val >= 8:
        
        return "B"
    
    elif val >= 7:
        
        return "C"

    elif val >= 6:

        return "D"
    
    else:

        return "F"



# Modifier Determination
def modifier(num):
    """Returns a "+", "-" or nothing for a submitted value,
        determined by where the modulo falls in a range.
        Note: 100 is hardcoded to return "+",
             and F's to not return "+" or "-"
    """
    # Keep it 100 fam
    if num >= 100:
        return "+"

    # The Brian rule: No F+
    if num < 60:
        return ""

    # Plus    
    if num % 10 >= 7:

        return "+"

    # Minus
    elif num % 10 <= 3:

        return "-"

    # Normal
    else:

        return ""




# DEBUG FUNCTION
# ---------------
def test():
    assert letter(90) == "A", "Letter A doesn't check out"
    assert modifier(99) == "+", "Modifier + doesn't out"
    assert modifier(71) == "-", "Modifier - doesn't check out"
    assert not modifier(59) == "+", "F triggers + Modifier"
    assert not modifier(100) == "-", "A+ registers - Modifier"
    assert not modifier(101) == "-", "Extra credit registers - Modifier"

    
    




# Applilcation
# --------------

def main():
    """Takes an input val and returns a grade and modifier
        for it based on each digit being >= corresponding values"""

    # prompt user for number and save as float
    userval = float(input("\n\nHello, what number would you like graded?"
                        "\n ?>"))
                        
    # DEBUG mode: print user's input
    if DEBUG == True:

        print(f"Entered val is {userval}")

        print(userval % 10)

    # Insert user input into function that returns letter
    result = letter(userval)

    # Run user input through function to return modifier
    result += modifier(userval)

    # Print letter + modifier
    print(f"  Requested grade: {result} \n")
    


# Run Statement
# ---------------

if DEBUG == True:
    test()
else:

