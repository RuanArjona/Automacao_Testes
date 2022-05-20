from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 08/12/2021
def cadastroOrc():
    #Selecionar a janela do Ouro Web
    #pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #Menu Principal
    #time.sleep(5)
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Venda / Saída > Orçamento
    pyautogui.hotkey('ctrl','o')
    time.sleep(15)
    #Clica no botão para maximizar a janela
    maximizaTela()
    time.sleep(5)
    #Seleciona o campo do cliente
    cad_orc_cli = pyautogui.locateOnScreen(rf"{path}\cad_orc_cli.png", confidence=0.9)
    pyautogui.click(cad_orc_cli)
    time.sleep(5)
    #Insere um clinte
    #cliente na MILFARMA
    pyautogui.write("00000002")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)
    #Seleciona o campo Nº Doc.
    pyautogui.press('tab',presses=2)
    #Chama método salvaNumeroOrc
    salvaNumeroOrcVend()
    #Seleciona o campo Desc. do Item no orçamento de venda
    time.sleep(5)
    pyautogui.press('tab', presses=12)
    time.sleep(2)
    #Seta para baixo para selecionar um produto
    pyautogui.press('down')
    time.sleep(2)
    #Implementado - Renan 22/12/2021
    #Verifica se tem produto disponível
    while pyautogui.locateOnScreen(rf"{path}\cad_orc_qtd_disp_zero.png"):
        time.sleep(1)
        pyautogui.press('down')
    #Encontra o produto disponível e aperta enter    
    else:
        pyautogui.press('enter')
        time.sleep(5)
        #Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        time.sleep(10)
        #Implementado - Renan 10/12/2021
    time.sleep(10)
    #Chama o método concluirOrc para concluir o Orçamento de Venda
    concluirOrc()
    #Implementado 06/01/2022
    time.sleep(5)
    #Clica no botão X para fechar a tela que está aberta
    fechaTela()