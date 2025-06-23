# Print Fibonacci series up to n numbers e.g. 0 1 1 2 3 5 8 13…..n


m = int ( input ("Enter a Fibonaci Series Term = "))
temp1 = 0
temp2 = 1
print (temp1 , temp2 , end=" ")

for i in range ( 3 , m+1): 
    temp3=temp1 + temp2
    print (temp3 , end=" ")
    temp1 = temp2
    temp2 = temp3
    
