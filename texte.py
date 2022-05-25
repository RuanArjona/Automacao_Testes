pathdoc = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\doc")

#Open the file back and read the contents
f=open(rf"{pathdoc}\ NUMERO-PEDIDO-COMPRA.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)
#or, readlines reads the individual line into a list
#fl =f.readlines()
#for x in fl:
#print(x)