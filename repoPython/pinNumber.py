# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


count = 0
yes_count = 0
#import getpass

# while count < 3 and yes_count == 0:
#     pintry = int(input("Please enter your pin:"))
#     if pintry == 1234:
#         print("Welcome to your bank")
#         yes_count += 1
#     else:
#         print("Pin incorrect. Please try again.")
#         count +=1
#     if count == 3:
#          print("You've had 3 tries. Go away.")

count = 0
yes_count = 0
#import getpass

while count < 3 and yes_count == 0:
    pintry = int(input("Please enter your pin:"))
    if pintry == 1234:
        print("Welcome to your bank")
        yes_count += 1
    elif count < 2 and pintry != 1234:
        print("Pin incorrect. Please try again.")
        count += 1
    # else count == 2 and pintry != 1234:
    else:
        print("You've had 3 tries. Go away.")
        count += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
