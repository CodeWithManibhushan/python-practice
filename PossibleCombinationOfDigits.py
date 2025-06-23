# num = [4 , 5]

# print("Printing all possible combinations of 4 and 5.")
# for i in range(len(num)):
#     for j in range(len(num)):
#         if i != j :
#             print(num[i],num[j])
            
# print()
# num.append(6)
# print(num)
# print("Printing all possible combinations of 4, 5, and 6.")
# for i in range(len(num)):
#     for j in range(len(num)):
#         if j != i :
#             for k in range(len(num)):
#                 if k != i and j != k :
#                     print(num[i] , num[j] , num[k])
             
# print()       
# num.append(7)
# print(num)
# print("Printing all possible combinations of 4, 5, 6 and 7.")
# for i in range(len(num)):
#     for j in range(len(num)):
#         if j != i :
#             for k in range(len(num)):
#                 if k != i and j != k :
#                     for l in range (len(num)):
#                         if l != i and l != j and l != k :
#                             print(num[i] , num[j] , num[k] , num[l])
num = [4 , 5 , 6]
print("Printing all possible combinations of 4, 5, and 6.")
for i in range(len(num)):
    for j in range(len(num)):
        if j != i :
            for k in range(len(num)):
                if k != i and j != k :
                    print(num[i] , num[j] , num[k])
