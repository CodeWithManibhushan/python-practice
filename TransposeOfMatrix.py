# Compute transpose of a matrix. 

r = int (input("Enter no. of row a Matrix= "))
c = int (input("Enter no. of Column a Matrix= "))
A = []
b = []
print(f"Now, Enter the Elements Of {r} X {c} Matrix -")
for i in range (r):
    row = []
    for j in range (c):
        item = int (input(f"Enter A[{i}][{j}]= "))
        row.append(item)
    A.append(row)

print(f"Your {r}X{c} Matrix A is -")
for k in range (len(A)):
    print(A[k])

print(f"and its A' (Order {r}X{c} -> {c}X{r}) is -")
for l in range(c):
    row = []
    for m in range(r):
        row.append(A[m][l])
    b.append(row)

for n in range (len(b)):
    print(b[n])
print()
