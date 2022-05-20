from maximiza_fecha import *
from metodos_compra_entrada import *
from login_ouro import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Fernando 16/05/2022
def cancelaPedComp():
    #Selecionar a janela do Ouro Web
    #pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #Menu Principal
    #time.sleep(5)
    #Chama o método insereNumeroPedComp
    time.sleep(5)
    insereNumeroPedComp()
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
    #Clica no botão Cancelar
    btn_canc_hist_mov = pyautogui.locateOnScreen(rf"{path}\btn_canc_hist_mov.png", confidence=0.9)
    pyautogui.click(btn_canc_hist_mov)
    time.sleep(10)
    #Insere usuário
    #Chama o método Login para fazer entrar com login e senha
    loginOuro()
    time.sleep(10)
    #Insere mensagem com o motivo de cancelamento de teste
    pyautogui.write("MOTIVO DE CANCELAMENTO DE TESTE")
    time.sleep(10)
    #Aperta Enter
    pyautogui.press('enter')
    time.sleep(10)
    #Verifica mensagem de cancelamento
    if  pyautogui.locateOnScreen(rf"{path}\msg_canc_hist_mov_vend_said.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('s')
    else:
        time.sleep(2)
    #Verifica mensagem de inutilização da nota na SEFAZ
    if  pyautogui.locateOnScreen(rf"{path}\msg_inu_nt_hist_mov_vend_said.png", confidence=0.9):
        time.sleep(15)
        #Código btn_ok
        btn_ok_nota_inul_hist_mov = pyautogui.locateOnScreen(rf"{path}\btn_ok_nota_inul_hist_mov.png", confidence=0.9)
        pyautogui.press(btn_ok_nota_inul_hist_mov)
    else:
        time.sleep(2)
    #Verifica mensagem de cancelamento efetuado com sucesso
    if pyautogui.locateOnScreen(rf"{path}\msg_canc_sucess_hist_mov_vend_said.png", confidence=0.9):
        time.sleep(20)
        pyautogui.press('enter')
    else:
        time.sleep(2)
    #Implementado 06/01/2022
    time.sleep(10)
    #Chama o método fechaTela para fechar a tela de Histórico de Movimentos
    fechaTela()