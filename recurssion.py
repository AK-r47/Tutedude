# def myfunc1():
#     myfunc1()
#     print("Function1")
# myfunc1()
#stack overflow errir
#------------------------------------------------------------------

# def func(x):
#     if (x == 0):
#         return
#     print(x)
#     func(x-1)

# func(3) 

#--------------------------------------------------------------------
#factorial
# def fact(n):
#     if n == 1 or n == 0:
#         return 1 
#     return n* fact(n-1)
# ans = fact(5)
# print(ans)
# # print(fact(4))
# # print(fact(5))


#-----------------------------------------------------------------
#practice factorial
def factorial(z):
    if z == 1 or z == 0:
        return 1
    return z * factorial(z-1)
zara = factorial(5)
print("FACTORIAL:",zara)

#-------------------------------------------------------------------
#fibonacci series
q=int(input("FIBONACCI OF:"))
def fib(q):
    if q == 1 or q == 2:
        return 1
    return fib(q-1)+ fib(q-2)
dior = fib(q)
print(dior)




