# Variable length arguments **kwargs (keyword arguements)
import random
def time_activity(*args, **kwargs):

    '''
    INPUT: Multiplevalues for minutes, key= value pair activity
    OUTPUT: Return sum of minutes + random minute spent on a random activity
    '''


    # print(args)
    # print(kwargs)
    min = sum(args) + random.randint(0, 60)
    # print(min)
    choice= random.choice(list(kwargs.keys()))
    # print(choice)
    print(f"You have to spend {min}min for {kwargs[choice]}")

time_activity(10,20,10, hobby="Dance", sport="boxing", fun="Driving", work="DevOps")