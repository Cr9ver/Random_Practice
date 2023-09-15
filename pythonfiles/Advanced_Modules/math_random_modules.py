# import math
# # help(math)

# value = 4.35
# the_floor = math.floor(value)
# ceil = math.ceil(value)
# print(the_floor)
# print(math.log(100,10))
# print(math.sin(10))
# print(math.degrees(math.pi/2))


import random

# print(random.randint(0,100))
# random.seed(101)
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))

# mylist = list(range(0,20))

# print(random.choice(mylist))

# # SAMPLE WITH REPLACEMENT
# new_random = random.choices(population=mylist,k=10)

# print(new_random)

# # SAMPLE WITHOUT REPLACEMENT
# without_replacemtn = random.sample(population=mylist,k=10)

# print(without_replacemtn)

unifrom = random.uniform(a=0,b=100)

print(unifrom)


print(random.gauss(mu=0,sigma=1))