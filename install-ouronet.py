import pyautogui
import os
import os as sistema
from tkinter import *
from tkinter import filedialog
from tkinter import Tk
from tkinter import PhotoImage
import tkinter as tk
import shutil
import time
import sys
from datetime import datetime, timezone
from datetime import *

#Arquivo Server Config
arquivosServConfig = (rf"C:\inetpub\wwwroot\OuroNetCadastro\custom.configuration.server.config")
#Arquvio Config
arquivosConfig = (rf"C:\inetpub\wwwroot\OuroNetCadastro\connectionStrings.config")
#Caminho da pasta OuroNetCadastro
arquivosCad = (rf"C:\inetpub\wwwroot\OuroNetCadastro")
#Caminho da pasta OuroNetFinanceiro
arquivosFin = (rf"C:\inetpub\wwwroot\OuroNetFinanceiro")
#Caminho da pasta OuroNetMovimento
arquivosMov = (rf"C:\inetpub\wwwroot\OuroNetMovimento")
#Camino dos arquivos copiados temporáriamente
arquivosTemp = (rf"C:\Arquivos_Temp")
#Caminho da Instalação do Ouro
installOuro = (rf"C:\Update_Automatico")
#Caminho do diretório de testes
servidorTeste = (rf"\\vm-srvfile01\Fontes\Application\OuroNet")
#Seleciona o diretório em que o MDE será copiado
path = filedialog.askdirectory(initialdir = rf"{servidorTeste}", title="Selecione a pasta de atualização OuroNet")
#Comando para pegar a pasta de formato normal
pasta = os.path.normpath(path)
print(pasta)
#Variável da pasta App
localApp = rf"{installOuro}\Client\App"
#Variável da pasta Server Cadastro
localServerCad = rf"{installOuro}\Server\Cadastro"
#Variável da pasta Server Financeiro
localServerFin = rf"{installOuro}\Server\Financeiro"
#Variável da pasta Server Movimento
localServerMov = rf"{installOuro}\Server\Movimento"
#Abre o arquivo install-ouro.bat
arquivo = open("install-ouro.bat", "w")
#Cria uma pasta temporária para os arquivos
arquivo.write("md "+'"'+arquivosTemp+'"')
arquivo.write("\n")
#puxa os arquivos de Configuração para a pasta C:\Arquivos_Temp
arquivo.write("copy ")
arquivo.write(arquivosConfig)
arquivo.write(" ")
arquivo.write(arquivosTemp)
arquivo.write("\n")
arquivo.write("copy ")
arquivo.write(arquivosServConfig)
arquivo.write(" ")
arquivo.write(arquivosTemp)
arquivo.write("\n")
#Escreve o comando que desinstala OuroNetApp
arquivo.write('wmic product where name="OuroNetApp" call uninstall /nointeractive')
arquivo.write("\n")
#Escreve o comando que desinstala OuroNetServerCadastre
arquivo.write('wmic product where name="OuroNetServerCadastre" call uninstall /nointeractive')
arquivo.write("\n")
#Escreve o comando que desinstala OuroNetServerMovement
arquivo.write('wmic product where name="OuroNetServerMovement" call uninstall /nointeractive')
arquivo.write("\n")
#Escreve o comando que desinstala OuroNetServerFiinancial
arquivo.write('wmic product where name="OuroNetServerFiinancial" call uninstall /nointeractive')
arquivo.write("\n")
#Cria uma pasta no c:\Update_Automatico
arquivo.write("md "+'"'+installOuro+'"')
#arquivo.write(installOuro)
arquivo.write("\n")
#puxa os arquivos do servidor para a pasta C:/Update_Automatico
arquivo.write("xcopy /s /e /q /y ")
arquivo.write('"'+pasta+'"')
arquivo.write(" ")
arquivo.write('"'+installOuro+'"')
arquivo.write("\n")
#Escreve Cd no arquivo
arquivo.write("cd ")
#Pega o caminho da variável localApp
arquivo.write(localApp)
arquivo.write("\n")
arquivo.write('msiexec /i OuroNetClientAppSetup.msi  /quiet /l*v logfilename hostA="localhost"')
arquivo.write("\n")
#Escreve Cd no arquivo
arquivo.write("cd ")
#Pega o caminho da variável localServerCad
arquivo.write(localServerCad)
arquivo.write("\n")
arquivo.write('msiexec /i OuroNetServerCadastreSetup.msi  /quiet')
arquivo.write("\n")
#Escreve Cd no arquivo
arquivo.write("cd ")
#Pega o caminho da variável localServerFin
arquivo.write(localServerFin)
arquivo.write("\n")
arquivo.write('msiexec /i OuroNetServerFinancialSetup.msi  /quiet')
arquivo.write("\n")
#Escreve Cd no arquivo
arquivo.write("cd ")
#Pega o caminho da variável localServerFin
arquivo.write(localServerMov)
arquivo.write("\n")
arquivo.write('msiexec /i OuroNet.Server.Movement.Setup.msi  /quiet')
#Copia os arquivos da temporária para pasta OuroNetCadastro
arquivo.write("\n")
arquivo.write("xcopy /s /e /q /y ")
arquivo.write('"'+arquivosTemp+'"')
arquivo.write(" ")
arquivo.write('"'+arquivosCad+'"')
arquivo.write("\n")
#Copia os arquivos da temporária para pasta OuroNetFinanceiro
arquivo.write("xcopy /s /e /q /y ")
arquivo.write('"'+arquivosTemp+'"')
arquivo.write(" ")
arquivo.write('"'+arquivosFin+'"')
arquivo.write("\n")
#Copia os arquivos da temporária para pasta OuroNetMovimento
arquivo.write("xcopy /s /e /q /y ")
arquivo.write('"'+arquivosTemp+'"')
arquivo.write(" ")
arquivo.write('"'+arquivosMov+'"')
arquivo.write("\n")
#Deleta a pasta Update_Automatico
arquivo.write("\n")
#Escreve Cd no arquivo
arquivo.write("cd ")
#Escreve o caminho do Update_Automatico
arquivo.write(installOuro)
arquivo.write("\n")
#Escreve o comando para deletar a pasta Update_Automatico
arquivo.write("rd /s /q ")
arquivo.write(installOuro)
arquivo.write("\n")
#Escreve Cd no arquivo
arquivo.write("cd ")
#Escreve o caminho do Arquivos_Temp
arquivo.write(arquivosTemp)
arquivo.write("\n")
#Escreve
arquivo.write("rd /s /q ")
arquivo.write(arquivosTemp)
#Comando para fechar o arquivo
arquivo.close()

#=======================IMPLEMENTAR ABRIR ARQUIVO=======================#
#pushd
#SRV-TST02\SQLTST2019
#SantisaVs1009_TST