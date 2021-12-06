# read input from a file 
def read():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    return lines

# create a function to look for a keyword and a value
def find(lines, keyword):
    for line in lines:
        if keyword in line:
            return line.split()[-1]

# define list of keywords
forward_list = []
down_list = []
up_list = []
# read input from file
lines = read()
# if keyword is "forward", add value to a list
for line in lines:
    if "forward" in line:
        forward_list.append(int(line.split()[-1]))
    if "down" in line:
        down_list.append(int(line.split()[-1]))
    if "up" in line:
        up_list.append(int(line.split()[-1]))
# sum the values in lists
forward_sum = sum(forward_list)
down_list = sum(down_list)
up_list = sum(up_list)
# print the coordinates of the final position
coordonates = forward_sum * (down_list - up_list)
print(coordonates)