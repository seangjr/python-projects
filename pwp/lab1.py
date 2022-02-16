def printhello():
    print("Hello World!")

def displaynumber(number):
    print(number)

def userdisplaynumber():
    number = int(input("Enter a number: "))
    displaynumber(number)

def addition():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x + y)

def swap():
    x = int(input("Enter first number: "))
    y = int(input("Enter the second number: "))
    print("The first number is ", y)
    print("The second number is ", x)

def arithmetic():
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print("The sum of the two numbers is:", x + y)
    print("The difference of the two numbers is:", x - y)
    print("The product of the two numbers is:", x * y)
    print("The quotient of the two numbers is:", x / y)
    print("The remainder of the two numbers is:", x % y)

def circlearea(radius):
    area = 3.14159 * radius ** 2
    print(area)

def circlecircumference(radius):
    circumference = 2 * 3.14159 * radius
    print(circumference)

def studentgrade():
    score_dictionary = {}
    for i in range(1, 6):
        score_dictionary["subject%s" %i] = int(input(f"Enter score for Subject%s: " %i))
    average = sum(score_dictionary.values()) / len(score_dictionary)
    print(f"Average score for the semester is {average}%")

def employeesalary():
    basic = int(input("Enter base salary: "))
    grade_pay = basic * 2
    DA = basic * 0.7
    TA = 200
    HRA = basic * 0.2
    salary = grade_pay + DA + TA + HRA
    print(f"Employee salary is {salary}")
