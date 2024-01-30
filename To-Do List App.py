import time
import os
class User:

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def __init__(self) :
        self.list = []
        self.task = 0
        print("Hello User, please sign up to access new feature of to do app")
        print("sign in")


    def view_task(self):
        if not self.list:
            print("No tasks to display.")
        else:
            for i, task in enumerate(self.list, start=1):
                print(f"{i}: {task}")
            print(f"Tasks remaining: {self.task}")
            time.sleep(2)
            self.clear_screen()

    def add(self):
        string = input()
        self.list.append(string)
        self.task +=1
        print("task successfully added.")


    def remove(self):
        self.view_task()
        if self.list:
            print('Select the index to remove the task.')
            index= int(input())
            if 1 <= index <= len(self.list):
                del self.list[index - 1]
                self.task -= 1
        # self.clear_screen()

    def mark(self):
        self.view_task()
        
        print('Select index of task to mark them')    
        strike_through = lambda index : ''.join([char + '\u0336' for char in (index)])
        if self.list:
            index = int(input())
            self.list[index-1] = strike_through(self.list[index-1])
            self.task -=1
        # self.clear_screen()

# I will complete this project
# even if it cost me, my life
# hah! finally completed

krrish = User()
krrish.add()
krrish.add()
krrish.add()
krrish.view_task()
time.sleep(3)
krrish.remove()
krrish.mark()
krrish.mark()
krrish.view_task()