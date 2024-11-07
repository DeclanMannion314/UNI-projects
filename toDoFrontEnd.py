from tkinter import *
from toDoBackEnd import TaskList

class ToDoList:

    def __init__(self, task):
        self.task = task
        self.root = Tk()
        self.root.title("To Do list")
        self.root.geometry("300x200")
        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(row=0, column=0)
        self.newTask = StringVar()

    def createWidgets(self):
        numTasks = self.task.getNumTasks()
        for lbl in range(numTasks):
            task = self.task.getTaskMsgByIndex(lbl)
            taskLabel = Label(
                self.mainFrame,
                width = 10,
                text = task
            )
            taskLabel.grid(row=0+lbl, column=0)

            editButton = Button(
                self.mainFrame,
                text = "Edit",
                command=lambda index=lbl, label=taskLabel: self.editTask(index, label)
            )
            editButton.grid(row=0+lbl, column=1)

            deleteButton = Button(
                self.mainFrame,
                text = "Delete",
                command=lambda index=lbl, label=taskLabel: self.deleteTask(index, label)
            )
            deleteButton.grid(row=0+lbl, column=2)

        addTaskEntry = Entry(
            self.mainFrame,
            width=10,
            textvariable= self.newTask
        )
        addTaskEntry.grid(row=numTasks+1, column=0)

        addTaskButton = Button(
            self.mainFrame,
            text = "Add",
            command=lambda: self.addTask(addTaskEntry.get())
        )
        addTaskButton.grid(row=numTasks+1, column=1)

    def editTask(self, index, taskLabel):
        newWin = Toplevel(self.root)
        newWin.title("Edit task")

        newTaskEntry = Entry(
            newWin,
            textvariable= self.newTask
        )
        newTaskEntry.pack()

        addButton = Button(
            newWin,
            text="Edit Task",
            command=lambda: self.updateTask(newTaskEntry.get(), newWin, index, taskLabel)
        )
        addButton.pack()

    def updateTask(self, newTask, newWin, index, taskLabel):
        self.task.setTaskMsgAtIndex(index, newTask)
        taskLabel.config(text=newTask)
        index = 0
        newWin.destroy()

    def deleteTask(self, index, taskLabel):
        self.task.removeTaskAtIndex(index)
        taskLabel.config(text="")
        index = 0

    def addTask(self, msg):
        self.task.addTaskByMsg(msg)
        
        taskLabel = Label(
            self.mainFrame,
            width=10,
            text=msg
        )
        taskLabel.grid(row=numTasks, column=0)

        editButton = Button(
            self.mainFrame,
            text="Edit",
            command=lambda index=numTasks, label=taskLabel: self.editTask(index, label)
        )
        editButton.grid(row=numTasks, column=1)

        deleteButton = Button(
            self.mainFrame,
            text="Delete",
            command=lambda index=numTasks, label=taskLabel: self.deleteTask(index, label)
        )
        deleteButton.grid(row=numTasks, column=2)

    def run(self):
        self.createWidgets()
        self.root.mainloop()

def main():
    task = TaskList()
    task.addTaskByMsg("Buy Milk")
    task.addTaskByMsg("Buy Eggs")
    task.addTaskByMsg("Go to Work")
    task.addTaskByMsg("Go to Gym")
    app = ToDoList(task)
    app.run()

main()
