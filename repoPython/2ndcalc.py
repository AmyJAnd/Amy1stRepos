
carry_on = "Y"
while carry_on == ("Y"):
    numbers = input("Please enter some numbers, separated by a space: ")
    operator = input("Please enter an operator: ")
    number_list = numbers.split()
    # print(number_list)
    int_number_list = [eval(e) for e in number_list]
# print(int_number_list)
# list_length = len(int_number_list) don't need this now
# print(list_length)
    if operator == "+":
     print("The answer is ", sum(int_number_list))
    elif operator == "-":
        # count = 0
        # while count < list_length:
        #     newNum = (int_number_list[count] - int_number_list[(count+1)])
         #     count+=1
        # print(newNum)
        running_total = int_number_list[0]
        for num in int_number_list[1:]:
            running_total -= num
        print("The answer is ", running_total)
    elif operator == "*":
        running_total = int_number_list [0]
        for num in int_number_list[1:]:
            running_total *= num
        print ("The answer is ", running_total)
    elif operator == "/":
        running_total = int_number_list[0]
        for num in int_number_list[1:]:
            running_total /= num
        print("The answer is ", running_total)
    else:
        print("You did not enter a valid operator!")
    carry_on_1 = input("Do you want to carry on? Press Y or N: ")
    carry_on = carry_on_1.upper()
print("Goodbye!")
