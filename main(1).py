GroupA=[]
GroupB=[]
GroupC=[]


GA=int(input("enter no of student in Group A="))
while GA>len(GroupA):
    s_roll=input("Enter of student who play cricket=")
    if s_roll not in GroupA:
        GroupA.append(s_roll)
        
GB=int(input("enter no of student in Group B="))
while GB>len(GroupB):
    s_roll=input("Enter of student who play badminton=")
    if s_roll not in GroupB:
        GroupB.append(s_roll)                
        
GC=int(input("enter no of student in Group C="))
while GC>len(GroupC):
    s_roll=input("Enter of student who play football=")
    if s_roll not in GroupC:
        GroupC.append(s_roll)

def GroupAGroupB():
    a=[]
    for i in GroupA:
        for j in GroupB:
            if i==j:
                a.append(i)           
    print("Roll number of student who play both cricket and badminton=",a)

                
GroupAGroupB()           

def noGroupAGroupB():
    b=[]
    for i in GroupA:
        if i not in GroupB:
            b.append(i)
    print("Roll number of student who play cricket but not badminton=",b)
    print("Roll number of student who play badminton  but not cricket=",b)

noGroupAGroupB()                

def noAnoB():
    c=[]
    for i in GroupA:
        if i not in GroupA and i not in GroupB:
            c.append(i)
    print("Roll no of student who play football but not cricket and badminton=",c)
                
noAnoB()                
def fcnb():
    d=[]
    for i in GroupC:
        if i not in GroupA and i not in GroupB:
            d.append(i)
    print("Roll no of student who play football and  cricket but not badminton=",d)
            
fcnb()            
            
print("-----Choose the opreation------")
print("1.List of the student who plays both cricket and badminton")
print("2.List of the student who plays either cricket or badminton but not both")
print("3.List of the student who plays football but not cricket and badminton")
print("4.Roll number of the student who plays football and cricket but not badminton")

x=int(input("Enter the opreation = "))
if x==1:
    GroupAGroupB() 
elif x==2:
    noGroupAGroupB()
elif x==3:
    noAnoB()
elif x==4:
    fcnb() 
else:
    ("Invalid opreation")
