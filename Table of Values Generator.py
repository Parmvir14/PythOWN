##########################################
#       Table of Values Generator        #
#             Parmvir Bath               #
##########################################
print("Welcome to Table-of-Values Generator!")
print("Please enter VALID answers \nIf you dont the program will not run correctly")
print("")

#Input questions for the user
m = int(input("Enter the slope:"))
b = int(input("Enter the y-intercept:"))
min1 = int(input("Enter the minimum x-value you want in the table:"))
max1 = int(input("Enter the maximum x-value you want in the table:"))
delta = float(input("Enter the size of delta x:"))

#Equation so the program runs as many times as the user inputs
max2 = int((max1 - min1) / delta + 1)

#Headings for the Table-of-Values
print("X \t Y")
print ("----------")
print("")

#The Table-of-Values 
for a in range (0, max2):
    y = float(min1 * m + b)
    x = float(min1)
    print (str(x), "\t " + str(y))
    min1 = round(min1 + delta, 2)


         
    
    

