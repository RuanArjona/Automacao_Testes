import pyautogui
from time import sleep

# Fernando 26/11/2021
# Caminho da pasta em uma variável

path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
global btn_lapis_cad_cli_for
btn_lapis_cad_cli_for = pyautogui.locateOnScreen(rf"{path}\btn_lapis_cad_cli_for.png", confidence=0.9)


def cadastroCliFor():
    # Menu Principal
    sleep(5)
    pyautogui.hotkey('ctrl', '1')
    sleep(15)
    # Menu Principal > Cadastro
    menu_princ_cad = pyautogui.locateOnScreen(rf"{path}\menu_cadastro.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_princ_cad)
    sleep(1)
    # Menu Principal > Cadastro > Cliente e Fornecedor
    menu_princ_cad_cli_for = pyautogui.locateOnScreen(rf"{path}\menu_cadastro_cli_for.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_princ_cad_cli_for)
    sleep(15)
    # Clica no botão ">*"
    cad_cli_for_novo = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_novo.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(cad_cli_for_novo)
    sleep(10)
    cad_cli_aba_geral = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_aba_geral.png", confidence=0.9)
    # Verifica se o cadastro do cliente está em branco
    if cad_cli_aba_geral:
        print("Janela Cadastro Cliente Fornecedor OK")
    else:
        # Se a tela estiver desconfigurada, irá ser exibido no console o print seguinte:
        print("Janela Cadastro de Cliente Fornecedor DESCONFIGURADA! Verifique o erro!")
    # Menu Principal > Cadastro > Cliente e Fornecedor > campo Grupo
    # aperta tab 5x até o campo Grupo
    pyautogui.press('tab', presses=5)
    sleep(1)
    # Coloca o grupo 002
    pyautogui.write("002")
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    # Clica no botão lápis para salvar
    pyautogui.click(btn_lapis_cad_cli_for)
    sleep(10)
    # Verifica a mensagem 'É necessário irformar um sub grupo, por favor verifique!'
    mgs_confirm_edit = pyautogui.locateOnScreen(rf"{path}\msg_necess_inf_subgrupo.png", confidence=0.9)
    sleep(0.5)
    if mgs_confirm_edit:
        sleep(0.5)
        pyautogui.press('enter')
        sleep(1)
    else:
        # Aviso que não teve mensagem
        print("Não houve mensagem de sub grupo")
    # Coloca o subgrupo 022
    sleep(0.5)
    pyautogui.write("022")
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # Clica no botão lápis para salvar
    pyautogui.click(btn_lapis_cad_cli_for)
    sleep(10)
    # Verifica mensagem de representante
    msg_n_cad_represe = pyautogui.locateOnScreen(rf"{path}\msg_cad_cli_for_nao_foi_cad_representante.png", confidence=0.9)
    sleep(0.5)
    if msg_n_cad_represe:
        sleep(1)
        # Localiza e clica no botão sim da mensagem "Não foi cadastrado um Representante para este cliente.
        # Deseja cadastra-lo?"
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_sim)
        sleep(1)
    else:
        # Aviso que não teve mensagem
        print("Não houve mensagem para cadastrar o representante!")
    # Coloca 0 no vendedor e clica enter
    pyautogui.write("0")
    sleep(1)
    pyautogui.press('enter')
    sleep(10)
    # Verifica mensagem de escolha um valor na lista
    if pyautogui.locateOnScreen(rf"{path}\msg_esc_val_list.png", confidence=0.9):
        sleep(0.5)
        pyautogui.press('enter')
        sleep(5)
    else:
        # Aviso que não teve mensagem
        print("Não houve mensagem para cadastrar o representante!")
    # Seleciona o primeiro vendedor da lista
    pyautogui.press('down')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    # Localiza e clica no botão lápis para salvar
    btn_lapis_cad_cli_for_end = pyautogui.locateOnScreen(rf"{path}\btn_lapis_cad_cli_for.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(btn_lapis_cad_cli_for_end)
