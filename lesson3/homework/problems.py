# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score1 = float(input("enter first test score:"))
score2 = float(input("enter second test score: ")) 




# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
brought_lunch = input("did you bring lunch? (yes/no): ").strip()



# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."



# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
score = float(input("enter your test score (0-100): "))
if score >= 90:
 print("a")
elif score >= 80:
 print("b")
elif score >= 70:
 print("c")
elif score >= 60:
 print("d")
else: print ("f")
# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
cond1 = (num1 % 5 == 0) and (num2 % 5 != 0)
cond2 = (num2 % 5 == 0) and (num1 % 5 != 0)
if cond1 or cond2:
 print("special pair")
else: print("plain pair")