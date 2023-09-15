# try:
#     # MAY HAVE AN ERROR
#     result = 10 + 10
# except :
#     print("Looks like you are not adding correctly ")

# else:
#     print("add went well")
#     print(result)

# try: 
#     rando_string = "Hello there I just wrote to test file "
#     with open('testfile.txt', 'w') as file:
#         file.write(rando_string)
# except TypeError:
#     print("There was a type error! ")
# except OSError:
#     print("Hey you have an OS error")
# finally:
#     print("I always run ")


def ask_for_int():
    while  True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops that is not a number")
            continue
        else:
            print("Yes thank you!")
            break
        finally:
            print("I'm going to ask you again")
            

ask_for_int()
