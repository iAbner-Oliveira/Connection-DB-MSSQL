<h1 align="left"> PYTHON - Database Connection <b>MSSQL</b> </h1>

Script created in python to validate connection with the database

## :snake: Functionality for Script.

- `Functionality 1`: Validate connection to <b>SQL SERVER</b> database,
- `Functionality 2`: Output for datas.

## Setup

### Python Version

It is recommended that for full script functionality the Python version is `3.9` or higher.

### Install and add to the following Python libraries;

```MSSQL Connector
pip install pyodbc
```

### If you don't have PIP installed, run this command:

For Debian-based distributions
```
apt-get install python-pip
```
For RedHat-based distributions
```
yum install python-pip
```

<hr>



## :snake: Script 1  - Validate Database Connection

```python

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


```


## :snake: <b>Script 2</b> - Datas

```python
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

cursor.execute("SELECT TOP 10 * FROM <table name>;")  # This line is responsible for executing the command inside the database

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()


```
<hr>

<h3>Observation;</h3>

<p>The cursor is responsible for executing the command within the database and returning the assigned value.</p>

