################################################################################
#
# Myles Crouther
# Netflix List Parser
#
################################################################################

import re

# Variables

titles = []
extractedTxt = []
array = []
key = "\"fallback-text\""


# First seperate txt file by line
with open("his-netflix-list.html", "r") as ins:
    for line in ins:
        array.append(line)


# Checks if line has instances of the variable "key" in the "inputString"
def hasKey(inputString):
	arr = [m.start() for m in re.finditer(key, inputString)]
	return arr


# Returns the next in-line Title of "fallback-Text" images in an html line
def findTitle(str, start):
	init = start + 16
	
	for x in range(init, len(str)):
		if str[x] == "<":
			return str[init:x]


# Loops through array (html file), reads each line for matching key values
for y in range(0,len(array)):
	temp = hasKey(array[y])
	if  len(temp) > 0:
		for z in range(0,len(temp)):
			extractedTxt.append(findTitle(array[y],temp[z]))


# Prints My List in Text Form (Title's Only)
print(extractedTxt)