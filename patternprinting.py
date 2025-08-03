# n=int(input("Enter columns:"))
# m=int(input("Enter rows:"))
# for i in range(n+1):
#     for i in range(m-1):
#         print(i, end=" ")
#     print(" ")

#------------------------------------------------------------------

n=int(input("ENTER NUMBER:"))
for i in range(n-1):
    for a in range(n):
        if  a<=i:
            print(a+1,end=" ")
        else:
            break
            print(" ", end="")
    print(" ")       
    
 