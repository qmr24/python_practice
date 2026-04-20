task={}
task_id_count=1
#adding task
def add_task():
    priority=["high","medium","low"]
    while True:
        global task_id_count
        task_id_countf="T"+str(task_id_count).zfill(3)
        print(("="*20))
        global task
        task_id=task_id_countf
        task_title=input("ENTER THE TASK TITLE")
        while True:
            task_priority=input("ENTER THE TASK PRIORITY (High / Medium / Low))")
            if task_priority.lower() not in priority:
                print('enter a vaild priority value (High / Medium / Low))')
                continue
            break
        task[task_id]={"TITLE":task_title ,"IMPORTANT":task_priority}
        task_id_count=int(task_id_count)+1
        ask=input("do you want to add more (yes/no)")
        if ask.lower()=="no":
            break
        elif ask.lower()=="yes":
            continue
        else:
            print("enter correct input")

#display task
def display_tasks():
    global task
    for key,value in task.items():
        print(f"{key} ==> {task[key]['TITLE']} ==> {task[key]['IMPORTANT']}")

#search task
def search_task():
    result=[]
    task_search=input("enter the name of the task to be searched")
    for key,value in task.items():
        if task_search.lower()== task[key]["TITLE"].lower():
            result.append(task[key])
    print(result)

def del_task( ):
    del_taskid=input("enter the task id which you want to delete")
    if  del_taskid in task :
                del task[del_taskid]
                print("task deleted")
    else:
        print("we didn't find the task id ")

            




add_task()
display_tasks()
search_task()



