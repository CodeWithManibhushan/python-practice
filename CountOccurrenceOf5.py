# #Count occurrence of a digit 5 in a given integer number input by the user.

# n = input("Enter a Number = ")
# count = 0
# for i in range ( len(n) ):
#     if n[i] == "5" :
#         count += 1
# print("The Count occurrence of a digit 5 is -> " , count)

# print()

# # 2nd Method Using inbuilt 'count' funtion
# print("2nd Method Using inbuilt 'count' funtion")
# print("The Count occurrence of a digit 5 is -> " , n.count("5"))
# Input integer from user
n = int(input("Enter Number = "))

count_of_5 = 0

while n > 0:
    digit = n % 10 
    if digit == 5:
        count_of_5 += 1 
    n = n // 10 

print("The digit 5 occurs ", count_of_5, " times in the number.")
