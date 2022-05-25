import pyodbc 

CGC = 17114621000107

x1 = pyodbc.connect('Driver={SQL Server};'
                      'Server=SRV-TST03\SQL2019;'
                      'Database=GomedVs1012_TST;'
                      'Trusted_Connection=yes;')

cursor = x1.cursor()
cursor.execute(rf'select top 10 pk_int_Cadastro from Tab_Cadastro')

for i in cursor:
    print(i)