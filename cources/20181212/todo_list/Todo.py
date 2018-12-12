#coding=utf-8

"""
待办项类
"""
import time
import utils

class Todo():
    __id # todo项的id，唯一，且不能修改
    """
    todo项的状态，0表示未完成，1表示已完成，外界只能通过complete方法修改
    """
    __status 

    def __init__(self, desc=""):
        self.__id = utils.createTodoId()
        self.desc = desc
        self.__status = 0 # 待办项初始化时默认为未完成
        self.createTime = utils.getCurrentTime()

    def getId(self):
        "获取todo的id"
        return self.__id
    
    def complete(self):
        "将todo设置成完成状态"
        self.__status = 1
        self.completeTime = utils.getCurrentTime()

    def isComplete(self):
        "该todo项是否已完成"
        return self.__status == 1
    
    def toString(self):
        string = "描述: " + self.desc + ", 创建时间: " + self.createTime + ", 是否已完成: " + self.isComplete() 
        if self.isComplete():
                string += (", 完成时间: " + self.completeTime)
        
        return string