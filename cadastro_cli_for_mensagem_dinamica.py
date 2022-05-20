import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

def cadastroCliForMensagensDinamicas():
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
    #Menu Principal > Cadastro > Cliente e Fornecedor > aba Outros
    cad_cli_for_aba_out = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_aba_out.png", confidence=0.9)
    pyautogui.click(cad_cli_for_aba_out)
    time.sleep(10)
    #Menu Principal > Cadastro > Cliente e Fornecedor > aba Outros
    cad_cli_for_aba_out_btn_mesg_dina = pyautogui.locateOnScreen(rf"{path}\cad_cli_for_aba_out_btn_msg_dina.png", confidence=0.9)
    pyautogui.click(cad_cli_for_aba_out_btn_mesg_dina)
    time.sleep(5)

    #Renan inclusão da validação de nenhum registro encontrado 01/12/2021
    #botão Novo
    #Tela Mensagens Dinâmicas > Botão Novo  
    if pyautogui.locateOnScreen(rf"{path}\msg_nen_reg_enc.png", confidence=0.9):
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        pyautogui.click(btn_ok)
        btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
        pyautogui.click(btn_novo)
        time.sleep(5)
    else:
        btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
        pyautogui.click(btn_novo)
        time.sleep(5)

    #funções

    #Inserir dados
    #Mensagem
    pyautogui.write("TESTE DE AUTOMATICO RENAN 2")
    pyautogui.press('tab')
    #Data de Validade
    pyautogui.write("27032022")
    #Tela Mensagens Dinâmicas > Botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    pyautogui.click(btn_salvar)
    print("Mensagem inserida com sucesso!")
    time.sleep(2)

    #Renan inclusão do método alterar 01/12/2021
    #Alterar dados
    if pyautogui.locateOnScreen(rf"{path}\msg_din_castrada.png", confidence=0.9):
        msg_din_castrada = pyautogui.locateOnScreen(rf"{path}\msg_din_castrada.png", confidence=0.9)
        pyautogui.click(msg_din_castrada)
        alt_msg_din = pyautogui.locateOnScreen(rf"{path}\alt_msg_din.png", confidence=0.9)
        pyautogui.click(alt_msg_din)
        pyautogui.hotkey('ctrl','a')
        pyautogui.write("MENSAGEM AUTOMATICA DE TESTE ALTERADA - 2")
        pyautogui.press('tab')
        pyautogui.write("10102022")
        pyautogui.click(btn_salvar)
        time.sleep(5)
        print("Mensagem alterada com sucesso")
    else:
        print("Não foi possível alterar a mensagem. Verifique a mensagem cadastrada e tente novamente.")

    #Renan inclusão do método selecionar 01/12/2021
    #Selecionar mensagem
    pyautogui.locateOnScreen(rf"{path}\msg_din_alterada.png", confidence=0.9)
    msg_din_alterada = pyautogui.locateOnScreen(rf"{path}\msg_din_alterada.png", confidence=0.9)
    pyautogui.click(msg_din_alterada)
    time.sleep(5)

    #Renan inclusão do método excluir 01/12/2021
    #Excluir dados
    if pyautogui.locateOnScreen(rf"{path}\msg_din_alterada.png", confidence=0.9):
        btn_excluir = pyautogui.locateOnScreen(rf"{path}\btn_excluir.png", confidence=0.9)
        pyautogui.click(btn_excluir)
        time.sleep(5)
        atencao_excl_msg_din_cad = pyautogui.locateOnScreen(rf"{path}\atencao_excl_msg_din_cad.png", confidence=0.9)
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.click(btn_sim)
        print("Mensagem excluída com sucesso!")
    else:
        print("Não foi possível excluir a mensagem. Verifique o Erro e tente novamente.")