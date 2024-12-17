total=int(input("Enter no of students in class: "))

marks={}

for i in range(total):
    key=int(input("Enter the roll no of student: "))
    value=int(input("Enter marks obtained by student in FDS: "))
    marks.update({key:value})
print("Dictionary: ",marks)

def avg():
    sum=0
    count=0
    for i in marks.values():
        if i!='a':
            sum +=int(i)
            count=count+1 
        
    average=sum/count
    print("Average Of Marks:",average)
    
avg()

def high_marks():
    max = 0
    for i in marks.values():
        if i!='a'and int(i)>max:
            max = int(i)
    print("Highest Score: ",max)

high_marks()    

def low_marks():
    min = 10
    for i in marks.values():
        if i!='a' and int(i)<min:
            min = int(i)
    print("Lowest Score: ",min)

low_marks()

def absent():
    absent_count = sum(1 for i in marks.values() if i == 'a')
    print(f"Number of students absent for the test: {absent_count}")

absent()

def frequency():
    check = 0
    num = 0 
    for i in marks.values():
        count = 0
        for ele in marks.values():
            if i!='a':
                if (i==ele):
                    count=count+1
            if check<count:
                check=count
                num=i
    print("maximum frequency: ",num)
    
frequency()          

print("-----Enter the operation-----")
print("Average Of Marks:")
print("Highest marks of student:")
print("Lowest marks of student:")
print("Absent students:")
print("Maximum Frequency: ")
print("STOP")

x=int(input("Enter youer operation"))
if x==1:
    avg()
elif x==2:
    high_marks() 
elif x==3:
    low_marks()
elif x==4:
    absent()
elif x==5:
    frequency()
else:
    print("Invalid Output")
    
    
        