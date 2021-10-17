import ast
import os

directory = os.path.dirname(os.path.abspath(__file__))
binaryfile = open(directory + "/binary_code.json", "r")

contents = binaryfile.read()
binary = ast.literal_eval(contents)

binaryfile.close()

x = input('Enter file name to convert to binary (should be in same folder as this script): ')

inputfile = open(directory + '/' + x, "r").read()

inputlist = [char for char in inputfile]
result = ""
num = 0

while num < len(inputlist):

    count = -1
    finalcount = -1
    test = ""
    final = ""
    for x in range(5):
        if num+x < len(inputlist):
            test += inputlist[num + x]
            count += 1
            if test + inputlist[num + x] in binary.keys():
                final = test
                finalcount = count
        else:
            break

    num += 1 + finalcount
    result += binary[final]

print(int(result))
