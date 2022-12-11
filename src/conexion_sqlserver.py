import pyodbc

try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=MANY\SQLEXPRESS;DATABASE=Spanish;UID=Many\Manuel;Trusted_Connection=yes;')
    print ('conexion exitosa',connection)
    cursor=connection.cursor()
    cursor.execute("Select c.ChannelName, year(f.DateKey) anho, count(Saleskey) cant_facturas from FactSales f, DimChannel c where f.StoreKey=c.ChannelKey and f.DateKey between '2008-01-01'  and '2008-12-31' group by c.ChannelName, year(f.DateKey)")
    row=cursor.fetchone()
    print(type(row))
except Exception as exception:
    print(exception)


