# List = [1, 2, 3]
original_list = [1, 2, "abc", 2, 1]
copied_list = original_list.copy()
original_list.reverse()
if (original_list == copied_list):
    print("palindrome")
else:
    print("not palindrome")


