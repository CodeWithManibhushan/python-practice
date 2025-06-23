# Count occurrence of vowels.

n = input("Enter a String = ")
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
for i in range (len(n)):
    if n[i] == "a" or n[i] == "A":
        count_a +=1
    elif n[i] == "e" or n[i] == "E":
        count_e +=1
    elif n[i] == "i" or n[i] == "I":
        count_i +=1
    elif n[i] == "o" or n[i] == "O":
        count_o +=1
    elif n[i] == "u" or n[i] == "U":
        count_u +=1
            
print("The occurrence of vowel a is ->",count_a)
print("The occurrence of vowel e is ->",count_e)
print("The occurrence of vowel i is ->",count_i)
print("The occurrence of vowel o is ->",count_o)
print("The occurrence of vowel u is ->",count_u)
