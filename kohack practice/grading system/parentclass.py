from studentclass import student
class parent(student):
  def feedback(tid,feedback):
    con = sqlite3.connect("teachers.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS parentFeedback(tid,feedback)")
    cur.execute("INSERT into parentFeedback VALUES(?,?)",(tid,feedback))
    con.commit()
    con.close()
    
