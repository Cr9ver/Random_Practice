# def say_hello(name):
#     return f"Hello {name}"

# new = say_hello("Daniel")
# print(new)


# def add_num(num1, num2):
#     return num1 + num2

# result = add_num(10,20)

# print(result)

# def return_result(a,b):
#     return a+b

# print(return_result(10,20))


# def even_check(number):
#     result = number % 2 == 0
#     return result 

# def even_check(number):
#     return number % 2 == 0

# new = even_check(51)
# print(new)


# Return true if any number is even in a list 

# def check_even_list(num_list):
#     for number in num_list:
#         if number %2 == 0 :
#             return True 
#         else:
#             pass
    
#     return False

# the_check  = check_even_list([2,4,5,5])
# print(the_check)



# def check_even_list(num_list):
#     # return all the even numbers in a list
#     even_numbers = []

#     for number in num_list:
#         if number %2 == 0:
#             even_numbers.append(number)
        
#         else:
#             pass
#     return even_numbers

# new_num = check_even_list([1,23,4,2,5,6])
# print(new_num)

# TUPLE UNPACKING 

# stock_prices = [('APPL', 200 ), ('GOOG', 400), ('MSFT', 100)]

# for item in stock_prices:
#     print(item)

# for ticker,price in stock_prices:
#     print(price)

# work_hours = [('Abby',100),('Billy', 400),('Cassie', 800)]

# def  employee_check(work_hours):

#     curent_max = 0
#     employee_of_the_month = ''
    
#     for employee, hours in work_hours:
#         if hours > curent_max:
#             curent_max = hours
#             employee_of_the_month = employee
#         else:
#             pass

#     return employee_of_the_month, curent_max


# work_hours = [('Abby',100),('Billy', 400),('Cassie', 800)]

# name,most_hours = employee_check(work_hours)
# print(most_hours)


# example = [1,2,3,4,5,6,7]

from random import shuffle 



def shuffle_list(mylist):
    shuffle(mylist)
    return mylist



mylist = ['','O','']
shuffle_list(mylist)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2: ")
    
    return int(guess)

myindex = player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess = (mixedup_list,guess)