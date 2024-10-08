# def lenList(list):
#     print(len(list))
#     return list

# result = lenList([1,2,3,4,5]) #we also can pass the list storing in a function
# print(result)


# def CurrencyConversion(USD):
#     BDT = USD * 120.00
#     print(BDT)
#     return BDT

# CurrencyConversion(float(input("Enter USD: ")))

def evenOddChecker(n):
    if(n%2 != 0):
        print("odd")
    else:
        print("even")

evenOddChecker(int(input("Enter n: ")))