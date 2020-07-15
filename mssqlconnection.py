import pyodbc
server = '.\sql2017'
database = 'myDB'
user = 'sa'
password = ''
cn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
cursor = cn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()