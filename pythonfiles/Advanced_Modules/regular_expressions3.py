import re

# re.search(r'cat|dog', 'The cat is here')

# print(re.findall(r'...at', 'The cat in the hat went splat.'))

# print(re.findall(r'^\d', '1 is a number')) # starts with a number
# print(re.findall(r'\d$', 'the number is a 2')) # ends with a number



# phrase = 'there are 3 numbers 34 inside 5 this senetence'

# pattern = r'[^\d]+' # exclude digits

# print(re.findall(pattern,phrase))

# test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
# clean = re.findall(r'[^!.? ]+', test_phrase)
# print(' '.join(clean))


text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern,text))


# 