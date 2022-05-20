from login_ouro import *
from cadastro_cli_for import *
from config_ouro import *
from cadastro_empresa import *
from tkinter import *
from tkinter import Tk
import pyautogui

path = (r"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

def teste_automatico_ouro():
    
    #Inicia o Ouro

    #Implementação - Renan 02/12/2021
    #verifica se o aplicativo Ouro Web está aberto
    if pyautogui.locateOnScreen(rf"{path}\barra_app_ouroweb.png", confidence=0.9):
        click_ouro_web_atalho = pyautogui.locateOnScreen(rf"{path}\barra_app_ouroweb.png", confidence=0.9)
        pyautogui.click(click_ouro_web_atalho)
        #Minimiza as telas do Ouro
        #minimizarTelas()
        #Fechar telas OuroNet
        fecharTelasOuroNet()
        #Fechar telas OuroWeb
        fecharTelasOuroWeb()
        #Cadastro de Empresas
        cadastroEmpresas()
        #Abre a tela de Cadastro de Cliente / Fornecedor > aba Outros e cria a Mensagem no botão Mensagens Dinâmicas
        #cadastroCliFor() 
    else:
        selecAppOuro()
        #Faz o login
        loginOuro()
        #Minimiza as telas do Ouro
        fecharCompromissos()
        #Fechar telas OuroNet
        fecharTelasOuroNet()
        #Fechar telas OuroWeb
        fecharTelasOuroWeb()
        #Cadastro de Empresas
        cadastroEmpresas()
        #Abre a tela de Cadastro de Cliente / Fornecedor > aba Outros e cria a Mensagem no botão Mensagens Dinâmicas
        #cadastroCliFor()

    #Implementação - Renan 02/12/2021    
    #Fechar janela
    def closeJanela():
        janela.destroy()
    closeJanela()

janela = Tk()
janela.geometry('200x50')
botao = Button(janela, text='Testa Ouro', command= teste_automatico_ouro )
botao.pack()
mainloop()


#alert(text='Teste concluído com sucesso!', title='Mensagem:', button='OK')