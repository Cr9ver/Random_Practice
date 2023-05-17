# message ="corona is 100% effective most of the time, most are more than 90% effec"
# print(message.capitalize())
# message= message.capitalize()
# print(message)


# dir func
#
# print(dir(message))

# print(message.upper())
# print(message.isdigit())
# print(message.find("effective"))
# print(message[15:24])
# print(message.find("not"))

# seq1=("192", "168", "40", "90")
# print(".".join(seq1))
# print("/".join(seq1))
# print("-".join(seq1))

mountains= ["Everest", "Himalaya", "Sahyadri", "Alps", "k2", "Mt Hood"]
print(mountains)

mountains.append("Oregon mount")
print(mountains)

mountains.extend(["Mt Rainer", "Saptuda",])
print(mountains)

mountains.insert(2, "Mt Abu")
print(mountains)

mountains.pop()
print(mountains)

mountains.pop(5)
print(mountains)


cnr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "code":1034}
print(cnr_emp1.keys())
print(cnr_emp1.values())
print(cnr_emp1.clear())