Continue = 0

while Continue == 0:
    firstNum = float(input("Please give me a number:"))
    Op = input("Please give me an operator:")
    secondNum = float(input("Please give a 2nd number:"))

    if Op == ("+"):
        print("The answer is", firstNum + secondNum)

    elif Op == ("-"):
        print("The answer is", firstNum - secondNum)

    elif Op == ("*"):
        print("The answer is", firstNum * secondNum)

    elif Op == ("/"):
        print("The answer is", firstNum / secondNum)

    else:
        print("Please type valid operator.")

    Ask_cont = input("Do you want to continue? Press y or n")
    if Ask_cont == "y":
        Continue = 0
    elif Ask_cont == "n":
        Continue += 1
        print("Goodbye for now.")
    else:
        print("Please type y or n")
