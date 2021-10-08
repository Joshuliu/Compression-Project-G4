# import abstract syntax trees
import ast
# opens the file
binaryfile = open("/Users/joshua/Documents/ECS 101 Project 1/binary_code.json", "r")

#reading the file
# converting the sting into binary
contents = binaryfile.read()
binary = ast.literal_eval(contents)
#closing the file
binaryfile.close()
# prompting the user to put in the file code is using
x = input('Enter file name to convert to text:')
# reading the file user put in
inputfile = open(x, "r").read()

# loop iterating over the string character by character, and adding the bianry value to the result
for line in inputfile:
result = ""
for line in inputfile:
    for character in line:
        result = result + str(binary[character])
#printin the result as string
print(int(result))
