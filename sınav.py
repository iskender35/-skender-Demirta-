# x = 15
# def fun(y):
#     global x
#     y = y+x
#     x = y-x
#     y = y-x
#     return y
# print((fun(x+x)+30)+x)
# for i in range(2):
#     print(i)
# for i in range(4,6):
#     print(i)
a = 1
b = 2
a,b = b,a
output = " {} {} ".format(a,b)
print(output)