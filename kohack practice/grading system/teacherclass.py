import sqlite3


from classesclass import classes
#from adminclass import admin
class teacher:
    def __init__(self,name,tid, email, password):
        self.name = name
        #tid stands for teacher id can't use id keyword
        self.tid = tid
        self.email = email
        self.password = password
        self.assignments = ["name","sid"]
    #find class ids that include this teacher
    def findcids(self):
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cids = []
        cur.execute("SELECT cid FROM classes WHERE tid IS ?;",(str(self.tid)))
        cids.append(cur.fetchall)
        con.close()
    
    #make a new assignment with a new grade
    def addAssignment(self,cid,assignment):
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cur.execute(f"ALTER TABLE a{cid} ADD COLUMN {assignment};")
        con.commit()
        con.close()
        self.assignments.append(assignment)

    def addGrade(self,sid,assignment,grade,cid):
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        cur.execute("UPDATE" +' a'+cid+f" SET {assignment}={grade} WHERE sid = {sid};")
        con.commit()
        con.close()