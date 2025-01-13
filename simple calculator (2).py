#simple calculator
#Sebastian 

#init
#functions
def add(num1, num2):
    result = num1 + num2
    print(result)

def subtract(num1, num2):
    result = num1 - num2
    print(result)

def multiply(num1, num2):
    result = num1 * num2
    print(result)

def divide(num1, num2):
    result = num1 / num2
    print(result)

def simple_calc():
    print("Welcome to Simple Calculator")
    while True:
        print("please choose an operation")
        print("""1.add
2.Subtract
3.multiply
4.divide
5.Quit""")
        option = int(input("1-5: "))
        if option == 1:
            num1 = int(input("please enter the first number:"))
            num2 = int(input("please enter the second number:"))
            add(num1,num2)
        if option == 2:
            num1 = int(input("please enter the first number:"))
            num2 = int(input("please enter the second number:"))
            subtract(num1, num2)

        if option == 3:
            num1 = int(input("please enter the first number:"))
            num2 = int(input("please enter the second number:"))
            multiply(num1, num2)

        if option == 4:
            num1 = int(input("please enter the first number:"))
            num2 = int(input("please enter the second number:"))
            divide(num1, num2)

        if option == 5:
            break
            print("see you later alligator")

#main
simple_calc()

