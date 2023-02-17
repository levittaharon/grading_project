import sqlite3
from studentclass import student
from teacherclass import teacher
from classesclass import classes
class admin:
    def __init__(self, password):
        
        self.password = password
        #make a new teacher db for basic teacher info
        con = sqlite3.connect("teachers.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS teachers(name,tid INTEGER NOT NULL PRIMARY KEY,email,password)")
        con.close()
        #make a new student db for basic student info
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students(name,sid INTEGER NOT NULL PRIMARY KEY,email,password)")
        con.close()
        #make a new classes db for subject, teacher, and class id to be accessed by individual class dbs
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS classes(name,tid,cid INTEGER NOT NULL PRIMARY KEY,period)")
        con.close()
    #add a teacher to the system
    def addteacher(self,name,tid, email, password):
        newteacher = teacher(name,tid,email,password)
        con = sqlite3.connect("teachers.db")
        cur = con.cursor()
        cur.execute("INSERT INTO teachers VALUES (?,?,?,?)",(newteacher.name,newteacher.tid,newteacher.email,newteacher.password))
        cur.execute("CREATE TABLE IF NOT EXISTS" +tid+ "(feedback,parentName)")
        con.commit()
        con.close()

    #add a student to the system
    def addstudent(self,name,sid, email, password):
        newstudent = student(name,sid,email,password)
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("INSERT INTO students VALUES (?,?,?,?)",(newstudent.name,newstudent.sid,newstudent.email,newstudent.password))
        con.commit()
        con.close()

    def addclass(self,subject,tid,cid,period):
        #add to list of classes
        newclass = classes(subject,tid,cid,period)
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cur.execute("INSERT INTO classes VALUES (?,?,?,?)",(newclass.subject,newclass.tid,newclass.cid,period))
        con.commit()
        con.close()
        #make a db for the class to keep track of students and grades, the table name will be named by the cid
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "+'a'+ str(cid) +" (studentName,sid INTEGER NOT NULL PRIMARY KEY)")
        con.commit()
        con.close()
    #astc stands for add student to class
    def astc(self,cid,name,sid):
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cur.execute("INSERT INTO " +'a'+ str(cid) + " (studentName,sid) VALUES (?,?)",(name,sid))
        con.commit()
        con.close()


    
