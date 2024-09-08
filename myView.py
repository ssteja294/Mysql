# Mysql View usage in framework

import mysql.connector

DbConnection = mysql.connector.connect(host='138.68.140.83', user='saiteja', password='Saiteja@123', database='dbSaiteja')
DbCursor = DbConnection.cursor()
def createView():
	DbCursor.execute("DROP VIEW IF EXISTS FrameworkTable2")
	DbCursor.execute("CREATE view FrameworkTable2 as SELECT * FROM Item")

def loadTableColumns():
	global DbCursor, Fields
	DbCursor.execute("SHOW COLUMNS FROM FrameworkTable2")
	Fields = [FieldName[0] for FieldName in DbCursor.fetchall()]

def addRecord():
	DbCursor.execute("INSERT into FrameworkTable2 values('TV1397', 'Telivision', 29000, 'LG123', 100)")
    DbConnection.commit()


DbCursor.execute("SELECT * from FrameworkTable2")
Items = DbCursor.fetchall()
for Item in Items:
    for FieldCounter, Field in enumerate(Fields):
      print(f"{Field}: {Item[FieldCounter]}")
    print("\n")
createView()
loadTableColumns()
