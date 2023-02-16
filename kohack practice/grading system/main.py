import sqlite3
from studentclass import student
from teacherclass import teacher
from classesclass import classes
from adminclass import admin
#Put in a while loop. If none of these values are inputed then restart a loop.
theAdmin = admin(1234)
while True:
    accountType = int(input("What type of account would you like to access or create? For admin type 1. For teacher type 2. For student type 3"))
    #if admin then ask for the admin password. For now it is too complicated to make this multischool
    if accountType == 1:
        
        action = int(input("Type the admin password"))
        if action == 1234:
            action = int(input("Which action would you like to do? To add a teacher type 1. To add a student type 2. To add a class type 3. To add a student to a class type 4. to restart type anything else."))
            if action == 1:
                name = input("what is the teachers name")
                tid = int(input("what is the teachers id"))
                email = input("what is the teachers email")
                password = input("what is the teachers password")
                theAdmin.addteacher(name,tid,email,password)
            if action == 2:
                name = input("what is the students name")
                sid = int(input("what is the students id"))
                email = input("what is the students email")
                password = input("what is the students password")
                theAdmin.addstudent(name,sid,email,password)

            if action == 3:
                subject = input("what is the subject")
                tid = int(input("what is the teachers id"))
                cid = int(input("what is the class id"))
                period = int(input("during which period is this class"))
                theAdmin.addclass(subject,tid,cid,period)

            if action == 4:
                name = input("what is the students name")
                sid = int(input("what is the teachers id"))
                cid = int(input("what is the class id"))
                theAdmin.astc(cid,name,sid)
    #if teacher
    if accountType == 2:
        name = input("What is your name?")
        tid = int(input("what is your id"))
        email = input("what is your email")
        password = input("what is your password")
        theTeacher = teacher(name,tid, email, password)
        theTeacher.findcids()
        #see what the teacher wants to do
        action = int(input("If you want to add an assignment type 1. If you want to add a grade type 2. To restart type anything else."))
        
        if action == 1:
            assignment = input("what is the assginment name please note that it can only be one word no spaces")
            cid = int(input("what is the class id"))
            
            theTeacher.addAssignment(cid,assignment)
        
        if action == 2:
            cid = str(int(input("what is the class id")))
            con = sqlite3.connect("classes.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM a"+cid+";")
            print("your current assginments and grades are:\n")
            print(theTeacher.assignments)
            print(cur.fetchall())
            con.close()
            assignment = input("what is the assginment name")
            
            sid = int(input("what is the student id of the student whos grade you want to add"))
            grade = int(input("what is the grade"))
            theTeacher.addGrade(sid,assignment,grade,cid)
    #if student
    if accountType == 3:
        name = input("what is your name")
        email = input("what is your email")
        sid = str(int(input("what is your student id")))
        password = input("what is your password")
        theStudent = student(name, sid, email, password)
        cid = input("what is the class id")
        print("note that your grades start from the third number and on")
        theStudent.getGrade(cid)



                

    

