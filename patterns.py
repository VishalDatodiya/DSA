
n = int(input("Enter the Number : "))

# 1.

# 3
# 1 1 1 
# 2 2 2 
# 3 3 3

 
 
 
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


# # ===============================================================================

#                                   Pattern - II

# # ===============================================================================

# 11.

# Enter the Number : 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

 

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

 

# i = 0
# while i < n:
#     space = 0
#     while space < (n-i-1):
#         print(' ', end=" ")
#         space += 1
#     while space < n:
#         print('*', end=" ")
#         space += 1
#     print()
#     i += 1



# 13.

#     * 
#   * * * 
# * * * * * 

# import time
# start = time.time()

# i = 0
# while i < n:
#     space = n-i-1
#     while space > 0:
#         print(' ', end="")
#         space -= 1
#     j = i * 2 + 1
#     while j > 0:
#         print('*', end="")
#         j -= 1
#     print()
#     i += 1
# end = time.time()
# print(end-start)        # 0.0138 time
    
# time.sleep(3)

# import time
# start = time.time()

# i = 0
# while i < n:
#     space = n-i-1
#     print(' '*space, end="")
#     j = i * 2 + 1
#     print('*'*j, end="")
#     print()
#     i += 1
# end = time.time()
# print(end-start)        # 0.0093 
    
    
    
# 14.

# Enter the Number : 3

#       * * * * * 
#         * * * 
#           * 
    
# i = n
# while i > 0:
#     space = n-i
#     while space > 0:
#         print(' ', end=" ")
#         space -= 1
#     j = i * 2 - 1
#     while j > 0:
#         print('*', end=" ")
#         j -= 1
#     print()
#     i -= 1


# 15.

# Enter the Number : 5
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 

# i = 0
# while i < n:
#     space = n-i-1
#     while space > 0:
#         print(' ', end=" ")
#         space -= 1
#     j = 0
#     while j < (i+1):
#         print(j+1, end=" ")
#         j += 1
#     k = i
#     while k > 0:
#         print(k, end=" ")
#         k -= 1
#     print()
#     i += 1


# 16.

#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 

# i = 0
# while i < n:
#     space = n-i-1
#     while space > 0:
#         print(' ', end=" ")
#         space -= 1
#     j = i + 1
#     k = 0
#     while k < (i+1):
#         print(j, end=" ")
#         j += 1
#         k += 1
#     l = j-2
#     while l > i:
#         print(l, end=" ")
#         l -= 1
#     print()
#     i += 1



# 17.  Pyramid  (n should be odd number)

# Enter the Number : 7
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

# i = 0
# n1 = (n+1)//2
# n2 = n//2
# while i < n1:
#     space = n1-i-1
#     while space > 0:
#         print(' ', end=" ")
#         space -= 1
#     j = i * 2 + 1
#     while j > 0:
#         print('*', end=" ")
#         j -= 1
#     print()
#     i += 1
    
# i = n2
# while i > 0:
#     space = n2-i+1
#     while space > 0:
#         print(' ', end=" ")
#         space -= 1
#     j = i * 2 - 1
#     while j > 0:
#         print('*', end=" ")
#         j -= 1
#     print()
#     i -= 1



# 18.

# 1      1
# 12    21
# 123  321
# 12344321


# hint

# if n = 4
# row     space
# 1       6
# 2       4
# 3       2
# 4       0


# i = 1

# totalSpace = (n-1)*2
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end="")
#         j += 1
#     print(' '*totalSpace, end="")
#     j = i
#     while j > 0:
#         print(j, end="")
#         j -= 1
#     totalSpace -= 2
#     print()
#     i += 1


# 19.

# Enter the Number : 4

# * 0 0 0 * 0 0 0 * 
# 0 * 0 0 * 0 0 * 0 
# 0 0 * 0 * 0 * 0 0 
# 0 0 0 * * * 0 0 0 

# start = 1
# end = n * 2 + 1
# k = end
# mid = n + 1
# row = 0
# while row < n:
#     col = 1
#     while  col <= k:
#         if col == start or col == end or col == mid:
#             print("*", end=" ")
#         else:
#             print('0', end=" ")
#         col += 1
#     start += 1
#     end -= 1
#     row += 1
#     print()
