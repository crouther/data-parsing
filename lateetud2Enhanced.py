#Myles Crouther
#Lateetud - Problem 2

#Variables
hasNum = []
hasDate = []
talksAboutMoney = []
array = []
dates = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#First seperate txt file by line
with open("lateetud.txt", "r") as ins:
    for line in ins:
        array.append(line)

#Function checks if each line as a string
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#Loops through list keeping strings with numbers
for x in range(len(array)):
    line = str(array[x])

    #Checks if line has number
    if hasNumbers(array[x]):
        hasNum.append(array[x])

    #Check if line has date
    for y in range(len(dates)):
        month = str(dates[y])
        if month in line:
            hasDate.append(array[x])

    #Checks if line talks about money     
    if "$" in line:
        talksAboutMoney.append(array[x])

file = open("lateetud2Output.txt", "w")
file.write("Lines with numbers : ")
file.write("\n")

for z in hasNum:
    file.write(z)

file.write("\n")
file.write("Lines with dates: ")
file.write("\n")
for a in hasDate:
    file.write(a)
    
file.write("\n")
file.write("Lines with dollar signs: ")
file.write("\n")
for b in talksAboutMoney:
    file.write(b)

file.close()

#Print list
print("Lines with numbers listed below: ")
print(hasNum)
print("Lines with dates listed below: ")
print(hasDate)
print("Lines with dollar signs: ")
print(talksAboutMoney)
