import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.



# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["math", "reading", "art", "science"]
print(subjects[2])
print("after insert:", subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
error_codes = [400, 401, 403, 404, 500]
print(len(error_codes))
for code in error_codes:
    print(code)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random
languages = ["python", "javascript"]
print(random.choice(languages))
languages.append("java")
print(languages)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = [20, 21, 22, 23, 24, 25]
middle_index = len(passwords) // 2
print([passwords[middle_index]])
passwords.pop(0)
print(passwords)


