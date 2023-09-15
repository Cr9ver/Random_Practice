import re

text = 'My phone number is 408-555-1234'
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())



phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{3})')
results = re.search(phone_pattern,text)
results.group()
print(results.group(1))