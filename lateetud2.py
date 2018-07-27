#Myles Crouther
#Lateetud - Problem 2

#Variables
hasNum = []
array = []

#Seperates .txt file by line
with open("lateetud.txt", "r") as ins:
    for line in ins:
        array.append(line)

#Function checks for numbers in a line
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#Loop keeps lines with numbers in new list
for x in range(len(array)):
    if hasNumbers(array[x]):
        hasNum.append(array[x])

#Prints list with lines that contain
#numbers (This includes all dates and $)
print(hasNum)
