import pyautogui
from time import sleep

# Caminho da pasta das imagens
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"


# Método implementado - Ruan 18/05/2022
def ediCadBanco():
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl', '1')
    sleep(10)
    btn_mnpricfinan = pyautogui.locateOnScreen(rf"{path}\mnprinc_finan.png")
    # Clica no botão Financeiro
    pyautogui.click(btn_mnpricfinan)
    sleep(2)
    btn_mnfinancontpag = pyautogui.locateOnScreen(rf"{path}\menu_finan_conta_pagar.png", confidence=0.9)
    # Clica no botão Contas a pagar
    pyautogui.click(btn_mnfinancontpag)
    sleep(10)
    # Clica no campo "Banco"
    camp_banco = pyautogui.locateOnScreen(rf"{path}\campo_banco.png", confidence=0.9)
    pyautogui.click(camp_banco)
    sleep(1)
    # Escreve 1 no campo banco
    pyautogui.write('1')
    sleep(2)
    # Da duplo clique no campo Banco
    pyautogui.doubleClick(camp_banco)
    sleep(10)
    # Verificação se o botão "Ativo" está marcado ou não
    if pyautogui.locateOnScreen(rf"{path}\btn_ativo_banco_marc.png"):
        # Verifica e printa no console caso botão esteja marcado
        btn_ativo_banco_marc = pyautogui.locateOnScreen(rf"{path}\btn_ativo_banco_marc.png")
        sleep(1)
        print("O botão Ativo esta marcado!")
        # Clica no botão Ativo para desmarcar
        pyautogui.click(btn_ativo_banco_marc)
        sleep(5)
        # Clica no lápis de salvar e printa no console avisando a alteração
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis_cad_cli_for.png", confidence=0.9)
        sleep(2)
        pyautogui.click(btn_lapis)
        print("A opção Ativo desmarcado foi salva!")
        sleep(5)
        # Fecha a tela de Tabela de Caixa/Banco
        pyautogui.hotkey('ctrl', 'F8')
        sleep(2)
        # Fecha tela de Contas a Pagar
        pyautogui.hotkey('ctrl', 'F8')

    else:
        # Verifica e printa no console caso o botão esteja desmarcado
        btn_ativo_banco_desmar = pyautogui.locateOnScreen(rf"{path}\btn_ativo_banco_desmarc.png")
        print("O botão Ativo está desmarcado!")
        sleep(2)
        # Clica no botão Ativo para marcar
        pyautogui.click(btn_ativo_banco_desmar)
        sleep(5)
        # Clica no lápis de salvar e printa no console avisando a alteração
        btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis_cad_cli_for.png", confidence=0.9)
        sleep(1)
        pyautogui.click(btn_lapis)
        print("A opção Ativo marcado foi salva!")
        sleep(5)
        # Fecha a tela de Tabela de Caixa/Banco
        pyautogui.hotkey('ctrl', 'F8')
        sleep(2)
        # Fecha tela de Contas a Pagar
        pyautogui.hotkey('ctrl', 'F8')
