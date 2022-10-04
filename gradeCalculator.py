print("""=====================
    Grade Calculator
=====================
""")

#this is the input for student ID.
#str is string as student ID consist of numbers and letters.
stdId = str(input("Enter Student ID: \n"))

#this is the input for tutorial mark.
#float because mark is in percentage.
tutoMark = float(input("Enter Tutorial Mark: \n"))

#this is the input for test mark.
#float because mark is in percentage.
testMark = float(input("Enter Test Mark: \n"))

total = tutoMark+testMark #to total up the marks
avgMark = (total/2)*50 #to calculate the average of both marks 

mark = avgMark + 50 #to calculate the actual marks of avg + final.
#we assume final is full marks which is 50%.
#that's why avg + 50.

#This is all the conditional values of the results should appear.
if(mark>=80):
    print("Grade: A\n Congrats!\n")
elif(mark>=70&mark<80):
    print("Grade: B\n Congrats!\n")
elif(mark>=60&mark<70):
    print("Grade: C\n Congrats and keep trying!\n")
elif(mark>=50&mark<60):
    print("Grade: D\n Congrats! Study More!\n")
else:
    print("Grade: F\n Please come and see me.\n")

