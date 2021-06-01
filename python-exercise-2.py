# exercise 1
def printHex():

    for x in range(5):
        print(6 * "#")

printHex() # <---- this is the only thing u need to write :D for exercise 1

#exercise 2a
def smaller_num(num1, num2):

    print(num1 if num1 < num2 else num2)

smaller_num(9, 8)

#exercise 2b
userInputNumber1 = int(input("Enter first number: "))
userInputNumber2 = int(input("Enter second number: "))

smaller_num(userInputNumber1, userInputNumber2)

# #exercise 3a
male = "Male"
female = "Female"

def getPrice(gender, age):

    if gender == male:
        if age >= 12:
            price = 20
        else:
            price = 12
        print("You have to pay $"+str(price))

    elif gender == female:
        if age >= 12:
            price = 18
        else:
            price = 10
        print("You have to pay $"+str(price))

    
#exercise 3b
def getFamPrice():

    famPrice = getPrice(male, 42) + getPrice(female, 40) + getPrice(female, 11) + getPrice(female, 10)
    print("Total cost of family is $"+str(famPrice))

getFamPrice()

#exercise 4a
def email_template(address, name):

    print("Email address: "+address+"\nName of sender: "+name)

email_template("mynamesjeff@iamgay.com", "Jeff")
#exercise 4b
address = input("Enter email: ")
name = input("Enter name: ")

email_template(address, name)

#exercise 5a
def print_timetable(x): #where x is the number to print for the timetable

    for i in range(12+1): # 12 isnt included so need to +1

        print(str(x)+" x "+str(i)+" = "+str(x*i))

print_timetable(12)

#exercise 5b
userInput = input("Enter a number to print multiplication table: ")
print_timetable(userInput)