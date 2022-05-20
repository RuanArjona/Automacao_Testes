from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 08/12/2021
def pedVendBaseado():
    #Selecionar a janela do Ouro Web
    #pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #Menu Principal
    #time.sleep(5)
    #Clica no campo Baseado
    pyautogui.hotkey('ctrl','1')
    time.sleep(5)
    pyautogui.hotkey('ctrl','p')
    time.sleep(20)
    maximizaTela()
    time.sleep(10)
    #Clica no campo Baseado
    nmr_ped_vend_baseado = pyautogui.locateOnScreen(rf"{path}\nmr_ped_vend_baseado.png", confidence=0.9)
    time.sleep(10)
    pyautogui.click(nmr_ped_vend_baseado)
    time.sleep(15)
    #Maximiza o txt do número do Pedido Venda
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Campo Nº do Pedido Venda
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Nº do Pedido Venda
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Nº do Pedido Venda do txt no Histórico de Movimentos
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
    #Aperta a tecla enter para carregar o pedido venda baseado
    pyautogui.press('enter')
    time.sleep(30)
    #Chama o método concluirPedVend para concluir o Pedido Venda
    time.sleep(10)
    concluirPedVend()
    #Implementado 06/01/2022
    time.sleep(5)
    #Chama o método fechaTela para fechar a tela de Pedido Venda
    fechaTela()
