import pyodbc

server = '<ip\host>'  # Example: '198.163.12.98\MSS'
database = '<db name>'
username = '<username database>'
password = '<database password>'

CON = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'  # Version of your connecting ODBC driver 
                      'SERVER='+server+';'
                      'DATABASE='+database+';'
                      'UID='+username+';'
                      'PWD='+password+';')

cursor = CON.cursor()

cursor.execute("SELECT @@version;")  # Will return the connected database version

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()
