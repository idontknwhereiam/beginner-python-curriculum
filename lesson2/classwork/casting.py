num_str = "42"
num_str = int(num_str) # convert string to integer
print(num_str + 1)

# error:
# print(num_str + 1)

float_str = "3.14"
num_float = float(float_str) # convert string to float
print(num_float + 2.19)

# error:
# print(float_str + 2.19)

int_num = 7
float_num = float(int_num) # convert integer to float
print(float_num)

float_num2 = 9.99
int_num = int(float_num2) # convert float to integer
print(int_num)

num = 20
num_str2 = str(num) # convert integer to string
print("this shirt costs $" + num_str2)

#error:
#print("this shirt costs $" + num")