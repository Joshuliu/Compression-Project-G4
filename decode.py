import ast
import os

directory = os.path.dirname(os.path.abspath(__file__))
binaryfile = open(directory + "/binary_code.json", "r")

#reading the file
# converting the string into dictionary
contents = binaryfile.read()
binary = ast.literal_eval(contents)
#closing the file
binaryfile.close()
# prompting the user to put in the file code is using
x = input('Enter file name to convert to text (should be in same folder as this script):')
# reading the file user put in
inputfile = open(directory + '/' + x, "r").read()

inputlist = [char for char in inputfile]