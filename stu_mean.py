import sqlite3

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
#===========================================================

#Look up each student's grade

pleasePrint = c.execute("SELECT name, mark FROM peeps,courses WHERE peeps.id=courses.id")
for row in pleasePrint:
	print row
	







#==========================================================
db.commit() #save changes
db.close()  #close database
