''' Perform following operations on two matrices. 
     1) Addition 2) Subtraction 3) Multiplication    '''

print(" Enter the Row & Column of same Order Two Matrix")
print("-------------------------------------------------")
r = int (input("Enter no. of rows = "))
c = int (input("Enter no. of Columns = "))
A = []
B = []
Addition = []
Subtraction = []
Multiplication = []
print(f"Now, Enter the Elements Of {r} X {c} Matrix A-")
for i in range (r):
    row = []
    for j in range (c):
        item = int (input(f"Enter A[{i}][{j}]= "))
        row.append(item)
    A.append(row)
print(f"Now, Enter the Elements Of {r} X {c} Matrix B-")
for i in range (r):
    row = []
    for j in range (c):
        item = int (input(f"Enter B[{i}][{j}]= "))
        row.append(item)
    B.append(row)
print(f"Your {r}X{c} Matrix A is -")
for k in range (len(A)):
    print(A[k])
print(f"Your {r}X{c} Matrix B is -")
for k in range (len(B)):
    print(B[k])

print("Addition Of Matrix A & B -")
for i in range(r):
    row = []
    for j in range (c):
        Add = A[i][j] + B[i][j]
        row.append(Add)
    Addition.append(row)
for i in range(len(Addition)):
    print(Addition[i])

print("Subtraction Of Matrix A & B (A - B) -")
for i in range(r):
    row = []
    for j in range (c):
        Sub = A[i][j] - B[i][j]
        row.append(Sub)
    Subtraction.append(row)
for i in range(len(Subtraction)):
    print(Subtraction[i])

print("Multiplication Of Matrix A & B (A X B) -")
for i in range(r):
    row = []
    for j in range (c):
        temp=0
        for k in range(c):
            temp += A[i][k] * B[k][j]
        row.append(temp)
    Multiplication.append(row)
for i in range(len(Multiplication)):
    print(Multiplication[i])
