import sqlite3
#from teacherclass import teacher

class student:
    def __init__(self, name, sid, email, password):
        self.name = name
        self.sid = sid
        self.email = email
        self.password = password

    def getGrade(self,cid):
        con = sqlite3.connect("classes.db")
        cur = con.cursor()
        #print(theTeacher.assignments)
        cur.execute("SELECT * FROM " +'a'+ str(cid) + " WHERE sid IS ?;",(self.sid))
        print(cur.fetchall())
        con.commit()
        con.close()