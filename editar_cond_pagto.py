from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
from time import sleep

# Caminho da pasta das imagens
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"


# Método implementado - Ruan 17/05/2022
def cadastroPedVenda():
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl', '1')
    time.sleep(15)
    # Atalho >> Venda / Saída > Pedido de Venda
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(20)
    # Clica no botão para maximizar a janela
    maximizaTela()
    time.sleep(5)
    # Seleciona o campo do cliente
    cad_ped_vend_cliente = pyautogui.locateOnScreen(rf"{path}\cad_ped_vend_cliente.png", confidence=0.9)
    # Clica no campo do cliente
    pyautogui.click(cad_ped_vend_cliente)
    time.sleep(5)
    # Seleciona um cliente no campo "Cliente"
    pyautogui.write("00000002")
    time.sleep(10)
    # Clica no cliente
    pyautogui.press('enter')
    time.sleep(15)
    # Tab até chegar "Cond. Pagto"
    pyautogui.press('tab', presses=9)
    sleep(3)
    # Escreve "7"
    pyautogui.write("7")
    sleep(3)
    # Pressiona enter
    pyautogui.press("enter")
    sleep(10)
    # Volta ao textbox "Cond. Pagto"
    campo_cond_pagto_7 = pyautogui.locateOnScreen(rf"{path}\campo_cond_pagto_7.png")
    pyautogui.doubleClick(campo_cond_pagto_7)
    sleep(10)
    # Clica em onde o ponteiro do mouse está fixado
    pyautogui.click()
    # Pressiona Tab 3x
    pyautogui.press('tab', presses=3)
    sleep(15)
    # Escreve "Teste" no campo "Descrição"
    pyautogui.write("Teste")
    sleep(10)
    # Localiza a imagem do botão "Filtrar"
    btn_filtrar = pyautogui.locateOnScreen(rf"{path}\btn_filtrar.png")
    # Clica no botão "Filtrar"
    pyautogui.click(btn_filtrar)
    sleep(10)
    # Localiza a imagem do botão "Salvar"
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    sleep(1)
    # Condição para verificar se CheckBox "Ativo" está marcado ou não
    if pyautogui.locateOnScreen(rf"{path}\btn_ativo_checked.png"):
        # Localiza a imagem do botão "Ativo marcado"
        btn_ativo_on = pyautogui.locateOnScreen(rf"{path}\btn_ativo_checked.png")
        print("Verificado que o botão *Ativo* está marcado!")
        # Clica no CheckBox que está ativo para desmarcar
        sleep(5)
        pyautogui.click(btn_ativo_on)
        sleep(5)
        print("O botão *Ativo* foi editado e agora está desmarcado!")
        sleep(2)
        # Clica no botão "Salvar"
        pyautogui.click(btn_salvar)
    else:
        # Localiza a imagem do botão "Ativo desmarcado"
        btn_ativo_off = pyautogui.locateOnScreen(rf"{path}\btn_ativo_clean.png")
        print("Verificado que o botão *Ativo* está desmarcado!")
        sleep(5)
        # Clica no CheckBox que está ativo para marcar
        pyautogui.click(btn_ativo_off)
        sleep(5)
        print("O botão *Ativo* foi editado e agora está marcado!")
        sleep(2)
        # Clica no botão "Salvar"
        pyautogui.click(btn_salvar)

    sleep(10)
    # Localiza e fecha a janela "Tabela de Condições de Pagamento"
    pyautogui.getWindowsWithTitle("Tabela de Condições de Pagamento")[0].close()
    sleep(5)
    # Método para fechar as janelas
    fechaTela()
