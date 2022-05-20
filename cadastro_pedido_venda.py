from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 30/12/2021
def cadastroPedVenda():
    #Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Venda / Saída > Pedido de Venda
    pyautogui.hotkey('ctrl','p')
    time.sleep(20)
    #Clica no botão para maximizar a janela
    maximizaTela()
    time.sleep(5)
    #Seleciona o campo do cliente
    cad_ped_vend_cliente = pyautogui.locateOnScreen(rf"{path}\cad_ped_vend_cliente.png", confidence=0.9)
    pyautogui.click(cad_ped_vend_cliente)
    time.sleep(5)
    #Insere um clinte
    #cliente na MILFARMA
    pyautogui.write("00000002")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)
    #Seleciona o campo º Doc
    pyautogui.press('tab',presses=3)
    time.sleep(5)
    #Chama o método para salvar o número do Pedido Venda
    salvaNumeroPedVend()
    time.sleep(5)
    #Seleciona o campo Desc. do Item no Pedido de Venda
    time.sleep(10)
    pyautogui.press('tab',presses=11)
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
        #Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        time.sleep(10)
    #Chama o método concluirPedVend
    time.sleep(5)
    concluirPedVend()
    time.sleep(5)
    #Implementado 06/01/2022
    time.sleep(5)
    #Clica no botão X para fechar a tela que está aberta
    fechaTela()