import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3306",
  password="Ayush"
)
mycursor = mydb.cursor()

mycursor.execute("Use PHARMACY ")

try:    
    mycursor.execute("""CREATE TABLE Medicine(Name VARCHAR(255) NOT NULL,    Manf VARCHAR(255),    price INT(255),    Quantity INT(255),    Symptom VARCHAR(255)    );""")
except mysql.connector.errors.ProgrammingError:
    pass
   
def searchMedicine(Name):
    mycursor.execute("""SELECT * FROM Medicine WHERE Name LIKE "{Name}%" """.format(Name=Name))
    values =[]
    for i in mycursor:
        values.append(i)
    return values 
def searchMedicineSymptom(Name):
    mycursor.execute("""SELECT * FROM Medicine WHERE Symptom LIKE "{Name}%" """.format(Name=Name))
    values =[]
    for i in mycursor:
        values.append(i)
    return values 

def searchMedicineBrand(Name):
    mycursor.execute("""SELECT * FROM Medicine WHERE Manf LIKE "{Name}%" """.format(Name=Name))
    values =[]
    for i in mycursor:
        values.append(i)
    return values

def addRecord(Name,Manf,Price,Quantity,Symptom):
    mycursor.execute("INSERT INTO Medicine(Name,Manf,Price,Quantity,Symptom)VALUES(%s,%s,%s,%s,%s)",(Name,Manf,Price,Quantity,Symptom))

def updateCase(Quantity,name,man):
    mycursor.execute(""" UPDATE Medicine SET Quantity="{Quantity}" WHERE Name="{name}"AND Manf="{man}" """.format(Quantity=Quantity,name=name,man=man))
    
    