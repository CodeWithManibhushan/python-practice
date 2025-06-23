#Compute sum of natural numbers from one to n number.

m = int ( input ("Enter Natural Number for Sum = "))
sum = 0
for i in range ( 0 , m+1):
    sum = sum + i 
print ("Sum of Natural Number of 0 to ", m , " is " , sum)
