# Problem 1
# Search the list and print whether "tiger" is found.
animals = ["cat", "dog", "tiger", "lion"]
found = False
for i in range (len(animals)):
    if animals[i] == "tiger":
        found = True
        if found == True:
            print("found tiger")
        else:
            print("tiger not found")

# Problem 2
# Count how many words have length greater than 5.
    words = ["python", "cat", "elephant", "dog", "computer"]
counter = 0
for i in range(len(words)):
    if words[i] > 5:
        counter = counter + 1
        print(counter, "numbers greater than 5")


# Problem 3
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
    print("the total is:", total)


# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("the biggest number is:", biggest)


# Problem 5
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
biggest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < biggest:
        biggest = numbers[i]
        print("the biggest number is:", biggest)