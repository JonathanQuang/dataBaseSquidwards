import sqlite3

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
#===========================================================
listOfRows = []


#Look up each student's grade

pleasePrint = c.execute("SELECT name, mark, peeps.id FROM peeps,courses WHERE peeps.id=courses.id")
for row in pleasePrint:
	row = str(row)
	row = row[2:row.find(")")]
	listOfRows.append(row)
	print row
	
#print listOfRows

#compute each students average
sumDict = {}
occurenceDict = {}
idDict = {}
for row in listOfRows:
	#turn the list of rows into something useful
	splitData=row.split(",")
	splitData[0]=splitData[0][1:len(splitData[0])-1	]
	splitData[1]=int(splitData[1])
	splitData[2]=int(splitData[2])
	
	#updates if data entry already exists
	if splitData[0] in sumDict:
		sumDict[splitData[0]] = sumDict[splitData[0]] + splitData[1]
		occurenceDict[splitData[0]] = occurenceDict[splitData[0]] + 1
	else:
		sumDict[splitData[0]] = splitData[1]
		occurenceDict[splitData[0]]= 1
		idDict[splitData[0]]=splitData[2]
		
#print sumDict
#print occurenceDict
#print idDict

averageDict={}
for key in sumDict:
	averageDict[key]=sumDict[key]/occurenceDict[key]

#print averageDict

#display each students name,id, and average
for key in averageDict:
	print key + " |average=" + str(averageDict[key]) + " | id=" + str(idDict[key])
	





#==========================================================
db.commit() #save changes
db.close()  #close database
