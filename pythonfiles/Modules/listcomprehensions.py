# mystring = 'Hello'

# mylist = []

# for letter in mystring:
#     mylist.append(letter)

# print(mylist)

# new = [x for x in mystring]
# print(new)

# mylist = [num**2 for num in range(0,11)]
# print(mylist)

# mylist = [x**2 for x in range(0,11) if x%2==0 ]
# print(mylist)

# celcius = [0,10,20,34.5]

# fahrenheit = [((9/5)*temp + 32) for temp in celcius ]
# print(fahrenheit)

# newlist = []

# for new in celcius:
#     temperature = ((9/5)*new + 32)
#     newlist.append(temperature)
# print(newlist)

# mylist = []

# for x in [2,4,6]:
#     for y in [100,200,300]:
#         mylist.append(x*y)

# print(mylist)

# mylist = [x*y for x in [2,4,6 ] for y in [1,10,1000]]
# print(mylist)

# st = 'Print only the words that start with s in this sentence'

# for letter in st.split():
#     if letter[0] == 's':
#         print(letter)
    

# coollist=[]
# for num in range(0,10):
#     if num%2 == 0:
#         coollist.append(num)
# print(coollist)

# listcom = [x for x in range(1,50) if x%3 == 0]
# print(listcom)
# st = 'Print every word in this sentence that has an even number of letters'

# for word in st.split():
#     if len(word)%2 == 0:
#         print(word)


# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

st = 'Create a list of the first letters of every word in this string'

new = [x[0] for x in st.split()]
print(new)



