#Q1
def printhello():
    # prints a hello world message
    print("Hello World!")
# Q2
def displaynumber(number):
    # display the number
    print(number)
# Q3
def userdisplaynumber():
    # get the number from the user and display it
    number = int(input("Enter a number: "))
    displaynumber(number)
# Q4
def addition():
    # get the numbers from the user and add them
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x + y)
# Q5
def swap():
    # swap the values of two variables
    x = int(input("Enter first number: "))
    y = int(input("Enter the second number: "))
    print("The first number is ", y)
    print("The second number is ", x)
# Q6
def arithmetic():
    # get the numbers from the user and perform arithmetic operations
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = x / y
    remainder = x % y
    print(f"Addition is {addition}")
    print(f"Subtraction is {subtraction}")
    print(f"Multiplication is {multiplication}")
    print(f"Division is {division}")
    print(f"Remainder is {remainder}")
# Q7
def circleareaandcircumference():
    # get the radius from the user and calculate the area and circumference
    radius = int(input("Enter radius: "))
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    print(f"Area of circle is {area}")
    print(f"Circumference of circle is {circumference}")
# Q8
def studentgrade():
    # initialize dictionary
    score_dictionary = {}
    # get the grades from students
    for i in range(1, 6):
        # assign score to the dictionary
        score_dictionary["subject%s" %i] = int(input(f"Enter score for Subject%s: " %i))
    #calculate the average from the dictionary (values over length)
    average = sum(score_dictionary.values()) / len(score_dictionary)
    print(f"Average score for the semester is {average}%")
# Q9
def employeesalary():
    # get base salary from the user
    basic = int(input("Enter base salary: "))
    # calculate the salary
    grade_pay = basic * 2
    DA = basic * 0.7
    TA = 200
    HRA = basic * 0.2
    salary = grade_pay + DA + TA + HRA
    print(f"Employee salary is {salary}")
