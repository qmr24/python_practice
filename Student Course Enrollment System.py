#Student Course Enrollment System
student={}
course_no=1
while True:
    name=input("enter the student name")
    course=[]
    while True:
        sub=input("enter the student subject")
        course.append(sub)
        per=input("do you want add more")
        if per.lower()=="yes":
            continue
        elif per.lower()=="no":
            break
        else:
            print("enter correct entry")
    student[course_no]={'NAME':name,'SUBJECTS':course}
    course_no=course_no+1
    per_2=input("do you want add more student(yes/no)")
    if per_2.lower() == "yes":
        continue
    elif per_2.lower() == "no":
        break

print("==============================================")
#Function – Find Students by Course
def find_students_by_course(student, target):
    result=[]
    for key,value in student.items():
        for x in student[key]['SUBJECTS']:
            if target.lower() == x.lower():
                result.append(student[key]['NAME'])
            else:
                pass
    return result

target=input("enter the subject name to be searched")
print(find_students_by_course(student, target))
#Count Courses 
for key,value in student.items():
    print(f"{student[key]["NAME"]} Enrolled {len(student[key]["SUBJECTS"])}")
print("==============================================")
def get_multi_course_students(student):
    for key,value in student.items():
        if len(student[key]["SUBJECTS"])>=2:
            print(key)
get_multi_course_students(student)


