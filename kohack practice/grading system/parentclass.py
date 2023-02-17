from studentclass import student
class parent(student):
  def __init__(self, name, sid, email, password,parentName):
    self.parentName = parentName
    self.name = name
    self.sid = sid
    self.email = email
    self.password = password
  def feedback(self,tid,feedback):
    con = sqlite3.connect("teachers.db")
    cur = con.cursor()
    cur.execute("INSERT INTO" + "a" +tid+ "VALUES(?,?)",(feedback,self.parentName))
    con.commit()
    con.close()
    
