import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="nbdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM `myapp_notice`")
# mycursor.execute("SELECT * FROM sys.databases")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)