name = input("what is your name? ")
print("hi, name")


# input always returns a string
year = input("what year is it?")
print("it is currently", year)

year_num = int(year) # casting to an integer
print("next year is", year_num + 1)

# you can shorten this process:
user_number = int(input("give me a number: "))
print(user_number + 1)