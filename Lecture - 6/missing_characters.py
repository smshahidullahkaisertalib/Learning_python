def missingCharacters(s):
    char_count = [0] * 123
    result = ""

    for i in range(len(s)):
        x = ord(s[i])
        char_count[x] += 1

    for i in range(48, 58):  # ASCII range for digits 0-9
        if char_count[i] == 0:
            result += chr(i)

    for i in range(97, 123):  # ASCII range for lowercase letters a-z
        if char_count[i] == 0:
            result += chr(i)

    return result

print(missingCharacters("abcdddd0123"))