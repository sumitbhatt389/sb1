class Student:#oop
    name = "jay"
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        print("adding new student in database..")
s1 = Student("jay", 98)
print(s1.name, s1.marks)

s2 = Student("vijay", 88)
print(s2.name, s2.marks)

#oop args and contructor
class Student:#oop
    college_name = "vdp"

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)
    
    def get_marks(self):
        return self.marks


s1 = Student("jay", 98)
s1.welcome()
print(s1.get_marks())

#oop demo how objects can relate 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self, amount):
        self.balance =- amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")

    def get_balance(self):
        return self.balance  
    

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)

#Threading
#i/o bound tasks , concurrency , shared memory , low overhead,
import threading
import time

def task():
    for i in range(5):
        time.sleep(1)
        print(i)

# Create and start a thread
thread = threading.Thread(target=task)
thread.start()

# Wait for thread to finish
thread.join()

print("Thread finished execution")

#multiprocessing
#cpu bound tasks, parallelism, separate memory space, high overhead,
import multiprocessing
import time

def task():
    for i in range(5):
        time.sleep(1)
        print(i)

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)
    process.start()


    process.join()

    print("process finished execution")

#coroutine

import asyncio #asynchronous mechanisms asyncio module

async def my_coroutine():
    print("Start of coroutine")
    await asyncio.sleep(2)  # Non-blocking wait (simulates I/O)
    print("End of coroutine")

# Running the coroutine
asyncio.run(my_coroutine())
#By combining coroutines and tasks with the asyncio module, Python can handle I/O-bound tasks concurrently without blocking the execution of the program.
