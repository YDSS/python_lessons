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

def writeRow(row, f=None, filePath=None):

    def writeRowInner(writer):
        writer.writerow(row)

    if f is not None:
        writer = csv.writer(f)
        writeRowInner(writer)
    else:
        if filePath is None:
            raise Exception('need one of these args: f or filePath')

        with open(filePath, 'ab') as f:
            writer = csv.writer(f)
            writeRowInner(writer)


# writeRow(filePath="todo.csv", row=['id', 'desc', 'status', 'createTime', 'completeTime'])

def createFileWithHeader(filePath):
    header = ['id', 'desc', 'status', 'createTime', 'completeTime']

    with open(filePath, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        
# createFileWithHeader('todo2.csv')

a = ""
b = a or "1"
print b