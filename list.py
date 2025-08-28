def todo_list():
   tasks=[]
   while True:
       print(
      "Type 1 for adding a task\n"
      "Type 2 for removing a task\n"
      "Type 3 for showing task\n"
      "Type 4 to quit\n"
  )
       choice=input("\nEnter your choice :")
       if choice=="1" :
           print("Adding a task")
           task=input("Enter the task :")
           tasks.append(task)
       elif choice=="2":
           print("Removing a task :\n")
           if task in tasks:
            tasks.remove(task)
           else:
             print("Task not found\n")
       elif choice=="3":
             print("Tasks are :\n")
             
             for task in tasks:
                  print("-" + task)
       elif choice=="4":
              break
       else:
             print("INVALID CHOICE\n")

todo_list()