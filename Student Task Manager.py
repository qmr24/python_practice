task={}
task_id_count=1
def add_task():
    global task_id_count
    task_id_countf="T"+str(task_id_count).zfill(3)
    print(("="*15))
    global task
    task_id=task_id_countf
    task_title=input("ENTER THE TASK TITLE")
    task_priority=input("ENTER THE TASK PRIORITY (High / Medium / Low))")
    task[task_id]={"TASK ID":task_id ,"TITLE":task_title}
    task_id_count=int(task_id_count)+1
add_task()
print(task)
    

