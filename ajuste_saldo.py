import pyautogui
import time
from maximiza_fecha import *


#Fernando 26/11/2021
#Caminho da pasta em uma variável
path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")
path_print = (rf"C:\Teste Automatizado OuroWeb\bin\project\tests\img\print_img_erro")
#Método implementado - Renan 31/01/2022

    #Implementado - Renan 08/04/2022
def ajusteSaldoEntrada():
    #Aperta ctrl+1 para abrir o Menu Principal
    pyautogui.hotkey('ctrl','1')    
    time.sleep(5)
    #Acessa o Menu Principal > Controle Estoque
    menu_controle_estoque = pyautogui.locateOnScreen(rf"{path}\menu_controle_estoque.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(menu_controle_estoque)
    time.sleep(5)
    #Acessa o Menu Principal > Controle Estoque > Ajuste de Saldo
    menu_controle_estoque_ajuste_saldo = pyautogui.locateOnScreen(rf"{path}\menu_controle_estoque_ajuste_saldo.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(menu_controle_estoque_ajuste_saldo)
    time.sleep(20)
    #Chama o método para maximizar a janela
    maximizaTela()
    time.sleep(10)
    #Clica no Tipo Movimento = Entrada
    ajuste_estoque_tip_mov_entrada = pyautogui.locateOnScreen(rf"{path}\ajuste_estoque_tip_mov_entrada.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(ajuste_estoque_tip_mov_entrada)
    time.sleep(5)
    pyautogui.press('tab', presses=12)
    #Insere o código 0 e aperta a tecla enter
    time.sleep(5)
    pyautogui.write("0")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(15)

    #Verifica se houve mensagem de Escolha um valor na lista
    if pyautogui.locateOnScreen(rf"{path}\msg_esc_val_list.png", confidence=0.9):
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
    else:
        #Caso não tenha mensade de Escolha um valor na lista, tira o print
        screenshot_msg_esc_val_list_nao_encontrada = pyautogui.screenshot(rf"{path_print}\screenshot_msg_esc_val_list_nao_encontrada.png")
        print("Mensagem 'Escolha um valor na lista' não encontrada, Verifique o erro no print")
    time.sleep(20)
    #Aperta seta pra baixo e enter para selecionar o primeiro produto
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    #Aperta seta pro lado para chegar no campo Qtde
    pyautogui.press('rigth')
    time.sleep(2)
    #Coloca no campo Qtde. como 100
    pyautogui.write("100")
    time.sleep(10)
    #Clica no Lapis para salvar
    btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
    pyautogui.click(btn_lapis)
    time.sleep(10)
    #Clica no botão conlcuir
    btn_concluir_ajuste_estoque = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ajuste_estoque.png", confidence=0.9)
    pyautogui.click(btn_concluir_ajuste_estoque)
    time.sleep(10)
    #Verifica se houve mensagem de Confirmar o Movimento
    if pyautogui.locateOnScreen(rf"{path}\msg_conf_mov_ajuste_estoque.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('s')
    else:
        #Caso não tenha mensade de Confirmar o Movimento, tira o print
        screenshot_msg_conf_mov_ajuste_estoque_nao_encontrada = pyautogui.screenshot(rf"{path_print}\screenshot_msg_conf_mov_ajuste_estoque_nao_encontrada.png")
        print("Mensagem 'Confirma o movimento' não encontrada, Verifique o erro no print")
    time.sleep(20)
    #Verifica se houve mensagem de Deseja imprimir documento
    if pyautogui.locateOnScreen(rf"{path}\msg_desej_imp_doc.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('n')
    else:
        #Caso não tenha mensade de Deseja imprimir documento, tira o print
        screenshot_msg_desej_imp_doc_nao_encontrada = pyautogui.screenshot(rf"{path_print}\screenshot_msg_desej_imp_doc_nao_encontrada.png")
        print("Mensagem 'Deseja imprimir documento', Verifique o erro no print")
    time.sleep(20)
    #Chama o método para fechar a tela
    fechaTela()
    
    #Implementado 11/04/2022
def ajusteSaldoSaida():
    #Aperta ctrl+1 para abrir o Menu Principal
    pyautogui.hotkey('ctrl','1')    
    time.sleep(5)
    #Acessa o Menu Principal > Controle Estoque
    menu_controle_estoque = pyautogui.locateOnScreen(rf"{path}\menu_controle_estoque.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(menu_controle_estoque)
    time.sleep(5)
    #Acessa o Menu Principal > Controle Estoque > Ajuste de Saldo
    menu_controle_estoque_ajuste_saldo = pyautogui.locateOnScreen(rf"{path}\menu_controle_estoque_ajuste_saldo.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(menu_controle_estoque_ajuste_saldo)
    time.sleep(20)
    #Chama o método para maximizar a janela
    maximizaTela()
    time.sleep(10)
    #Clica no Tipo Movimento = Saida
    ajuste_estoque_tip_mov_saida = pyautogui.locateOnScreen(rf"{path}\ajuste_estoque_tip_mov_saida.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(ajuste_estoque_tip_mov_saida)
    time.sleep(5)
    pyautogui.press('tab', presses=13)
    #Insere o código 0 e aperta a tecla enter
    time.sleep(5)
    pyautogui.write("0")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(15)

    #Verifica se houve mensagem de Escolha um valor na lista
    if pyautogui.locateOnScreen(rf"{path}\msg_esc_val_list.png", confidence=0.9):
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
    else:
        #Caso não tenha mensade de Escolha um valor na lista, tira o print
        screenshot_msg_esc_val_list_nao_encontrada = pyautogui.screenshot(rf"{path_print}\screenshot_msg_esc_val_list_nao_encontrada.png")
        print("Mensagem 'Escolha um valor na lista' não encontrada, Verifique o erro no print")
    time.sleep(20)
    #Aperta seta pra baixo e enter para selecionar o primeiro produto
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    #Aperta seta pro lado para chegar no campo Qtde
    pyautogui.press('rigth')
    time.sleep(2)
    #Coloca no campo Qtde. como 10
    pyautogui.write("10")
    time.sleep(10)
    #Clica no Lapis para salvar
    btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
    pyautogui.click(btn_lapis)
    time.sleep(10)
    #Clica no botão conlcuir
    btn_concluir_ajuste_estoque = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ajuste_estoque.png", confidence=0.9)
    pyautogui.click(btn_concluir_ajuste_estoque)
    time.sleep(10)
    #Verifica se houve mensagem de Confirmar o Movimento
    if pyautogui.locateOnScreen(rf"{path}\msg_conf_mov_ajuste_estoque.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('s')
    else:
        #Caso não tenha mensade de Confirmar o Movimento, tira o print
        screenshot_msg_conf_mov_ajuste_estoque_nao_encontrada = pyautogui.screenshot(rf"{path_print}\screenshot_msg_conf_mov_ajuste_estoque_nao_encontrada.png")
        print("Mensagem 'Confirma o movimento' não encontrada, Verifique o erro no print")
    time.sleep(20)
    #Verifica se houve mensagem de Deseja imprimir documento
    if pyautogui.locateOnScreen(rf"{path}\msg_desej_imp_doc.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('n')
    else:
        #Caso não tenha mensade de Deseja imprimir documento, tira o print
        screenshot_msg_desej_imp_doc_nao_encontrada = pyautogui.screenshot(rf"{path_print}\screenshot_msg_desej_imp_doc_nao_encontrada.png")
        print("Mensagem 'Deseja imprimir documento', Verifique o erro no print")
    time.sleep(20)
    #Chama o método para fechar a tela
    fechaTela()