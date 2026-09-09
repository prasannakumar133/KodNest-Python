# To print hello world

#
# start
# return hello World
# end
print("Hello world", end='-')
print("how are you")
name = "prasanna kumar"
print("name:\t",name)
#To find whether number (n) is even or odd

# start
# read n
# if n%2==0:
#     return even
# else:
#     return odd
# end
n = int(input("enter the number:"))
if n % 2 == 0:
    print("even")
else:
    print("odd")

  
  # to find the number is positive ,neg or zero

#   start
#   read n 
#   if n>0:
#     return positive
#     elif n<0:
#         return negative
#     else:
#         return zero
#     end
n=int(input("Enter the number:"))
if n > 0:
    print("positive")
elif n < 0: 
    print("negative")
else:
    print("zero")

#  # to find the largest among 3 numbers a,b,c
#    start
#     read a,b,c   
#     if a>b:
#       if a>c:
#         return a
#       else:
#         return c
#     else:
#       if b>c:
#         return b
#       else:
#     return c
# end
a = 21
b = 22
c = 20
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")