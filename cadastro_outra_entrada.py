from time import sleep
import pyautogui
from maximiza_fecha import *
from metodos_compra_entrada import *

# Caminho da pasta das imagens
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
path2 = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\doc"

# Implementado - Ruan 24/05/2022
def criarOutraEntrada():
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl', '1')
    sleep(10)
    # Localiza e clica no botão "Compra/Entrada"
    menu_camp_entr = pyautogui.locateOnScreen(rf"{path}\menu_compra_entrada.png")
    pyautogui.click(menu_camp_entr)
    sleep(1)
    # Localiza e clica no botão "Compra/Entrada > Outras entradas"
    btn_outras_entr = pyautogui.locateOnScreen(rf"{path}\menu_btn_outras_entradas.png")
    pyautogui.click(btn_outras_entr)
    sleep(30)
    # Localiza e clica no campo "Código"
    camp_cod = pyautogui.locateOnScreen(rf"{path}\campo_codigo.png")
    pyautogui.click(camp_cod)
    sleep(2)
    # Escreve no campo "00000002" para selecionar o fornecedor e logo pressiona a tecla "Enter"
    pyautogui.write("00000002")
    sleep(2)
    pyautogui.press("enter")
    sleep(25)
    # Localiza e clica no campo "Desc. Item"
    pyautogui.press('tab', presses=19)
    sleep(3)
    # Pressiona a seta para baixo
    pyautogui.press('down')
    sleep(2)
    # Looping para verificar quantidade de produtos
    while pyautogui.locateOnScreen(rf"{path}\cad_ent_qtd_disp_zero.png"):
        sleep(1)
        # Pressiona a seta para baixo
        pyautogui.press('down')
    # Encontra o produto disponível e aperta enter
    else:
        pyautogui.press('enter')
        # Salva o produto clicando no lápis
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
        pyautogui.click(btn_lapis)
        sleep(5)
        # Localiza e clica no campo "Busca Dinâm. Desc.:"
        camp_busc_dinam_descri = pyautogui.locateOnScreen(rf"{path}\campo_busc_dinam_descri.png")
        pyautogui.click(camp_busc_dinam_descri)
        sleep(2)
        # Local onde onde arquivo DESCRICAO-PRODUTO.txt está salvo
        with open(rf"{path2}\DESCRICAO-PRODUTO.txt", 'r', encoding="utf8") as ler_str:
            # Ler todas as linhas do arquivo uma a uma
            line = ler_str.read()
            sleep(5)
            # Escreve no campo e pressiona a tecla "Enter"
            pyautogui.write(line)
            sleep(2)
            pyautogui.press("enter")
            sleep(10)
            # Localiza e clica no botão checkbox para salvar
            pyautogui.press('tab')
            sleep(1)
            pyautogui.press('space')
            sleep(2)
            # Localiza e clica no botão "OK"
            pyautogui.press("enter", presses=3)
            sleep(8)
            # Metodo para maximizar a janela
            maximizaTela()
            sleep(2)
            # Metodo para finalizar pedido
            concluirPedComp()
            sleep(5)
            # Metodo para fechar janela
            fechaTela()
