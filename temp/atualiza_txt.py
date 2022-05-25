import socket
path = (rf"C:\Custom Software\ERP\OuroNetApp")


def alteraTexto():
    OuroNetMov = 'OuroNetMovimento'
    OuroNetFin = 'OuroNetFinanceiro'
    OuroNetCad = 'OuroNetCadastro'
     # Abrir o arquivo em modo de leitura
    with open(rf"{path}\OuroNetApp.exe.config", 'r') as fd:
        txt = fd.read()  # Ler todo o arquivo
        # ocorrências no texto lido
        txt = txt.replace(OuroNetMov, OuroNetMov + 'Teste')
        print(txt)
        txt = txt.replace(OuroNetFin, OuroNetFin + 'Teste')
        print(txt)
        txt = txt.replace(OuroNetCad, OuroNetCad + 'Teste')
        print(txt)
    # Abrir o arquivo em modo de escritaS
    with open(rf"{path}\OuroNetApp.exe.config", 'w') as fd:
        fd.write(txt)  # Escrever texto modificado