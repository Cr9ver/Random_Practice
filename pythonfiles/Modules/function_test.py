# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b%2 == 0 :
#         return min(a,b)
#     else:
#         return max(a,b)


# def animal_crackers(text):
#     wordlist = text.lower().split()
#     return wordlist[0][0] == wordlist[1][0]


# new = animal_crackers("Two Teeth")
# print(new)



# def makes_twenty(n1,n2):
#     total = n1 + n2
#     if total == 20 :
#         return True
#     elif n1 == 20 or n2 == 20:
#         return True
#     else:
#         return False
    

# new = makes_twenty(10,10)
# print(new)


# def old_mac(name):
#     if len(name) > 3:
#         new_name = name[:3].capitalize() + name[3:].capitalize()
#         return new_name
#     else:
#         return 'Name is too short'
    

# new = old_mac("magnito")
# print(new)

# def reverse_me(wow):
#     new_sent = wow.split()
#     complete_new = new_sent[::-1]
    
#     return ' '.join(complete_new)

# new = reverse_me("I am home")
# print(new)


# def almost_there(n):
#     if (abs(100 - n ) <= 10 ) or (abs(200 - n ) <= 10):
#         return True
#     else:
#         return False

# new = almost_there(70)
# print(new)

# def makes_twenty(n1,n2):
#     return(n1 +n2) == 20 or n1== 20 or n2 == 20

# def has_33(nums):

#     for i in range(0,len(nums)-1 ):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# new = has_33([1,3,3])
# print(new)


# def paper_doll(text):
#     result = ""

#     for char in text:
#         result += char*3
#     return result


# new = paper_doll("HOWFAR")
# print(new)



# def blackjack(a,b,c):
#     if sum([a,b,c]) <= 21:
#         return sum([a,b,c])
#     elif 11 in [a,b,c] and sum([a,b,c]) <=31:
#         return sum([a,b,c]) - 10 
#     else:
#         return "BUST"
    
# new = blackjack(9,10,1)
# print(new)


# def summer_69(arr):

#     total = 0
#     add = True

#     for num in arr:
#         while add:
#             if num !=6 :
#                 total +=num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num !=9:
#                 break
#             else:
#                 add = True
#                 break
#     return total



# def spy_game(nums):

#     code_list = [0,0,7,'x']
#     for num in nums:
#         if num == code_list[0]:
#             code_list.pop(0)

#     return len(code_list) == 1

# new = spy_game([1,7,2,0,4,5,0])
# print(new)
        

# def count_primes(num):

#     # Check for 0 or 1 input 
#     if num < 2:
#         return 0

#     # 2 or greater
#     primes = [2]
#     # Counter going up to input num 
#     x = 3

#     # x is going through every number up to input num
#     while x <= num:
#         for y in range(3,x,2):
#             if x%y == 0:
#                 x +=2
#                 break
#         else:
#             primes.append(x)
#             x +=2
#     print(primes)
#     return len(primes)

# new = count_primes(100)
# print(count_primes)


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

new = print_big('b')





