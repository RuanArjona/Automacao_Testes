from maximiza_fecha import *
from metodos_compra_entrada import *
import pyautogui
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Fernando 26/11/2021
# Caminho da pasta em uma variável
path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")


# Método implementado - Fernando 19/05/2022
def cadastroCompEntrada():
    # Selecionar a janela do Menu Principal dentro do Ouro
    time.sleep(5)
    pyautogui.hotkey('ctrl', '1')
    time.sleep(15)
    # Menu Principal > Compra / Entrada
    menu_compra_entrada = pyautogui.locateOnScreen(rf"{path}\menu_compra_entrada.png", confidence=0.9)
    pyautogui.click(menu_compra_entrada)
    time.sleep(5)
    # Menu Principal > Compra / Entrada > Compra / Entrada
    menu_comp_ent = pyautogui.locateOnScreen(rf"{path}\menu_compra_entrada_compra_entrada.png", confidence=0.9)
    pyautogui.click(menu_comp_ent)
    time.sleep(25)
    # Clica no botão para maximizar a janela
    maximizaTela()
    time.sleep(5)
    # Seleciona o campo do fornecedor
    cad_ped_comp_fornecedor = pyautogui.locateOnScreen(rf"{path}\cad_comp_entr_fornecedor.png", confidence=0.9)
    pyautogui.click(cad_ped_comp_fornecedor)
    time.sleep(5)
    # Insere um fornecedor
    # fornecedor na MILFARMA
    pyautogui.write("00000001")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)
    # Chama o método para salvar o número do Pedido Venda

    dataatual = datetime.now()
    cod = (dataatual.strftime('%H%M%d'))
    pyautogui.write(str(cod))
    pyautogui.hotkey('shiftleft', 'shiftright', 'home')

    salvaNumeroCompEnt()
    time.sleep(5)
    # Seleciona o campo Desc. do Item no Pedido de Venda
    time.sleep(10)
    pyautogui.press('tab', presses=5)
    time.sleep(1)
    pyautogui.write("7")
    time.sleep(2)
    # Seta para baixo para selecionar um produto
    pyautogui.press('tab', presses=7)
    pyautogui.press('down')
    time.sleep(2)
    # Implementado - Renan 22/12/2021
    # Verifica se tem produto disponível
    while pyautogui.locateOnScreen(rf"{path}\cad_ent_qtd_disp_zero.png"):
        time.sleep(1)
        pyautogui.press('down')
    # Encontra o produto disponível e aperta enter
    else:
        pyautogui.press('enter')
        # Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        time.sleep(5)

    # Seta para baixo para selecionar um produto
    pyautogui.press('down')
    pyautogui.press('right', presses=2)
    pyautogui.press('down', presses=2)
    time.sleep(2)
    # Implementado - Renan 22/12/2021
    # Verifica se tem produto disponível
    while pyautogui.locateOnScreen(rf"{path}\cad_ent_qtd_disp_zero.png"):
        time.sleep(1)
        pyautogui.press('down')
    # Encontra o produto disponível e aperta enter
    else:
        pyautogui.press('enter')
        # Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        time.sleep(5)

    # Chama o método concluirPedVend
    # time.sleep(5)
    # concluirPedComp()
    # time.sleep(5)
    # Clica no botão X para fechar a tela que está aberta
    # fechaTela()


cadastroCompEntrada()
