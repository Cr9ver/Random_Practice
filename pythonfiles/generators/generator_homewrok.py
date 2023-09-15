# def gensquares(n):

#     for num in range(n) :
#         yield num*num
        


# # for x in gensquares(10):
# #     print(x)

# g = gensquares(10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

import random
# random.randint(1,10)

def rand_num(low,high,n):
    
    for i in range(n):
        yield random.randint(low,high)

# s = rand_num(1,10,12)
# print(next(s))
# print(next(s))


# for num in rand_num(1,20,12):
#     print(num)

# s = "hello"

# s_iter = iter(s)
# print(next(s_iter))