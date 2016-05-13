#Created when I first began learning how to program
print ("*"*60)
print ("*"*60)
print("**    This programs calculates the equation of a line     **")
print("**               Created by Parmvir Bath                  **")
print ("*"*60)
print ("*"*60)

#Ask user to input points
x1 = int(input("What is the value for x1?"))
y1 = int(input("What is the value for y1?"))
x2 = int(input("What is the value for x2?"))
y2 = int(input("What is the value for y2?"))

#Check if line is vertical 
if x1 == x2:
    print("The line is vertical. The equation is x=", x1)

#Check if line is horizontal 
elif y1 == y2:
    print("The line is horizontal. The equation is y=", y1)

elif type(x1, y1, x1, y2) != int:
    print("Numbers are invalid")
#Calculate the equation of a line if it is not horizontal or vertical 
else:
    m = (y2 - y1) / (x2 - x1)
    b = -m*x1+ y1
    mR = round (m)
    bR = round (b)
    equation =" y=" + str(mR) + "x+" + str(bR)

    print("The equation of the line is" + equation)
    
