
# 1.

# 3
# 1 1 1 
# 2 2 2 
# 3 3 3

# n = int(input("Enter the Number : "))
# i = 0
# while i < n:
#     j = 0
#     while j < n:
#         print(i+1, end=" ")
#         j += 1
#     print()
#     i += 1



# 2.

# Enter the Number : 3
# 1 2 3 
# 1 2 3 
# 1 2 3 

# n = int(input("Enter the Number : "))
# i = 0
# while i < n:
#     j = 0
#     while j < n:
#         print(j+1, end=" ")
#         j += 1
#     print()
#     i += 1
    


# 3.

# Enter the Number : 4
# 4 3 2 1 
# 4 3 2 1 
# 4 3 2 1 
# 4 3 2 1 


# n = int(input("Enter the Number : "))
# i = n
# while i > 0:
#     j = 0
#     while j < n:
#         print(n-j, end=" ")
#         j += 1
#     print()
#     i -= 1



# 4.

# Enter the Number : 4
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4

# n = int(input("Enter the Number : "))
# i = 1
# while i <= n:
#     j = 0
#     while j < i:
#         print(j+1, end=" ")
#         j += 1
#     print()
#     i += 1



# 5.

# Enter the Number : 4
# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7 

# n = int(input("Enter the Number : "))
# i = 1
# while i <= n:
#     j = 0
#     k = i
#     while j < i:
#         print(k, end=" ")
#         j += 1
#         k += 1
#     print()
#     i += 1



# 6.

# Enter the Number : 4
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

# n = int(input("Enter the Number : "))
# i = 1
# k = i
# while i <= n:
#     j = 0
#     while j < i:
#         print(k, end=" ")
#         j += 1
#         k += 1
#     print()
#     i += 1



# Alfabat Pattern


# 7.

# Enter the Number : 3
# A B C 
# A B C 
# A B C 


# n = int(input("Enter the Number : "))
# i = 0
# while i < n:
#     j = 0
#     start = ord('A')
#     while j < n:
#         letter = chr(start+j)
#         print(letter, end=" ")
#         j += 1
#     print()
#     i += 1


# 8.

# Enter the Number : 3
# A B C 
# B C D 
# C D E 

# n = int(input("Enter the Number : "))
# i = 0
# while i < n:
#     j = 0
#     k = i
#     start = ord('A')
#     while j < n:
#         letter = chr(start+k)
#         print(letter, end=" ")
#         j += 1
#         k += 1
#     print()
#     i += 1


# 9.

# Enter the Number : 3
# C
# B C
# A B C


# n = int(input("Enter the Number : "))
# i = n
# while i > 0:
#     j = 0
#     start = ord('A') + i - 1
#     while j < (n-i+1):
#         letter = chr(start+j)
#         print(letter, end=" ")
#         j += 1
#     print()
#     i -= 1



# 10

# Enter the Number : 5
# 1
# 1 1 
# 2 0 2 
# 3 0 0 3 
# 4 0 0 0 4

# n = int(input("Enter the Number : "))

# print("1")
# i = 1
# while i < n:
#     j = 0
#     while j <= i:
#         if j == 0 or j == i:
#             print(i, end=" ")
#         else:
#             print("0", end=" ")
#         j += 1
#     print()
#     i += 1




# 11.

# Enter the Number : 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n = int(input("Enter the Number : "))

# i = n
# while i > 0:
#     j = 0
#     while j < i:
#         print('*', end=" ")
#         j += 1
#     print()
#     i -= 1




# 12.

# Enter the Number : 5
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

n = int(input("Enter the Number : "))

i = 0
while i < n:
    space = 0
    while space < (n-i-1):
        print(' ', end=" ")
        space += 1
    while space < n:
        print('*', end=" ")
        space += 1
    print()
    i += 1
