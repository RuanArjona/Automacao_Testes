from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 08/12/2021
def editaPedVend():
    #Selecionar a janela do Ouro Web
    #pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #Menu Principal
    #time.sleep(5)
    #Chama o método insereNumeroPedVend
    time.sleep(15)
    insereNumeroPedVend()
    time.sleep(5)
    #Chama o método filtroHistMov
    filtroHistMov()
    time.sleep(15)
    #Verifica a mensagem do intervalo da data maior que 6 meses
    if pyautogui.locateOnScreen(rf"{path}\msg_interv_maior_6meses.png", confidence=0.9):
        time.sleep(10)
        #Aperta a tecla S para confirmar a mensagem = botão (SIM)
        pyautogui.press('s')
    else:
        print("Não teve mensagem de intervalo maior que 6 meses")
    #Espera 10 segundos
    time.sleep(10)
    #Clica para editar o orçamento depois de fazer o filtro
    btn_editar_hist_mov = pyautogui.locateOnScreen(rf"{path}\btn_editar_hist_mov.png", confidence=0.9)
    pyautogui.click(btn_editar_hist_mov)
    #Chama o método para maximizar a tela
    time.sleep(20)
    maximizaTela()
    time.sleep(10)
    #Teste realizado na Milfarma
    #Aperta TAB  8 vezes para chegar no campo Qtde
    pyautogui.press('tab', presses=8)
    time.sleep(10)
    #Altera a quantidade para 10
    pyautogui.write("10")
    time.sleep(5)
    #Salva o produto clicando no lápis
    btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
    pyautogui.click(btn_lapis)
    time.sleep(20)
    #Chama o método concluirPedVend para concluir o Pedido Venda
    concluirPedVend()
    #Implementado 06/01/2022
    time.sleep(5)
    #Chama o método fechaTela para fechar a tela de orçamento
    fechaTela()
    time.sleep(5)
    #Chama o método fechaTela para fechar a tela de Histórico de Movimentos
    fechaTela()