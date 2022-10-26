import pyodbc

server = '192.168.30.122\MSS'
database = 'JDE_JDI_2'
username = 'sa'
password = 'EGE@P4$$wd'

CON = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER='+server+';'
                      'DATABASE='+database+';'
                      'UID='+username+';'
                      'PWD='+password+';')

cursor = CON.cursor()

cursor.execute("SELECT @@version;")

row = cursor.fetchone()

while row:
    print (row)
    row = cursor.fetchone()
