from collections import Counter
from collections import defaultdict
from collections import namedtuple

# mylist = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

# print(Counter(mylist))


# new_list = ['a','a', 10,10,10]
# print(Counter(new_list))


# sentence = "How many times does each word show up in this sentence with a word"

# new = Counter(sentence.lower().split())
# print(new)


# letters = 'aaaabbbbbcccccdddddd'
# c = Counter(letters)
# c.most_common(1)
# print(c)

d = defaultdict(lambda: 0)
d['correct'] = 100
d['Wong key']

print(d)

mytuple = (10,20,30)

Dog = namedtuple('Dog',['age','breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')



