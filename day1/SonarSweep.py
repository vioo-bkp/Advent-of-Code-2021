# read input from a file 
def read():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    return lines

# cout +1 if the input number is higher than the previous number
def count(lines):
    count = 0
    # loop through the list, starting at index 1 (bcs index 0 is the first number)
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            count += 1
    return count

print(count(read()))
