import sqlite3
#from studentclass import student
#from teacherclass import teacher
#from classesclass import classes
#from adminclass import admin
class classes:
    def __init__(self,subject,tid,cid,period):
        self.subject = subject
        self.tid = tid
        self.cid = cid
        self.period = period
