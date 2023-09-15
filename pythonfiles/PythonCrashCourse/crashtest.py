# planet = "Earth"
# diameter = 12742

# print("The diameter of {} is {} kilometers".format(planet,diameter))


# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

# print(lst[3][1][2])


# def findDog(there):
#     if "dog "in there:
#         return True
#     else:
#         return False
    

# dog = findDog('Is there a dog here?')
# print(dog)

# def domain_get(email):
#     return email.split('@')[-1]

# new = domain_get('user@domain.com')
# print(new)

def count_dog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count +=1
    return count

new = count_dog("hello I am a dog but a dog or dog but dgo")
print(new)
