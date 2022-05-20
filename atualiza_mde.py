import os
from tkinter import *
from tkinter import filedialog
from tkinter import Tk
from tkinter import PhotoImage
import pyautogui
import tkinter as tk
import shutil
import time
from datetime import datetime, timezone
from datetime import *
import os as sistema

#Servidor onde fica o MDE de PRODUÇÃO
servidorProd = (rf"\\vm-srvfile01\Produtos\ERP\Medicamento\Fontes\Versão 10.0\Publicados\Desktop")
#Pasta de imagens do servidor
pastaImg = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

def atualizaMde():

    root = tk.Tk()
    #Alerta para selecionar o novo MDE
    pyautogui.alert("ATENÇÃO! SELECIONE O NOVO ARQUIVO DO MDE")
    #Seleciona o MDE para copiar para a pasta local
    filename = filedialog.askopenfilename(initialdir = rf"{servidorProd}", title = "Selecione o novo MDE", 
                                        filetypes = (("Atalhos",  "*.mde*"), ("Todos Arquivos", "*.*")))
    #Alerta para selecionar a pasta onde o MDE será colocado
    pyautogui.alert("ATENÇÃO! SELECIONE A PASTA PARA INSERIR O MDE COPIADO")
    #Seleciona o diretório em que o MDE será copiado
    path = filedialog.askdirectory(initialdir="/", title="Selecione a pasta de DESTINO do MDE")
    #print(path)
    #Busca pelo arquivo OuroWeb.mde
    file_oldname = os.path.join(path, "OuroWeb.mde")
    #Variável com o nome _OuroWeb.mde
    nomeArquivoMde = '_OuroWeb.mde'
    #Seleciona o Usuário que está logado na máquina
    usuario = sistema.getlogin()
    #Data e hora
    #Seta a data/hora atual da máquina
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("Old_%d%m%y_%H%M_")
    #print(data_e_hora_em_texto)
    #Concatena o nome do arquivo com o data_e_hora + usuario + nomeArquivoMde
    novoNomeArquivoMde = (data_e_hora_em_texto + usuario + nomeArquivoMde)
    #Print no console com o novo nome digitado + extensão do arquivo
    #print(novoNomeArquivoMde)
    #Renomeia o arquivo MDE com a variável novoNomeArquivoMde
    file_newname_newfile = os.path.join(path, novoNomeArquivoMde)
    rename = os.rename(file_oldname, file_newname_newfile)
    #Copia o novo MDE
    source_file = os.path.join(filename)
    #Cola na pasta o novo MDE
    destination_file = os.path.join(path)
    shutil.copy(source_file, destination_file)
    
    
    #implementar
    #entrar no caminho do mde antigo e copiar a linha
    #entrar no novo mde e colar a linha inteira
    #clicar no checkbox para anexar a base

    #pyautogui.alert("ATENÇÃO! O MDE ANTIGO SERÁ DELETADO.")
    #os.remove(file_newname_newfile)
    def fecharJanela():
        janela.destroy()
    fecharJanela()

janela = Tk()
janela.title('Atualização de MDE')
janela.geometry('338x100')
bg = PhotoImage(file = "setor-de-testes-branco.png")
canvas1 = Canvas(janela, width = 338, 
                 height = 100) 
canvas1.pack(fill = "both", expand = TRUE) 
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw")

button1 = Button( janela, text = "Atualiza MDE",command= atualizaMde, bg='black',fg='white')

button1.pack()
button1.place(rely=1, relx=1, x =-140, y =-50, anchor=SE)
janela.resizable(width = False, height = False)
mainloop()