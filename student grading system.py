mark={} #dictionary to store the student name and marks
total_marks=0
#asking for user input
for i in range(3):
    name=input("enter the student name")
    marks=int(input("enter the student mark"))
    mark[name]=marks
#grading system
for key,value in mark.items():
    if value >= 75:
        print(f"{key} got A")
    elif value >= 50:
        print(f"{key} got B")
    elif value < 50:
        print(f"{key} got C")
    if value > 50:
        total_marks= total_marks + value

print(total_marks)

#finding the students who score more than 75 marks
def get_top_students(mark):
    for key,value in mark.items():
        if value >= 75:
            print(f"{key} got for than 75")

#function to indentify the marks when the user input the name
def find_student(mark,names):
    for key,value in mark.items():
        if key.lower()== names:
            print(f"{names} got {value}")
        

get_top_students(mark)
print("search and find the mark")
names=input("enter the student name").lower()
find_student(mark,names)
    
    
    
