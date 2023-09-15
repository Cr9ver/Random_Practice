# def square(num):
#     return num**2

# my_nums = [1,2,3,4,5]

# for item in map(square, my_nums):
#     print(item)

# map_list = list(map(square,my_nums))
# print(map_list)

# def splicer(mystring):
#     if len(mystring)%2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]
# names = ['Andy', 'Eve', 'Sally']

# new_names = list(map(splicer,names))
# print(new_names)


# def check_even(num):
#     return num%2 == 0 


# mynum = [1,2,3,4,5,6]

# new = list(filter(check_even, mynum))
# print(new)
# for n in filter(check_even,mynum):
#     print(n)

# square = lambda num:num **2

# print(square(5))


# mynums = [1,2,3,4,5,6]
# new = list(map(lambda num:num**2, mynums))
# print(new)


# Basic lambda expression

# check = lambda num:num%2 == 0

mynums = [1,2,3,4,5,6]
check = list(filter(lambda num:num%2 == 0, mynums))
print(check)
mynums = [1,2,3,4,5,6]
check = list(map(lambda num:num%2 == 0, mynums))
print(check)


my_names = ['Andy', 'Eve', 'Sally']
new_order = list(map(lambda x:x[::-1],my_names))
print(new_order)

my_names = ['Andy', 'Eve', 'Sally']
new_order = list(filter(lambda x:x[::-1],my_names))
print(new_order)