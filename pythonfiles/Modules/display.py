
# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1 = [' ',' ',' ']
# row2 = [' ',' ',' ']
# row3 = [' ',' ',' ']
# new = display(row1,row2,row3)
# print(new)

# def user_choice():
#     choice = 'WRONG'

#     while choice.isdigit() == False:
#         choice = input("Please enter a number (0-10): ")

#         if choice.isdigit() == False:
#             print("That is not a digit")
#     return int(choice)

# user_choice()


# result = 'Wrong Value'
# acceptable = [0,1,2]
# print(result not in acceptable)


def user_choice():
    # VARIABLES 

    #Initital
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # TWO CONDITIONS TO CHECK
    # DIGIT OR WITHIN_RANGE == False

    while choice.isdigit() == False or within_range==False:
        choice = input("Please enter a number (0-10): ")

        # DIGIT CHECK
        if choice.isdigit() == False:
            print("That is not a digit")

        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry you are out of the range (0-10)")
                within_range = False

    return int(choice)

user_choice()