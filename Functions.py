# defining function
# def add(arg1, arg2):
#     total = arg1 + arg2
#     return total
#
# out = add(2,3)
# print(out)
# print(add(10,30))


# def adder(arg1, arg2):
#     total =  arg1 + arg2
#     print(total)
#
# # adder(10,50)
# print(adder(10,50))


def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

# out = summ([10,20,30])
# print(out)

# summ([10,20])

# Default arguement
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function.")

greetings("Evening")