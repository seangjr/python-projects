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

def arithmetic():
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    operator = input("Enter the operator: ")
    if operator == "+":
        print(x+y)
    elif operator == "-":
        print(x-y)
    elif operator == "*":
        print(x*y)
    elif operator == "/":
        print(x/y)
    elif operator == "%":
        print(x%y)
    else:
        print("Enter a valid operator!")
        arithmetic()

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

def main():
    printhello()
    userdisplaynumber()
    addition()
    arithmetic()
    radius = int(input("Enter the radius of the circle: "))
    circlearea(radius)
    circlecircumference(radius)
    studentgrade()
    employeesalary()