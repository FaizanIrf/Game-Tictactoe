class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task index!")


def main():
    todo_list = TodoList()
    while True:
        print("--- Todo List Menu ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added!")
        elif choice == '2':
            todo_list.show_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()