import time

# Define a function that counts down from a number
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
    print('Allahu Akbar!\n'*30)

countdown(5)