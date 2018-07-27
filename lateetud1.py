# Myles Crouther
# Lateetud - Problem 1

# Variables
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x = 4 # This is the number who's matrix coordinates you're looking for
m = 3  # Let the row maximum size be "m"
n = 5  # Where "n" is the column boundary maximum size

if (x % n) >= 1:
    j = x % n
    i = int(x/n) + 1
    
else:
    j = n
    i = int(x/n)

print("Variable x:" + str(x) + " is on...")
print("row: " + str(i))
print("column: " + str(j))
