def task():
    
    tasks =[]
    print("-----Wellcome TO Task Management App-----")
    
    totalTask = int(input("Enter how many task you want to add = "))
    for i in range(1,totalTask+1):
        taskName = input(f"Enter task {i} = ") 
        tasks.append(taskName)
        
    print(f"Todays tasks are\n {tasks}")
    
    while True:
        operation = int (input("Enter\n 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit/Stop" ))
        if operation== 1:
            add= input ("Enter task you want to add")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation== 2:
            updateTask= input ("Enter the task you want to update = ")    
            if updateTask in tasks:
                up=input ("Enter new task =")
                ind= tasks.index(updateTask)
                tasks[ind]=up
                print(f"Updated task {up}")
        
        elif operation == 3:
            deleteTask= input ("Enter the task you want to delete = ")    
            if deleteTask in tasks:
                ind= tasks.index(deleteTask)
                del tasks[ind]
                print(f"Task {deleteTask} has been deleted...")
        
        elif operation == 4:
            print(f"Total tasks = {tasks}")
        
        elif operation == 5:
            print(f"Closing the program...")
            print("Closed")
            break
        
        else:
            print("Invalid input !")
task()
