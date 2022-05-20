import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")
path_print = (rf"C:\Teste Automatizado OuroWeb\bin\project\tests\img\print_img_erro")
#Método implementado - Renan 31/01/2022

    #Implementado - Renan 31/01/2022
    #pesquisar nome do produto
def alterarProd():
    #Aperta ctrl+f10 para abrir a tela Cadastro Produto Busca
    pyautogui.hotkey('ctrl','f10')    
    time.sleep(5)
    #Aperta tab 3x até o campo Nome
    pyautogui.press('tab', presses=4)
    time.sleep(2)
    #Insere o nome do produto cadastrado como PRODUTO DE TESTE AUTOMATICO
    pyautogui.write("PRODUTO TESTE AUTOMATICO")
    time.sleep(10)
    #Clica no botão OK para pesquisar o item
    btn_ok_cad_prod_busc = pyautogui.locateOnScreen(rf"{path}\btn_ok_cad_prod_busc.png", confidence=0.9)
    time.sleep(5)
    pyautogui.click(btn_ok_cad_prod_busc)
    time.sleep(20)
    #Verifica se foi aberta a tela ou deu algum erro
    if pyautogui.getWindowsWithTitle("Cadastro de Produto"):
        print("Produto encontrado com Sucesso!")
    
    else:
        #Caso não encontre e abra a tela do Cadastro de Produto, printa a tela
        screenshot_cad_prod_nao_encont = pyautogui.screenshot(rf"{path_print}\screenshot_cad_prod_nao_encont.png")
        print("Cadastro do Produto não encontrado, Verifique o erro no print")
    time.sleep(20)
    #Seleciona o campo Código do Produto para copiar e pesquisar pelo código posteriormente
    #Aperta tab 8x até o campo código do produto
    pyautogui.press('tab', presses = 8)
    #Copiar código do produto e colar em txt
    time.sleep(5)
    #Copia o Código do Produto
    pyautogui.hotkey('ctrl','c')
    time.sleep(10)
    #Abre o windows + r
    pyautogui.hotkey('win','r')
    time.sleep(5)
    #Escreve notepad e aperta enter
    pyautogui.write("notepad")
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    #Cola o Código do Produto no txt
    pyautogui.hotkey('ctrl','v')
    time.sleep(5)
    #Salva o txt como CODIGO-PRODUTO
    pyautogui.hotkey('ctrl','s')
    time.sleep(5)
    pyautogui.write("CODIGO-PRODUTO")
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("CODIGO-PRODUTO.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
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
    #Abre a tela de cadastro de produto
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Menu Principal > Cadastro
    menu_princ_cad = pyautogui.locateOnScreen(rf"{path}\menu_cadastro.png", confidence=0.9)
    pyautogui.click(menu_princ_cad)
    time.sleep(5)
    #Menu Principal > Cadastro > Produto
    menu_cadastro_prod = pyautogui.locateOnScreen(rf"{path}\menu_cadastro_prod.png", confidence=0.9)
    pyautogui.click(menu_cadastro_prod)
    time.sleep(10)
    #Seleciona o Campo Código do Produto
    cad_prod_aba_filtro_cod_item = pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_filtro_cod_item.png", confidence=0.9)
    pyautogui.click(cad_prod_aba_filtro_cod_item)
    time.sleep(10)
    #Maximiza o txt do número do Codigo do Produto
    pyautogui.getWindowsWithTitle("CODIGO-PRODUTO.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Codigo do Produto
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Codigo do Produto
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("CODIGO-PRODUTO.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Codigo do Produto no campo para pesquisa
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
    #Clica no botão Filtrar
    btn_filtrar = pyautogui.locateOnScreen(rf"{path}\btn_filtrar.png", confidence=0.9)
    pyautogui.click(btn_filtrar)
    time.sleep(20)
    #Clica na aba Medicamentos
    cad_prod_aba_medicamentos = pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_medicamentos.png", confidence=0.9)
    pyautogui.click(cad_prod_aba_medicamentos)
    time.sleep(10)
    #Na aba Medicamentos, seleciona o campo Tipo de Produto
    cad_prod_aba_med_tipo_de_produto = pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_med_tipo_de_produto.png", confidence=0.9)
    #Move o mouse para o campo Tipo de Produto
    pyautogui.moveTo(cad_prod_aba_med_tipo_de_produto)
    time.sleep(5)
    #Clica no campo Tipo de Produto
    pyautogui.click(cad_prod_aba_med_tipo_de_produto)
    time.sleep(10)
    #Aperta seta para baixo para selecionar o Tipo de Produto
    pyautogui.press('backspace')
    #Enquanto o tipo do produto não for genérico, aperta seta para baixo
    cad_prod_aba_med_tip_de_prod_gen = pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_med_tip_de_prod_gen.png")
    while cad_prod_aba_med_tip_de_prod_gen != pyautogui.locateOnScreen(rf"{path}\cad_prod_aba_med_tip_de_prod_gen.png"):
        time.sleep(2)
        #Pressiona seta para baixo até encontrar o tipo = Genérico
        pyautogui.press('down')
    else:
        #Acha o tipo genérico e clica enter
        pyautogui.press('enter')
    time.sleep(10)    
    #Clica no botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    pyautogui.click(btn_salvar)
    time.sleep(10)
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

