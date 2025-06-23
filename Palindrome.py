# Determine whether a string is palindrome or not. 

n = input("Enter a string = ") 
a=len(n)%2
b=len(n)//2 
for i in range(b):  
    for j in range( len(n)-1,b-1,-1): 
        if n[i] == n[j] :               
            i+=1
        else:
            print("The given string is not a palindrome")
            break
    else:
        print("The given string is a palindrome")
        break
    break
