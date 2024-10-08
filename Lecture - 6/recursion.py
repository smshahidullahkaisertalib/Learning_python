# def Cal(n):
#     if(n == 0):
#         return 0
#     else:
#         sum = Cal(n-1) + n
#     return sum

# print(Cal(4))

    

# def traverse_list(list, index=0):
#     if(index == len(list)):
#         return
#     print(list[index])
#     return traverse_list(list, index+1)


# list = ["movies", "natok", "series"]
# traverse_list(list)



# fibonacci series


def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
# fibo = fibo(5)
for i in range(10):
    print(fibo(i))