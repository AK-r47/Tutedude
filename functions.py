# def myfunc():
#     print("This is my function in functions.py")
# myfunc()


# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# def add(a,b):
#     print(a+b)


# add(a,b)
# add(5,6)


#-----------------------------------------------------------------


# def add(num1, num2):
#     print(num1 + num2)                  
# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# # add(a,b)

# add(a,b)


#-----------------------------------------------------------------
def mul(*numbers):
    ans=0
    return ans  
    print(numbers,type(numbers))   

    for i in numbers:
        ans += i
    return ans
ac=int(input())
ad=int(input())

print(mul(ac,ad ,8 ,8 ,8))
