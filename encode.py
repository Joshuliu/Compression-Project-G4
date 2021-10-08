import ast
binaryfile = open("/Users/joshua/Documents/ECS 101 Project 1/binary_code.json", "r")

contents = binaryfile.read()
binary = ast.literal_eval(contents)

binaryfile.close()

print('Enter file name to convert to binary:')
x = input()

inputfile = open(x, "r").read()

result = ""
for line in inputfile:
    for character in line:
        if character in line == 'and'
            str.replace('a'+'n'+'d', 'and')
        if character in line == 'th'
            str.replace('t'+'h', 'th')
        if character in line == 'er'
            str.replace('e'+'r', 'er')
        result = result + str(binary[character])

print(int(result))
