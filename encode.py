import ast # lib to interpret string into dict
import os # lib to find path of files

directory = os.path.dirname(os.path.abspath(__file__)) # gets path to current file
binaryfile = open(directory + "/binary_code.json", "r") # opens file to be read

contents = binaryfile.read() # reads file
binary = ast.literal_eval(contents) # turns string of dict into actual python dict

binaryfile.close() # closes file

# prompts user for file that they want to input
x = input('Enter file name to convert to binary (should be in same folder as this script): ')

inputfile = open(directory + '/' + x, "r").read() # opens and reads the file that user inputed

inputlist = [char for char in inputfile] # converts all chars in the inputfile into a list
result = "" # stores result
num = 0 # stores which character to iterate through 

while num < len(inputlist): # ensures char being iterated is in inputlist

    count = -1 # stores length of each test to find largest number of chars in our binary code
    finalcount = -1 # stores length of final largest number of chars in our binary code
    test = "" # stores each test to find largest number of chars in our binary code
    final = "" # stores final largest number of chars in our binary code 
    for x in range(5): # testing next if char, next 2 chars,... next 5 chars in our binary code
        if num+x < len(inputlist): # if there are any chars left to test
            count += 1 # indicates what index of list has been iterated over
            if test + inputlist[num + x] in binary.keys(): # if next x characters are in our binary code
                final = test + inputlist[num + x] # updates string to hold largest special characters (could just be one character)
                finalcount = count # updates finalcount to determine which character to iterate over next

            test += inputlist[num + x] # updates the next biggest group of chars to test
        else: # stop iterating over list if no more chars to test
            break

    num += 1 + finalcount # determines next character to iterate over
    result += binary[final] # adds most updated binary numbers to the final result

print(str(len(result)) + "." + result) # prints "d.b" format of final characters
