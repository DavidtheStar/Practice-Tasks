"write a program gets user input 2 numbers. If numbers different, output value"
",if equal say numbers are equal, program repeats until 0 is answered."


while True :
    num1 = int(input("what is your first number?: "))
    num2 = int(input("what is your second number?: "))

    if num1 == 0 or num2 == 0:
        print("Exiting program. ")
        break

    if num1 > num2:
        print(f"{num1}")
    elif num2 > num1:
        print(f"{num2}")
    else:
        print("the numbers are equal")



