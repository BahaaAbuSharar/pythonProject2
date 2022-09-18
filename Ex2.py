from math import *

first_input = input("Enter the first number: ")

if first_input.isdigit() or first_input.__contains__("."):

    op = input("choose the operator:\n1_+\n2_-\n3_*\n4_/\n5_^\n6_%\n")

    if op == "1" or op == "+":
        second_input = input("Enter the second number: ")
        if second_input.isdigit() or second_input.__contains__("."):
            result = float(first_input) + float(second_input)
            print(result)
            op2 = input("Extra choices:\n1_Rounded the number\n2_Floor the number\n3_Exit\n")
            if op2 == "1":
                print(round(result))
            elif op2 == "2":
                print(floor(result))
            elif op2 == "3":
                print(result)
            else:
                print("Error")
        else:
            print("Error")

    elif op == "2" or op == "-":
        second_input = input("Enter the second number: ")
        if second_input.isdigit() or second_input.__contains__("."):
            result = float(first_input) - float(second_input)
            print(result)
            op2 = input("Extra choices:\n1_Rounded the number\n2_Floor the number\n3_Exit\n")
            if op2 == "1":
                print(round(result))
            elif op2 == "2":
                print(floor(result))
            elif op2 == "3":
                print(result)
            else:
                print("Error")
        else:
            print("Error")

    elif op == "3" or op == "*":
        second_input = input("Enter the second number: ")
        if second_input.isdigit() or second_input.__contains__("."):
            result = float(first_input) * float(second_input)
            print(result)
            op2 = input("Extra choices:\n1_Rounded the number\n2_Floor the number\n3_Exit\n")
            if op2 == "1":
                print(round(result))
            elif op2 == "2":
                print(floor(result))
            elif op2 == "3":
                print(result)
            else:
                print("Error")
        else:
            print("Error")
    elif op == "4" or op == "/":
        second_input = input("Enter the second number: ")
        if second_input.isdigit() or second_input.__contains__("."):
            result = float(first_input) / float(second_input)
            print(result)
            op2 = input("Extra choices:\n1_Rounded the number\n2_Floor the number\n3_Exit\n")
            if op2 == "1":
                print(round(result))
            elif op2 == "2":
                print(floor(result))
            elif op2 == "3":
                print(result)
            else:
                print("Error")
        else:
            print("Error")
    elif op == "5" or op == "^":
        second_input = input("Enter the second number: ")
        if second_input.isdigit() or second_input.__contains__("."):
            result = float(first_input) ** float(second_input)
            print(result)
            op2 = input("Extra choices:\n1_Rounded the number\n2_Floor the number\n3_Exit\n")
            if op2 == "1":
                print(round(result))
            elif op2 == "2":
                print(floor(result))
            elif op2 == "3":
                print(result)
            else:
                print("Error")
        else:
            print("Error")
    elif op == "6" or op == "%":
        second_input = input("Enter the second number: ")
        if second_input.isdigit() or second_input.__contains__("."):
            result = float(first_input) % float(second_input)
            print(result)
            op2 = input("Extra choices:\n1_Rounded the number\n2_Floor the number\n3_Exit\n")
            if op2 == "1":
                print(round(result))
            elif op2 == "2":
                print(floor(result))
            elif op2 == "3":
                print(result)
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
