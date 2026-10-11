fruit = ["banana", "apple"]

if "apple" in fruit:
    print("found apple")
else:
    print("no apples found")

print("our algoirthm:")

found = False 
index = -1

for i in range(len(fruit)):
    if fruit[1] == "apple":
        foud = True
        index = i
        break
    if found == True:
        print("foudn the apple at", index)

    else:
        print("no apples in the list")

