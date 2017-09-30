a = 0
b = 1
c = a + b
print(a)
print(b)
print(c)

while c < 100 or b < 100 or a < 100:
    a = b + c
    b = a + c
    c = b + a

    if a > 100:
        break
    else:
     print(a)
    if b > 100:
        break
    else:
        print(b)
    if c > 100:
        break
    else:
        print(c)






# for indeks, element in enumerate(zakres):
#     if indeks != 0 and indeks != 1:
#         print ("dupa")















#def fib(n):

# for (indeks, liczba) in cyfry:
#     if indeks == 0:
#         print("0")
#     if indeks == 1:
#         print("1")
#     if indeks > 1:
#         print((0,))




# def fib(n):
#  a,b = 1,1
#  for i in range(n-1):
#   a,b = b,a+b
#  return a
# print fib(5)


# def fibR(n):
#  if n==1 or n==2:
#   return 1
#  return fibR(n-1)+fibR(n-2)
# print fibR(5)








# for i in zakres:
#     if i = 0:
#         print ("0")



## Example 1: Using looping technique
# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a
#
#
# print
# fib(5)



# ## Example 2: Using recursion
# def fibR(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibR(n - 1) + fibR(n - 2)
#
#
# print
# fibR(5)