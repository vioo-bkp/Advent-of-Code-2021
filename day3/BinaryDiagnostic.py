with open("doom_input.txt", "r") as file:
    numbers = [row.rstrip() for row in file]

binary_gamma = ""
binary_columns = zip(*numbers)

for column in binary_columns:
    if column.count("1") > column.count("0"):
        binary_gamma += "1"
    else:
        binary_gamma += "0"

number_bits = int(len(numbers[0]))
maximum_rate = 2 ** number_bits

gamma_rate = int(binary_gamma, 2)
epsilon_rate = maximum_rate - gamma_rate - 1
power_consumption = gamma_rate * epsilon_rate

print("Gama rate:", gamma_rate)
print("Epsilon rate:", epsilon_rate)
print("Power consumption:", power_consumption)