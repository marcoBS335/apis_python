import pyodbc
server = 'apis-server.database.windows.net'
database = 'APIS Database'
username = 'milan4apis'
password = 'apisMilan99'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP 1 FROM [dbo].[skuska_kalkulacka] ORDER BY ID DESC")
row = cursor.fetchone()
while row:
    print (str(row[1]) + str(row[3]) + str(row[2]))
    row = cursor.fetchone()
