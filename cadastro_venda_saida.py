from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 30/12/2021
def cadastroVendaSaida():
    #Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Venda / Saída > Venda / Saída
    pyautogui.hotkey('ctrl','k')
    time.sleep(20)
    #Clica no botão para maximizar a janela
    maximizaTela()
    time.sleep(5)
    #Seleciona o campo do cliente
    cad_vend_said_cliente = pyautogui.locateOnScreen(rf"{path}\cad_vend_said_cliente.png", confidence=0.9)
    pyautogui.click(cad_vend_said_cliente)
    time.sleep(5)
    #Insere um clinte
    #cliente na MILFARMA
    pyautogui.write("00000002")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(15)
    #Aperta tab até chegar no campo Nº Doc
    pyautogui.press('tab',presses=3)
    time.sleep(10)
    #Chama o método para salvar o Nº Venda Saída
    salvaNumeroVendSaid()
    #Seleciona o campo Desc. do Item na Venda / Saída
    time.sleep(8)
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
        time.sleep(5)
        #Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        time.sleep(10)

    #Implementado - Renan 05/01/2022
    #Clica na aba Desc/Despesas/Frete/Div
    cad_vend_said_aba_ddfv = pyautogui.locateOnScreen(rf"{path}\cad_vend_said_aba_ddfv.png", confidence=0.9)
    pyautogui.click(cad_vend_said_aba_ddfv)
    time.sleep(5)
    #Verifica se o campo Volume = 0 da aba Desc/Despesas/Frete/Div
    if pyautogui.locateOnScreen(rf"{path}\cad_vend_said_aba_ddfv_volume.png", confidence=0.9):
        #Clica no campo Volume da aba Desc/Despesas/Frete/Div
        cad_vend_said_aba_ddfv_volume = pyautogui.locateOnScreen(rf"{path}\cad_vend_said_aba_ddfv_volume.png", confidence=0.9)
        pyautogui.click(cad_vend_said_aba_ddfv_volume)
        time.sleep(5)
        #Seleciona o campo Volume = 0 e apaga
        pyautogui.press('end')
        time.sleep(2)
        pyautogui.hotkey('shiftleft','shiftright','home')
        time.sleep(1)
        pyautogui.press('backspace')
        time.sleep(2)
        #Insere 1 no campo Volume
        pyautogui.write("1")
        pyautogui.press('enter')
    else:
        time.sleep(2)
        print("O volume estava maior (>) que 1")
    #Chama o método concluirVendSaid
    time.sleep(10)
    concluirVendSaid()
    #Implementado 06/01/2022
    time.sleep(5)
    #Clica no botão X para fechar a tela que está aberta
    fechaTela()
    time.sleep(5)