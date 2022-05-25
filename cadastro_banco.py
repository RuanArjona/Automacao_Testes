from time import sleep
from maximiza_fecha import *
import pyautogui

# Definindo caminho raiz das imagens e localizando botão "OK" nas imagens
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)


# Implementado - Ruan 19/05/2022
def cadBanco():
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl', '1')
    sleep(10)
    # Localiza e clica no menu tabelas
    menu_tabelas = pyautogui.locateOnScreen(rf"{path}\menu_tabelas.png")
    pyautogui.click(menu_tabelas)
    sleep(1)
    # Localiza e clica no botão "Tabela > Financeiro"
    menu_tab_finan = pyautogui.locateOnScreen(rf"{path}\menu_tab_financeiro.png")
    pyautogui.click(menu_tab_finan)
    sleep(1)
    # Localiza e clica no botão "Tabela > Financeiro > Tabela de Caixa/Banco"
    menu_tab_caix_banc = pyautogui.locateOnScreen(rf"{path}\menu_tabela_caixa_banco.png")
    pyautogui.click(menu_tab_caix_banc)
    sleep(1)
    # Localiza e clica no botão ">*" vulgo item novo p/ cadastro
    cad_cli_for_novo = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_novo.png")
    pyautogui.click(cad_cli_for_novo)
    sleep(5)
    pyautogui.write("TESTE")
    # Clica no lápis de salvar e printa no console avisando a alteração
    btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis_cad_cli_for.png", confidence=0.9)
    sleep(2)
    # Clica no botão lápis para salvar alterações
    pyautogui.click(btn_lapis)
    sleep(2)
    # Verifica se mensagem "selecione a empresa" aparece ou não
    if pyautogui.locateOnScreen(rf"{path}\msg_select_empresa.png", confidence=0.9):
        sleep(2)
        print("Mensagem exibida!")
        # Localiza e clica no botão "Ok"
        sleep(2)
        pyautogui.click(btn_ok)
        sleep(2)
    else:
        print("menssagem não foi exibida corretamente!")
        sleep(5)
    # Escreve "todas" no campo empresas
    pyautogui.write("todas")
    sleep(2)
    # Clica no botão lápis para salvar alterações
    pyautogui.click(btn_lapis)
    sleep(5)
    # verifica se mensagem "este codigo ja está cadastrado" existe ou não
    if pyautogui.locateOnScreen(rf"{path}\msg_cod_ja_cad.png", confidence=0.9):
        print("Cadastro já realizado anteriormente!")
        sleep(1)
        # Clica no botão "OK"
        pyautogui.click(btn_ok)
        sleep(3)
        # Fecha tela nomeada de "Tabela de Caixa/Banco"
        fechaTela()
    else:
        print("Empresa salva!")
        sleep(3)
        # Fecha tela nomeada de "Tabela de Caixa/Banco"
        fechaTela()


def excluiBanco():
    print("Empresa salva!")
    pyautogui.hotkey("Shift", "Del")
    sleep(2)
    btn_yes = pyautogui.locateOnScreen(rf"{path}\btn_yes_del_cad_caixa.png")
    sleep(3)
    pyautogui.click(btn_yes)
    sleep(3)
    fechaTela()

