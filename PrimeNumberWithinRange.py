# Determine prime numbers within a specific range.
# 2, 3, 5, 7, 11, 13, 17, 19 etc

m = int (input("Enter Starting Range = "))
n = int (input("Enter Ending Range = "))
 
for i in range (m , n + 1):
    if i>1:
        for j in range(2,i): 
            if i%j == 0 :
                break
       
        else:
          print(i,end=" ")
