#coding=utf-8

"""
待办项类
"""
import time
import utils

class Todo():
    baseId = 0 # 初始id，每个Todo的id都由它+1生成，静态变量
    __id = 0 # todo项的id，唯一，且不能修改
    """
    todo项的状态，0表示未完成，1表示已完成，外界只能通过complete方法修改
    """
    __status = 0 # 待办项初始化时默认为未完成

    def __init__(self, desc="", id=None, status=0, createTime=None, completeTime=None):
        self.__id = id or self.__createTodoId()
        self.__status = status
        self.desc = desc
        self.createTime = createTime or utils.getCurrentTime()
        self.completeTime = completeTime

    def getId(self):
        "获取todo的id"
        return self.__id

    def __createTodoId(self):
        tmp = Todo.baseId # 先把当前的baseId保存起来，这也是当前todo的id
        Todo.baseId += 1 # 让baseId加1，供下一个todo生成id时使用

        return tmp # 返回的是当前的id，也就是baseId未加1的值
    
    def complete(self):
        "将todo设置成完成状态"
        self.__status = 1
        self.completeTime = utils.getCurrentTime()

    def isComplete(self):
        "该todo项是否已完成"
        return self.__status == 1
    
    def toString(self):
        "把todo项转成可打印的字符串信息"
        string = "id: " + str(self.__id) + " ,描述: " + self.desc + ", 创建时间: " + self.createTime + ", 是否已完成: " + str(self.isComplete())
        if self.isComplete():
                string += (", 完成时间: " + self.completeTime)
        
        return string