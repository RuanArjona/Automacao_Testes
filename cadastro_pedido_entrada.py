from maximiza_fecha import *
from metodos_compra_entrada import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável
path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Fernando 18/05/2022
def cadastroPedEntrada():
    #Selecionar a janela do Menu Principal dentro do Ouro
    time.sleep(5)
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Menu Principal > Compra / Entrada
    menu_compra_entrada = pyautogui.locateOnScreen(rf"{path}\menu_compra_entrada.png", confidence=0.9)
    pyautogui.click(menu_compra_entrada)
    time.sleep(5)
    #Menu Principal > Compra / Entrada > Pedido de Entrada
    menu_comp_ent_ped_ent = pyautogui.locateOnScreen(rf"{path}\menu_comp_ent_ped_ent.png", confidence=0.9)
    pyautogui.click(menu_comp_ent_ped_ent)
    time.sleep(25)
    #Clica no botão para maximizar a janela
    maximizaTela()
    time.sleep(5)
    #Seleciona o campo do fornecedor
    cad_ped_comp_fornecedor = pyautogui.locateOnScreen(rf"{path}\cad_comp_entr_fornecedor.png", confidence=0.9)
    pyautogui.click(cad_ped_comp_fornecedor)
    time.sleep(5)
    #Insere um fornecedor
    #fornecedor na MILFARMA
    pyautogui.write("00000001")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)
    #Chama o método para salvar o número do Pedido Entrada
    salvaNumeroPedComp()
    time.sleep(5)
    #Seleciona o campo Cond. Pagto no Pedido de Entrada
    time.sleep(10)
    pyautogui.press('tab',presses=4)
    time.sleep(1)
    pyautogui.write("7")
    time.sleep(2)
    #Seta para baixo para selecionar um produto
    pyautogui.press('tab',presses=10)
    pyautogui.press('down')
    time.sleep(2)
    #Implementado - Fernando 22/12/2021
    #Verifica se tem produto disponível
    while pyautogui.locateOnScreen(rf"{path}\cad_ent_qtd_disp_zero.png"):
        time.sleep(1)
        pyautogui.press('down')
    #Encontra o produto disponível e aperta enter    
    else:
        pyautogui.press('enter')
        #Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        time.sleep(5)
          
    #Chama o método concluirPedComp
    time.sleep(5)
    concluirPedComp()
    time.sleep(5)
    #Clica no botão X para fechar a tela que está aberta
    fechaTela()
