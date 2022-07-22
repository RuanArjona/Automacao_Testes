import pyautogui
from time import sleep


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

def cadastroCliForMensagensDinamicas():
    #Menu Principal
    sleep(5)
    pyautogui.hotkey('ctrl','1')
    sleep(15)
    #Menu Principal > Cadastro
    menu_princ_cad = pyautogui.locateOnScreen(rf"{path}\menu_cadastro.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_princ_cad)
    sleep(5)
    #Menu Principal > Cadastro > Cliente e Fornecedor
    menu_princ_cad_cli_for = pyautogui.locateOnScreen(rf"{path}\menu_cadastro_cli_for.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_princ_cad_cli_for)
    sleep(15)
    #Menu Principal > Cadastro > Cliente e Fornecedor > aba Outros
    cad_cli_for_aba_out = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_aba_out.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(cad_cli_for_aba_out)
    sleep(10)
    #Menu Principal > Cadastro > Cliente e Fornecedor > aba Outros
    cad_cli_for_aba_out_btn_mesg_dina = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_aba_out_btn_msg_dina.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(cad_cli_for_aba_out_btn_mesg_dina)
    sleep(5)

    #Renan inclusão da validação de nenhum registro encontrado 01/12/2021
    #botão Novo
    #Tela Mensagens Dinâmicas > Botão Novo  
    if pyautogui.locateOnScreen(rf"{path}\msg_nen_reg_enc.png", confidence=0.9):
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_ok)
        sleep(0.5)
        btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_novo)
        sleep(5)
    else:
        btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_novo)
        sleep(5)

    #funções

    #Inserir dados
    #Mensagem
    pyautogui.write("TESTE DE AUTOMATICO")
    sleep(0.5)
    pyautogui.press('tab')
    sleep(0.5)
    #Data de Validade
    pyautogui.write("27092022")
    sleep(0.5)
    #Tela Mensagens Dinâmicas > Botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(btn_salvar)
    sleep(0.5)
    print("Mensagem inserida com sucesso!")
    sleep(2)

    #Renan inclusão do método alterar 01/12/2021
    #Alterar dados
    if pyautogui.locateOnScreen(rf"{path}\msg_din_castrada.png", confidence=0.9):
        msg_din_castrada = pyautogui.locateOnScreen(rf"{path}\msg_din_castrada.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(msg_din_castrada)
        sleep(0.5)
        alt_msg_din = pyautogui.locateOnScreen(rf"{path}\alt_msg_din.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(alt_msg_din)
        sleep(0.5)
        pyautogui.hotkey('ctrl','a')
        sleep(0.5)
        pyautogui.write("MENSAGEM AUTOMATICA DE TESTE ALTERADA - 2")
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.write("10102022")
        sleep(0.5)
        pyautogui.click(btn_salvar)
        sleep(5)
        print("Mensagem alterada com sucesso")
    else:
        print("Não foi possível alterar a mensagem. Verifique a mensagem cadastrada e tente novamente.")

    #Renan inclusão do método selecionar 01/12/2021
    #Selecionar mensagem
    msg_din_alterada = pyautogui.locateOnScreen(rf"{path}\msg_din_alterada.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(msg_din_alterada)
    sleep(5)

    #Renan inclusão do método excluir 01/12/2021
    #Excluir dados
    if pyautogui.locateOnScreen(rf"{path}\msg_din_alterada.png", confidence=0.9):
        btn_excluir = pyautogui.locateOnScreen(rf"{path}\btn_excluir.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_excluir)
        sleep(5)
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_sim)
        print("Mensagem excluída com sucesso!")
    else:
        print("Não foi possível excluir a mensagem. Verifique o Erro e tente novamente.")
