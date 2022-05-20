from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 08/12/2021
def editaPedVendSimp():
    #Selecionar a janela do Ouro Web
    #pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #Menu Principal
    #time.sleep(5)
    #Chama o método insereNumeroPedVend
    time.sleep(15)
    insereNumeroPedVendSimp()
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
    time.sleep(25)
    maximizaTela()
    time.sleep(10)
    #Teste realizado na Milfarma
    #Aperta TAB  13 vezes para chegar no campo Qtde
    pyautogui.press('tab', presses=13)
    time.sleep(10)
    #Altera a quantidade para 10
    pyautogui.write("10")
    time.sleep(5)
    #Salva o produto clicando no lápis
    btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
    pyautogui.click(btn_lapis)
    time.sleep(20)
    #Concluir o Pedido Venda simples
    #Implementado - Renan 10/12/2021
    #Mensagem de rentabilidade
    if pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9):
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(5)
        pyautogui.press('o')
        #pyautogui.click(btn_ok)
        time.sleep(5)
        #Clica no botão Concluir
        btn_concluir_ped_venda_simples = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_venda_simples.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_venda_simples)
    else:
        #Clica no botão Concluir
        time.sleep(5)
        btn_concluir_ped_venda_simples = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_venda_simples.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_venda_simples)
        #Mensagem de rentabilidade
        time.sleep(5)
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(5)
        pyautogui.press('o')
        #pyautogui.click(btn_ok)
        

    #Espera 15s    
    time.sleep(15)

    #Implementado - Renan 10/12/2021
    #Verifica mensagem de conclusão de movimento
    if pyautogui.locateOnScreen(rf"{path}\msg_conf_movi.png", confidence=0.9):
        time.sleep(15)
    #Clica no botão sim para concluir o movimento
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.press('s')
        #pyautogui.click(btn_sim)
        time.sleep(5)
        print("Clicou no botão 'sim' para concluir o movimento")
        time.sleep(25)
    #Clica para não imprimir o movimento    
        btn_nao_imp_mov = pyautogui.locateOnScreen(rf"{path}\btn_nao_imp_mov.png", confidence=0.9)
        pyautogui.press('n')
        #pyautogui.click(btn_nao_imp_mov)
        time.sleep(5)
        print("Clicou no botão 'não' para não imprimir o documento")
    else:
        print("Não teve mensagem de confirmação do movimento, verifique o erro!")
  
    #Implementado 06/01/2022
    #Clica no botão X para fechar a tela que está aberta
    time.sleep(20)
    fechaTela()
    #Chama o método fechaTela para fechar a tela de Histórico de Movimentos
    time.sleep(20)
    fechaTela()