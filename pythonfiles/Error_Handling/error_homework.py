# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print("String cannot be multiplied")


# try:
#     x = 5
#     y = 0

#     z = x/y
# except ZeroDivisionError:
#     print("Numbers cannot be divide by zero")
# finally:
#     print("All done")

def ask():
    while True:
        try:
            num1 = int(input("Please enter a number: "))
            square = num1*num1
            print(square)
        except ValueError:
            print("You did not enter a number please enter a number! ")
        else:
            print("Thanks for entering a number: ")
            break

ask()


        