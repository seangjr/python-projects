#exercise 1a
def showMultiples(number):

    for i in range(10+1):

        print(i*number)

# 1b
showMultiples(12)

# 2a
def draw_triangle(levels):

    for i in range(levels, 0, -1):
        for j in range(0, i):
            print("X", end="")
        print()

# 2b
userLevels = int(input("Enter a number: "))
draw_triangle(userLevels)

# 3a
def draw_pyramid(levels):

    for row in range(1, levels+1):
        for col in range(1, 2*levels):
            if row == levels or row+col == levels+1\
                    or col - row == levels-1:
                print("O", end="")
            else:
                print(end=" ")
        print()


# 3b
userLevel2 = int(input("Enter a number: "))
draw_pyramid(userLevel2)