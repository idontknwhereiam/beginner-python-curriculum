colors = ["red", "green", "blue", "yellow"]

print(colors)

print("first color:", colors[0])
print("second color:", colors[1])
print("third color:", colors[1])
print("forth color:", colors[3])

#error: index out of range
print(colors[10])

colors[0] = "maroon"
print("after edit:", colors)

colors.append("orange")
print("after append:", colors)

colors.inset(2, "purple")
print("after inset at index 2:", colors)

colors.remove("green")
print("after removing 'green':", colors)

# error: rempoving item not in the list
# colors.remove("pink")

popped_colot = colors.pop()
print("poppled color:" , popped_color)
print("after pop:", colors)

popped_color_at_index = colors.pop(1)
print("poped color:", popped_colors_at_index)
print("after pop at index 1:", colors)

index_of_blue = colors.index("blue")
print("index of 'blue':", index_of_blue)

#error: finding index of item not in the list
 # colors.index("pink")

colors.append("blue")
blue_count = colors.count("blue")
print("count of 'blue':", blue_count)

color.sort()
print("after sort:", colors)

colors.reverse()
print("after reverse:", colors)
