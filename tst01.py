'''import pyautogui
from time import sleep'''

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
'''
from cadastro_pedido_entrada import *
from editar_pedido_compra import *
from cancela_pedido_compra import *

print("===========================")
print("Qual módulo deseja iniciar?")
print("/n")
print("1 - CAD PED ENT")
print("2 - EDIT PED ENT")
print("3 - CANCEL PED ENT")
print("===========================")
i = input()

if (i == 1):
    print(i)
    cadastroPedEntrada()
    print(i)
elif (i == 2):
    print(i)
    editaPedVend()
    print(i)
elif (i == 3):
    print(i)
    cancelaPedComp()
    print(i)'''