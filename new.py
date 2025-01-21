#oop *****
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

#Threading *****
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

#multiprocessing *****
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

#coroutine *****

import asyncio #asynchronous mechanisms asyncio module

async def my_coroutine():
    print("Start of coroutine")
    await asyncio.sleep(2)  # Non-blocking wait (simulates I/O)
    print("End of coroutine")

# Running the coroutine
asyncio.run(my_coroutine())
#By combining coroutines and tasks with the asyncio module, Python can handle I/O-bound tasks concurrently without blocking the execution of the program.



#generators in python *****
def count_up_to(n):#generator function/yield
    count = 1
    while count <= n:
        yield count  # Yield the current count value
        count += 1

# Create a generator object
counter = count_up_to(5)

# Iterate over the generator
for number in counter:
    print(number)

#generators are memory efficient, lazy evaluation, can be used to implement cooperative multitasking
#Generator expression
squares = (x * x for x in range(1, 6))

# Iterate over the generator
for square in squares:
    print(square)

#chain generators
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def square_numbers(n):
    for i in range(n):
        yield i * i

# Chain the generators *****
even_gen = even_numbers(10)
square_gen = square_numbers(10)

for num in even_gen:
    print(num)

for num in square_gen:
    print(num)

#send() in generators
def simple_gen():
    value = yield "Hello"
    print(f"Received value: {value}")
    yield "World"

# Create a generator
gen = simple_gen()

# Start the generator and get the first yielded value
print(next(gen))  # Output: Hello

# Send a value back into the generator and resume execution
print(gen.send("Python"))  # Output: Received value: Python
                           # Output: World


#decorators *****
def decorator_function(original_function):
    def wrapper_function():
        # Add extra functionality before or after the original function
        print("Wrapper executed before the function")
        original_function()
        print("Wrapper executed after the function")
    return wrapper_function

@decorator_function  # The decorator syntax
def display():
    print("Display function executed")

display()  # Calling the decorated function


#socket programming *****
#server side
import socket

server_socket = socket.socket()

server_socket.bind(('localhost', 9999))

server_socket.listen(5) # Maximum number of connections allowed

print("server is listening for connection...")

client_socket, client_address = server_socket.accept()
print(f"connection established with {client_address}")
client_socket.send(b"hello, client")

data = client_socket.recv(9999)

print(f"received from client: {data.decode()}")

client_socket.close()
server_socket.close()


#client side

import socket

client_socket = socket.socket()

client_socket.connect(('localhost', 9999))

data = client_socket.recv(9999)

print(f"received from server: {data.decode()}")

client_socket.send(b"hello, server")
client_socket.close



#numpy *****
#numpy is a library for mathematical computation

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Element-wise operations
arr2 = arr * 2
print(arr2)  # Output: [2 4 6 8 10]

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Shape of the array
print(matrix.shape)  # Output: (3, 3)

# Matrix multiplication
result = np.dot(matrix, matrix)
print(result)

# Generate a random array
random_array = np.random.rand(3, 3)  # 3x3 matrix of random numbers between 0 and 1
print(random_array)


#pandas *****
#open source data analysis & manipulation library

import pandas as pd
# Create a Series
data = [10, 20, 30, 40]
series = pd.Series(data)

print(series)

# Create a DataFrame from a dictionary
data = {
    'name': ['jay', 'raj', 'ram'],
    'Age':  [21, None, 23],
    'City': ['pune', 'surat', 'ayodhya']
}

df = pd.DataFrame(data)

print(df)

print(df.head(2))

print(df.describe())

# Filter rows based on condition
final_df = df[df['Age'] > 21]
print(final_df)

# Access multiple columns
print(df[['Age', 'name']])

# Access by index position (iloc)
print(df.iloc[0])  # First row
print(df.iloc[0:2])  # First two rows

# Access by index label (loc)
print(df.loc[0])  # First row

print(df.shape) # (number of rows, number of columns)
print(df.info()) # Info about DataFrame

print(df.isnull().sum()) # Detect missing values # True for missing values

df_filled = df.fillna(value={'Age': 22})
print(df_filled)

df_cleaned = df.dropna() #drop row with missing values

print(df_cleaned)

# Create two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Category': ['X', 'Y', 'Z']})

# Merge DataFrames on a common column 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # 'left', 'right', 'outer', 'inner'
print(merged_df)

#operators in pandas
import pandas as pd

var = pd.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8]})
print(var)  # prints the DataFrame

var["c"] = var["a"] + var["b"] # for +,*,-,/,%
print(var) 


#inster & delete in pandas
import pandas as pd

var = pd.DataFrame({"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8], "c" : [9, 10, 11, 12]})
var.insert(2,"py",var["a"])
print(var)

#delete
var.pop("b") #or you can use del

print(var)


#creating a csv file in pandas *****
import pandas as pd

dis = {"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8], "c" : [9, 10, 11, 12]}
d = pd.DataFrame(dis)

print(d)

d.to_csv("test_new.csv", index = False)


#read a csv file *****

import pandas as pd

csv_1 = pd.read_csv("C:\\Users\\ITIDOLLAPTOP-33\\Downloads\\day.csv")
print(csv_1)

#drop rows and columns
#drop columns
import pandas as pd

df = pd.read_csv("C:\\Users\\ITIDOLLAPTOP-33\\Downloads\\day.csv")
df_cleaned_columns = df.dropna(axis=1)
print(df_cleaned_columns)

#drop rows
import pandas as pd

df = pd.read_csv("C:\\Users\\ITIDOLLAPTOP-33\\Downloads\\day.csv")
df_cleaned = df.dropna()
print(df_cleaned)

#fill null values with mean
import pandas as pd

df = pd.read_csv("C:\\Users\\ITIDOLLAPTOP-33\\Downloads\\day.csv")
# Fill missing values with 0
df_filled = df.fillna(0)

# Fill missing values with the mean of each column
df_filled_mean = df.fillna(df[['N1','N2']].mean())

print(df_filled_mean)

#sorting in pandas *****

import pandas as pd

data = {
    "Name": ["John", "Mary", "David", "Emily"],
    "Age": [35, 30, 25, 40],
    "salary": [55000, 65000, 50000, 65000]
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by =["Age", "salary"], ascending = [True, False])

print(sorted_df)

#convert datatype
#with above code
df['Salary'] = df['Salary'].astype(float) # Convert Salary to float
print(df.dtypes)
print(df)

#apply custom function
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

# Function to categorize age
def categorize_age(age):
    if age < 30:
        return 'Young'
    elif age < 40:
        return 'Middle-aged'
    else:
        return 'Senior'

df['Age Category'] = df['Age'].apply(categorize_age)
print(df)

#Merging data frames *****

import pandas as pd

# DataFrame 1
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
}

df1 = pd.DataFrame(data1)

# DataFrame 2
data2 = {
    'ID': [1, 2, 4, 5],
    'Salary': [50000, 60000, 70000, 75000],
}

df2 = pd.DataFrame(data2)

# Merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)

#joining  *****

import pandas as pd

# DataFrame 1
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
}

df1 = pd.DataFrame(data1).set_index('ID')

# DataFrame 2
data2 = {
    'Salary': [50000, 60000, 70000, 75000],
}

df2 = pd.DataFrame(data2, index = [1, 2, 4, 5])

# Merge on the 'ID' column
joined_df = df1.join(df2, how='inner')
print(joined_df)


