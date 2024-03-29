import time 
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

# numbers  = func_one(10)
# print(numbers)

def func_two(n):
    return list(map(str,range(n)))

# new_numbers = func_two(10)
# print(new_numbers)


# start_time = time.time()
# result = func_one(10)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)

# start_time = time.time()
# result = func_two(10)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)


stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]

'''

timer = timeit.timeit(stmt,setup,number=1000000)
print(timer)

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
    
'''
timer = timeit.timeit(stmt2,setup2,number=1000000)
print(timer)


