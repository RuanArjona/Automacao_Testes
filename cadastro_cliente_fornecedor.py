import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")
global btn_lapis_cad_cli_for
btn_lapis_cad_cli_for = pyautogui.locateOnScreen(rf"{path}\btn_lapis_cad_cli_for.png", confidence=0.9)

def cadastroCliFor():
    #Menu Principal
    time.sleep(5)
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Menu Principal > Cadastro
    menu_princ_cad = pyautogui.locateOnScreen(rf"{path}\menu_cadastro.png", confidence=0.9)
    pyautogui.click(menu_princ_cad)
    time.sleep(5)
    #Menu Principal > Cadastro > Cliente e Fornecedor
    menu_princ_cad_cli_for = pyautogui.locateOnScreen(rf"{path}\menu_cadastro_cli_for.png", confidence=0.9)
    pyautogui.click(menu_princ_cad_cli_for)
    time.sleep(15)
    #Menu Principal > Cadastro > Cliente e Fornecedor > botão >* 
    cad_cli_for_novo = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_novo.png", confidence=0.9)
    pyautogui.click(cad_cli_for_novo)
    time.sleep(20)
    #Verifica se o cadastro do cliente está em branco
    if pyautogui.locateOnScreen(rf"{path}\cad_cli_for_aba_geral.png", confidence=0.9):
        print("Janela Cadastro Cliente Fornecedor OK")
    else:
        #Se a tela estiver desconfigurada, da um print e salva no diretório path_print
        screenshot_cad_cli_for_aba_geral = pyautogui.screenshot(rf"{path_print}\screenshot_cad_cli_for_aba_geral.png")
        print("Janela Cadastro de Cliente Fornecedor DESCONFIGURADA! Veja o print da imagem")
    
    #Menu Principal > Cadastro > Cliente e Fornecedor > campo Grupo
    #aperta tab 5x até o campo Grupo
    pyautogui.press('tab', presses=5)
    time.sleep(2)
    #Coloca o grupo 002
    pyautogui.write("002")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    #Clica no botão lápis para salvar
    pyautogui.click(btn_lapis_cad_cli_for)
    time.sleep(10)
    #Verifica a mensagem 'É necessário irformar um sub grupo, por favor verifique!'
    if pyautogui.locateOnScreen(rf"{path}\msg_necess_inf_subgrupo.png", confidence=0.9):
        time.sleep(5)
        #btn_ok_cad_prod_busc = pyautogui.locateOnScreen(rf"{path}\btn_ok_cad_prod_busc.png", confidence=0.9)
        #time.sleep(5)
        #pyautogui.click(btn_ok_cad_prod_busc)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        #Aviso que não teve mensagem
        print("Não houve mensagem de sub grupo")
    #Coloca o subgrupo 022
    time.sleep(5)
    pyautogui.write("022")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    #Clica no botão lápis para salvar
    pyautogui.click(btn_lapis_cad_cli_for)
    time.sleep(10)
    #Verifica mensagem de representante
    if pyautogui.locateOnScreen(rf"{path}\msg_cad_cli_for_nao_foi_cad_representante.png", confidence=0.9):
        time.sleep(5)
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.click(btn_sim)
        time.sleep(5)
    else:
        #Aviso que não teve mensagem
        print("Não houve mensagem para cadastrar o representante!")
    #Coloca 0 no vendedor e clica enter
    pyautogui.write("0")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    #Verifica mensagem de escolha um valor na lista
    if pyautogui.locateOnScreen(rf"{path}\msg_esc_val_list.png", confidence=0.9):
        time.sleep(5)
        #btn_ok_cad_prod_busc = pyautogui.locateOnScreen(rf"{path}\btn_ok_cad_prod_busc.png", confidence=0.9)
        #pyautogui.click(btn_ok_cad_prod_busc)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        #Aviso que não teve mensagem
        print("Não houve mensagem para cadastrar o representante!")
    #Seleciona o primeiro vendedor da lista
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    #Clica no botão lápis para salvar
    pyautogui.moveTo(btn_lapis_cad_cli_for)
    time.sleep(5)
    pyautogui.click(btn_lapis_cad_cli_for)
    time.sleep(10)
    #fecha a tela de Cadastro de Cliente Fornecedor
    #pyautogui.hotkey('ctrl','f8')