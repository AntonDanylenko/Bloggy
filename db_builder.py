# creates tables for database stored in DB_FILE: blogs.db
# field names created; no records
import sqlite3   #enable control of an sqlite database

DB_FILE="blogs.db"


def createTable(tableName, fieldNames):
	db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops
	commandArgs = "("
	colTypes = []
	for name in fieldNames:
		commandArgs += name + " " + fieldNames[name] + ","
		colTypes.append(fieldNames[name])
	commandArgs = commandArgs[:-1]
	# print(colTypes)
	commandArgs += ")"
	# print ("CREATE TABLE " + tableName + " "+ commandArgs)
	c.execute("CREATE TABLE " + tableName + " "+ commandArgs)
	closeDB()

def closeDB ():
	db.commit() #save changes
	db.close()  #close database

usersHeader = {"UserID":"INTEGER PRIMARY KEY","PFP":"TEXT","Username":"TEXT UNIQUE", "Password":"TEXT"}
createTable("users", usersHeader)

postsHeader = {"PostID": "INTEGER PRIMARY KEY", "BlogId": "INTEGER", "AuthorID": "INTEGER", "Content":"TEXT", "Timestamp":"DATETIME", "VOTES":"INTEGER"}
createTable( "posts", postsHeader)

blogsHeader = {"BlogID":"INTEGER PRIMARY KEY", "OwnerID":"INTEGER", "CollaboratorIDs":"TEXT","BlogName":"TEXT", "Category":"TEXT"}
createTable("blogs", blogsHeader)
