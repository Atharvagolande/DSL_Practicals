mat1 = []
mat2 = []
new_mat = []
new_mat1=[]
new_mat2=[]

row1 = int(input("Enter the row of 1st matrix: "))
col1 = int(input("Enter the column of 1st matrix: "))
row2 = int(input("Enter the row of 2nd matrix: "))
col2 = int(input("Enter the column of 2nd matrix: "))

def matrix1():
    global mat1
    for i in range(row1):
        x = []
        for j in range(col1):
            x.append(int(input(f"Enter the elements of matrix A at position ({i},{j}): ")))
        mat1.append(x)

def matrix2():
    global mat2
    for i in range(row2):
        x = []
        for j in range(col2):
            x.append(int(input(f"Enter the elements of matrix B at position ({i},{j}): ")))
        mat2.append(x)

def addition():
    if row1 == row2 and col1 == col2:
        for i in range(row1):
            b = []
            for j in range(col1):
                b.append(mat1[i][j] + mat2[i][j])
            new_mat.append(b)
        prinadd()
    else:
        print("Matrix cannot be added as dimensions are not equal.")
        

def prinadd():
    print("Resultant Matrix:")
    for i in range(row1):
        for j in range(col1):
            print(new_mat[i][j], end=" ")
        print()

        
def subtraction():
    if row1 == row2 and col1 == col2:
        for i in range(row1):
            a = []
            for j in range(col1):
                a.append(mat1[i][j] + mat2[i][j])
            new_mat1.append(a)
        prinsub()
    else:
        print("Matrix cannot be added as dimensions are not equal.")
   

def prinsub():
    print("Resultant Matrix:")
    for i in range(row1):
        for j in range(col1):
            print(new_mat[i][j], end=" ")
        print()
        
        
def multiplication():
    if row1==col2:
        for i in range(0,row1):
            a=[]
            for j in range(0,col2):
                sum=0
                for k in range(0,col1):
                    sum+=mat1[i][k]*mat2[k][j]
                a.append(sum)
            new_mat2.append(a)
        prinmulti()
    else:
        print("Matrix cannot be multiplied as dimensions of matrix are not equal")
        
def prinmulti():
     print("Resultant Matrix:")
     for i in range (0,row1):
         for j in range(0,col1):
             print(new_mat[i][j], end=" ")
             print()
        
def transposeA():
    for i in range(0,row1):
        for j in range(0,col1):
            print(mat1[j][i],end="")
        print()    
        
def transposeB():
    for i in range(0,row2):
        for j in range(0,col2):
            print(mat2[j][i],end="")
        print()
        
matrix1()
matrix2()

addition()
subtraction()
multiplication()
transposeA()
transposeB()

print("------Choose the opreation------")
print("1.Addition of matrix  ")
print("2.Subtraction of matrix ")
print("3.Multiplication of matrix ")
print("4.Transpose of matrix A and matrix B")
print("5.Exit")

while(True):
    choice=int(input("Enter the opreation = "))
    if choice==1:
        print("Addition of matrix A and B are :")
        addition()
    elif choice==2:
        print("Subrtraction of matrix A and B :")   
        subtraction()
    elif choice==3:
        print("Multiplication of matrix A and B :")
        multiplication()
    elif choice==4:
        print("Transpose of matrix A :")
        transposeA()
        print("Transpose of matrix B :")
        transposeB()
    elif choice==5:
        break
    else:
        print("Invalid choice")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    