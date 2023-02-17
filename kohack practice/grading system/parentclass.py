from studentclass import student
class parent(student):
  def __init__(self,parentName, name, sid, email, password):
    super().__init__(name, sid, email, password)
    self.parentName = parentName
  def feedback(self,tid,feedback):
    con = sqlite3.connect("teachers.db")
    cur = con.cursor()
    cur.execute("INSERT INTO" + "a" +tid+ "VALUES(?,?)",(feedback,self.parentName))
    con.commit()
    con.close()
    
