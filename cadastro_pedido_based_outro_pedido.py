from time import sleep
from maximiza_fecha import *
import pyautogui

# Caminho da pasta das imagens e documentos
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
path2 = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\doc"


# Implementado - Ruan 19/05/2022
def criarPedBasedPed():
    # Botão para ir ao menu
    pyautogui.hotkey('ctrl', '1')
    sleep(10)
    # Localiza e clica no botão "Compra/Entrada"
    menu_camp_entr = pyautogui.locateOnScreen(rf"{path}\menu_compra_entrada.png")
    pyautogui.click(menu_camp_entr)
    sleep(1)
    # Localiza e clica no botão "Pedido/Entrada"
    menu_camp_entr_ped_entr = pyautogui.locateOnScreen(rf"{path}\menu_comp_ent_ped_ent.png")
    pyautogui.click(menu_camp_entr_ped_entr)
    sleep(40)
    # Utiliza o metodo de maximizar tela da Ouro
    maximizaTela()
    sleep(5)
    # Localiza e seleciona o campo "Baseado em:"
    camp_baseadoem = pyautogui.locateOnScreen(rf"{path}\campo_baseado_em.png")
    pyautogui.click(camp_baseadoem)
    sleep(5)
    with open(rf"{path2}\NUMERO-PEDIDO-COMPRA.txt", 'r', encoding="utf8") as ler_str:
        # Ler todas as linhas do arquivo uma a uma
        line = ler_str.read()
        sleep(5)
        # Escreve no campo e pressiona a tecla "Enter"
        pyautogui.write(line)
        sleep(3)
        pyautogui.doubleClick()
        # pressiona o botão "enter"
        pyautogui.press("enter")
        sleep(20)
        # Localiza e clica no botão "Concluir"
        btn_concluir = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_compra.png")
        pyautogui.click(btn_concluir)
        sleep(10)
        # Localiza e clica no botão "Sim" da mensagem exibida na tela
        btn_yes = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.click(btn_yes)
        sleep(4)
        # Localiza e clica no botão "Não" da mensagem exibida na tela
        btn_no = pyautogui.locateOnScreen(rf"{path}\btn_nao_imp_mov.png")
        pyautogui.click(btn_no)
        '''sleep(4)
        fechaTela()
        sleep(3)
        pyautogui.click()'''
