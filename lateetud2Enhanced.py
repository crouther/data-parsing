#Myles Crouther
#Lateetud - Problem 2

#Variables
hasNum = []
hasDate = []
talksAboutMoney = []
figures = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", " "]
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
            datePlace = line.index(month) + len(month) - 1
            day = str(line)
            
            #Loops through string starting at $, stops at nondigit
            for z in range(datePlace+1, len(day)):
                if day[z] in figures:
                    continue
                else:
                    hasDate.append(day[line.index(month):z])
                    break

    #Checks if line talks about money     
    if "$" in line:
        num = line.index("$")
        word = str(line)

        #Loops through string starting at $, stops at nondigit
        for a in range(num+1, len(word)):
            if word[a] in figures:
                continue
            else:
                talksAboutMoney.append(word[num:a])
                break

#Opens & Saves arrays to output files
file = open("lateetud2Output.txt", "w")
file.write("Lines with numbers : ")
file.write("\n")

#Prints Has Number array to output file
for z in hasNum:
    file.write(z)

#Prints lines with dates to output file
file.write("\n")
file.write("Lines with dates: ")
file.write("\n")
for b in hasDate:
    file.write(b)
    file.write("\n")

#Prints dollar values to output file
file.write("\n")
file.write("Lines with dollar signs: ")
file.write("\n")
for c in talksAboutMoney:
    file.write(c)
    file.write("\n")

file.close()

#Print list
print("Lines with numbers listed below: ")
print(hasNum)
print("Lines with dates listed below: ")
print(hasDate)
print("Lines with dollar signs: ")
print(talksAboutMoney)
