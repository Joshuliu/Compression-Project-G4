import ast
binaryfile = open("/Users/joshua/Documents/ECS 101 Project 1/binary_code.json", "r")

contents = binaryfile.read()
binary = ast.literal_eval(contents)

binaryfile.close()

x = input('Enter file name to convert to text:')

inputfile = open(x, "r").read()


for line in inputfile:
result = ""
for line in inputfile:
    for character in line:
        result = result + str(binary[character])

print(int(result))