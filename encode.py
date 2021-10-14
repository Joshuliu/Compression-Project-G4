import ast
binaryfile = open("/Users/joshua/Documents/ECS 101 Project 1/binary_code.json", "r")

contents = binaryfile.read()
binary = ast.literal_eval(contents)

binaryfile.close()

x = input('Enter file name to convert to binary: ')

inputfile = open(x, "r").read()

inputlist = [char for char in inputfile]
result = ""
num = 0

while num < len(inputlist):

    count = -1 # to determine how many characters to skip for multicharacter words 
    test = ""
    for x in range(5):
        if num+x < len(inputlist) and test + inputlist[num + x] in binary.keys():
                test += inputlist[num + x]
                count += 1
        else:
            break

    num += 1 + count
    print(test)
    print(binary[test])
    result += binary[test]

print(int(result))
