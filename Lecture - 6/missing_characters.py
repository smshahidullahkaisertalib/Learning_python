# def missingCharacters(s):
#     char_count = [0] * 123
#     result = ""

#     for i in range(len(s)):
#         x = ord(s[i])
#         char_count[x] += 1

#     for i in range(48, 58):  # ASCII range for digits 0-9
#         if char_count[i] == 0:
#             result += chr(i)

#     for i in range(97, 123):  # ASCII range for lowercase letters a-z
#         if char_count[i] == 0:
#             result += chr(i)

#     return result

# print(missingCharacters("abcdddd0123"))


import string
def missing_characters():
    
    alphabets = string.ascii_lowercase #for generating a-z
    numbers = string.digits  #for generating 0-9
    combination= set(alphabets + numbers)

    user_given = input("enter some character:") #taking character from user
    rest_of_char = combination - set(user_given) 
    missing_char = "".join(sorted(rest_of_char)) # using empty string to join all the char in one string
    return missing_char
print(missing_characters())