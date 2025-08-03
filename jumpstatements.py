#using continue and break
# n=10
# for i in range (1,n+1):
#     temp=i;
#     while temp%2 == 0:
#         temp /= 2

#     if temp != 1:
#         # break
#         continue
#     print(i)

#--------------------------------------------------------
# i=0
# while True:
#     i += 1 
#     if i%2 ==1:
#         continue
#     print(i)
#     if i == 5:
#         break

#-------------------------------------------------------

# i=0
# while True:
#     i += 1
#     print(i)

#--------------------------------------------------------

limit=10
currSum = 0
while True:
    num = int(input())
    if currSum + num > limit:
        print(currSum,"limit reached")
    currSum += num 