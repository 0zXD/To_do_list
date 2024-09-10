while True:

    print("0. Exit \n1. Add Task \n2. View All Tasks \n3. Tasks completed \n4. Delete all tasks ")

    while True:
        try: 
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("******************")

    if choice == 0:
        print("Exiting...")
        break

    elif choice == 1:
        print("This is your to-do list")
        a= int(input("How many tasks to be done? "))
        print("Add tasks:")
        for i in range(a):
            n = i + 1
            x = input(f"{n}): ")
            y = open('tasks.txt', 'a')
            y.write(f"\n{x}\n")
            y.close()
        print("Tasks added successfully.")
        print("******************")

    elif choice ==2:
        f = open('tasks.txt')
        content = f.read()
        if not content: 
            print("Sorry, this list is empty :)")
            print("******************")
        else:
            print("This is your list:")
            print(content)
            print("******************")
        f.close()
        


    elif choice ==3:

        # Delete empty lines from tasks.txt
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()
        with open('tasks.txt', 'w') as f:
            f.writelines(line for line in lines if line.strip())
        # This enclosed portion is the code to delete the empty lines, it still needs to be understood.
        f = open('tasks.txt', 'r')
        g = len(f.readlines())
        with open('tasks.txt', 'r') as f:
            content = f.read()
            print(content)
        print("******************")
        
        p = int(input(f"Choose from [1 - {g}]: "))
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()

        lines.pop(p-1)
        with open('tasks.txt', 'w') as f:
            f.writelines(lines)

        with open('tasks.txt', 'r') as f:
            content = f.read()
            print(f"Remaining tasks:- \n{content}")
            print("******************")
        
    elif choice ==4:
        open("tasks.txt", "w").close()
        print("All entries deleted...")
        print("******************")
    

print("Thank you for using this app")
print("******************")