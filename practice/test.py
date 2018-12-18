# coding=utf-8

import csv
import time

def readFile():
    with open('todo.csv') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        todos = []
        for row in reader:
            todoDesc = ''
            for i in range(len(row)):
                val = row[i]
                headerDesc = header[i]
                todoDesc += (headerDesc + ": " + val + ", ")

            todos.append(todoDesc)
            todoDesc = ""

        print todos

# readFile()

def writeRow():
    with open('todo.csv', 'ab') as f:
        writer = csv.writer(f)
        d = time.time()
        row = [1, 'lalala', 0, d, d]

        writer.writerow(row)

writeRow()