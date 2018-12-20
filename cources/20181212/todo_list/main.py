#coding=utf-8

from TodoInputter import *
from TodoStore import TodoStore
from Todo import Todo
import csv
import time

# inputter = TodoInputter()
# inputter.start()
d = time.time(time.localtime())
store = TodoStore('todo.csv')
todo = Todo(id=10, desc="lalala", status=0, createTime=d, completeTime=d)