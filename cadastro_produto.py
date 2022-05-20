import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")
path_print = (rf"C:\Teste Automatizado OuroWeb\bin\project\tests\img\print_img_erro")
#Método implementado - Renan 06/12/2021
def cadastroProd():
    
    #Selecionar a janela do Ouro Web
    #pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #Menu Principal
    #time.sleep(5)
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Menu Principal > Cadastro
    menu_princ_cad = pyautogui.locateOnScreen(rf"{path}\menu_cadastro.png", confidence=0.9)
    pyautogui.click(menu_princ_cad)
    time.sleep(10)
    #Menu Principal > Cadastro > Produto
    menu_cadastro_prod = pyautogui.locateOnScreen(rf"{path}\menu_cadastro_prod.png", confidence=0.9)
    pyautogui.click(menu_cadastro_prod)
    time.sleep(25)
    #Verifica quando clicar em Cadastro > Produtos irá abrir na aba filtro os campos corretos
    # cad_prod_aba_filtro
    if pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_filtro.png", confidence=0.9):
        print("Janela Cadastro de Produto > Aba Filtro (MAXIMIZADA) OK")
    else:
        #Se a tela estiver desconfigurada, da um print e salva no diretório path_print
        screenshot_cad_prod_aba_filtro = pyautogui.screenshot(rf"{path_print}\screenshot_cad_prod_aba_filtro.png")
        print("Janela Cadastro de Produto > Aba Filtro (MAXIMIZADA) DESCONFIGURADA! Veja o print da imagem")
    #Restaura a aba filtro do Cadastro do Produto
    time.sleep(15)
    pyautogui.getWindowsWithTitle("Cadastro de Produto")[0].restore()
    #Verifica a aba filtro > Cadastro do Produto após estar reataurada
    time.sleep(10)
    if pyautogui.locateOnScreen(rf"{path}\cad_prod_abafiltro_rest.png", confidence=0.9):
        print("Janela Cadastro de Produto > Aba Filtro (RESTAURAR) OK")
        time.sleep(5)
        #Maximiza a janela do Cadastro de Produto novamente
        pyautogui.getWindowsWithTitle("Cadastro de Produto")[0].maximize()
    else:
        #Se a tela estiver desconfigurada, da um print e salva no diretório path_print
        screenshot_cad_prod_aba_filtro_rest = pyautogui.screenshot(rf"{path_print}\screenshot_cad_prod_aba_filtro_rest.png")
        print("Janela Cadastro de Produto > aba Filtro (RESTAURAR) DESCONFIGURADA! Veja o print da imagem")
        pyautogui.getWindowsWithTitle("Cadastro de Produto")[0].maximize()
    #Chama a tela Cadastro de Produto para frente e maximiza
    #pyautogui.getWindowsWithTitle("Cadastro de Produto")[0].maximize()
    time.sleep(10)
    #Botão novo
    btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
    pyautogui.click(btn_novo)
    time.sleep(10)

    #cad_prod_novo_limpo
    if pyautogui.locateOnScreen(rf"{path}\cad_prod_novo_limpo.png", confidence=0.9):
        print("Janela Cadastro de Produto > btn (NOVO) OK")
        time.sleep(5)        
    else:
        #Se a tela estiver desconfigurada, da um print e salva no diretório path_print
        screenshot_cad_prod_novo_limpo = pyautogui.screenshot(rf"{path_print}\screenshot_cad_prod_novo_limpo.png")
        print("Janela Cadastro de Produto > btn (NOVO) DESCONFIGURADA! Veja o print da imagem")
    #Insere o registro
    time.sleep(15)
    #Insere os dados no campo Descrição
    cad_prod_descricao = pyautogui.locateOnScreen(rf"{path}\cad_prod_descricao.png", confidence=0.9)
    pyautogui.click(cad_prod_descricao)
    time.sleep(5)
    pyautogui.write("PRODUTO TESTE AUTOMATICO")
    time.sleep(5)
    #Botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    pyautogui.click(btn_salvar)
    time.sleep(5)

    #Verifica mensagem para preencher Grupo e SubGrupo
    if pyautogui.locateOnScreen(rf"{path}\msg_cad_prod_grup_subgrup.png", confidence=0.9):
        time.sleep(5)
        print("Janela Cadastro de Produto > Mensagem para preencher Grupo e Subgrupo OK")
        time.sleep(15)
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        pyautogui.click(btn_ok)
        #pyautogui.press('enter')
    else:
        #Se não houver mensagem de grupo e subgrupo, da um print e salva no diretório path_print
        screenshot_msg_cad_prod_grup_subgrup = pyautogui.screenshot(rf"{path_print}\screenshot_msg_cad_prod_grup_subgrup.png")
        print("Janela Cadastro de Produto > Não houve mensagem para preencher Grupo e Subgrupo! Veja o print da imagem")
    time.sleep(10)
    #Aperta tab 5 vezes para ir até o campo Grupo
    pyautogui.press('tab', presses = 5)
    time.sleep(5)
    #Aperta seta para baixo para selecionar um grupo
    pyautogui.press('down')
    time.sleep(2)
    #Aperta tab 2 vezes para ir até o campo SubGrupo
    pyautogui.press('tab', presses = 2)
    time.sleep(2)
    #Aperta seta para baixo para selecionar um subgrupo
    pyautogui.press('down')
    time.sleep(5)
    #Clica no botão salvar
    pyautogui.click(btn_salvar)
    time.sleep(10)
    #Verifica a mensagem para selecionar a menor unidade
    if pyautogui.locateOnScreen(rf"{path}\msg_cad_prod_sel_men_uni.png", confidence=0.9):
        time.sleep(5)
        print("Janela Cadastro de Produto > Mensagem para Selecioonar a Menor Unidade OK")
        time.sleep(5)
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        pyautogui.click(btn_ok)
        #pyautogui.press('enter')
    else:
        #Se não houver mensagem de selecionar a menor unidade, da um print e salva no diretório path_print
        screenshot_msg_cad_prod_sel_men_uni = pyautogui.screenshot(rf"{path_print}\screenshot_msg_cad_prod_sel_men_uni.png")
        print("Janela Cadastro de Produto > Não houve mensagem para Selecioonar a Menor Unidade! Veja o print da imagem")
    #Aba Unidade
    time.sleep(5)
    time.sleep(15)
    cad_prod_abauni = pyautogui.locateOnScreen(rf"{path}\cad_prod_abauni.png", confidence=0.9)
    pyautogui.click(cad_prod_abauni)
    time.sleep(15)
    #Clica no Campo Unid.
    cad_prod_aba_uni_unid =  pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_uni_unid.png", confidence=0.9)
    #Escreve 'UN' no campo Unid
    time.sleep(10)
    pyautogui.click(cad_prod_aba_uni_unid)
    time.sleep(5)
    pyautogui.write("UN")
    time.sleep(5)
    #Seleciona a unidade e seleciona o bit menor
    pyautogui.press(['down', 'enter', 'tab','left','left','space'])
    time.sleep(2)
    #Botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    pyautogui.click(btn_salvar)
    time.sleep(30)
    #Fechar tela OuroNet
    #Verifica se a janela Cadastro de Produto está aberta
    if  pyautogui.getWindowsWithTitle("Cadastro de Produto"):
        #Maximiza a janela Cadastro de Produto
        pyautogui.getWindowsWithTitle("Cadastro de Produto")[0].maximize()
        time.sleep(5)
        #Fecha a janela Cadastro de produto com o comando alt + f4
        pyautogui.hotkey('alt','f4')
        time.sleep(2)
        print("Janela Cadastro do Produto fechada com sucesso!")
    else:
        screenshot_fechar_tela_cad_prod = pyautogui.screenshot(rf"{path_print}\screenshot_fechar_tela_cad_prod.png")
        print("Não foi possível fechar a janela Cadastro de Produto! Veja o print da imagem.")
    