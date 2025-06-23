# Count total number of vowels in a word. 

n = input("Enter a String = ")
vowels = 0
for i in range(len(n)):
    if n[i] == "A" or n[i] == "a" or n[i] == "E" or n[i] == "e" or n[i] == "I" or n[i] == "i" or n[i] == "O" or n[i] == "o" or n[i] == "U" or n[i] == "u" :
        vowels += 1
print("The total number of vowels in a word is ->",vowels)
