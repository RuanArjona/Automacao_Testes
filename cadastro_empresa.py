import pyautogui
import time

#Pasta de imagens
path = (r"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")
#Implementação - Renan 02/12/2021
#Método de cadastro de Empresas

#btn Salvar
global btn_salvar
btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)

#Nome da empresa
global cad_emp_empresa
cad_emp_empresa = pyautogui.locateOnScreen(rf"{path}\cad_emp_empresa.png", confidence=0.9)

def cadastroEmpresas():
    #Menu Superior > Tabelas
    menu_tabelas = pyautogui.locateOnScreen(rf"{path}\menu_tabelas.png", confidence=0.9)
    pyautogui.click(menu_tabelas)
    time.sleep(5)
    #Menu Superior > Tabelas > Empresas
    menu_tab_empresas = pyautogui.locateOnScreen(rf"{path}\menu_tab_empresas.png", confidence=0.9)
    pyautogui.click(menu_tab_empresas)
    time.sleep(5)
    #Menu Superior > Tabelas > Empresas > Cadastro de Empresas
    menu_tab_emp_cadastro = pyautogui.locateOnScreen(rf"{path}\menu_tab_emp_cadastro.png", confidence=0.9)
    pyautogui.click(menu_tab_emp_cadastro)
    time.sleep(5)

    #Tela Cadastro de Empresas > Botão Novo 
    # Verifica mensagem se não tiver cadastros
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
        
        #Método implementado - Renan 03/12/2021
        #Inserindo dados no cadastro de empresa *Dados essenciais*
        
def inserirDados():
    time.sleep(15)
    pyautogui.click(cad_emp_empresa)
    time.sleep(2)
    pyautogui.write("EMPRESA DE TESTE AUTOMATICO - 1")
    time.sleep(5)
    #Endereço da empresa
    cad_emp_endereco = pyautogui.locateOnScreen(rf"{path}\cad_emp_endereco.png", confidence=0.9)
    pyautogui.click(cad_emp_endereco)
    time.sleep(2)
    pyautogui.write("ENDEREÇO DE TESTE AUTOMATICO")
    time.sleep(5)
    #Número do endereço da empresa
    cad_emp_num = pyautogui.locateOnScreen(rf"{path}\cad_emp_num.png", confidence=0.9)
    pyautogui.click(cad_emp_num)
    time.sleep(2)
    pyautogui.write("444")
    time.sleep(5)
    #Bairro do endereço da empresa
    cad_emp_bairro = pyautogui.locateOnScreen(rf"{path}\cad_emp_bairro.png", confidence=0.9)
    pyautogui.click(cad_emp_bairro)
    time.sleep(2)
    pyautogui.write("BAIRRO DE TESTE AUTOMATICO")
    time.sleep(5)
    #CEP do endereço da empresa
    cad_emp_cep = pyautogui.locateOnScreen(rf"{path}\cad_emp_cep.png", confidence=0.9)
    pyautogui.click(cad_emp_cep)
    time.sleep(2)
    pyautogui.press('home')
    time.sleep(2)
    pyautogui.write("14085289")
    time.sleep(5)
    #Cidade da empresa
    cad_emp_cidade = pyautogui.locateOnScreen(rf"{path}\cad_emp_cidade.png", confidence=0.9)
    pyautogui.click(cad_emp_cidade)
    time.sleep(2)
    pyautogui.write("RIO PRETO")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    #Estado da empresa
    cad_emp_estado = pyautogui.locateOnScreen(rf"{path}\cad_emp_estado.png", confidence=0.9)
    pyautogui.click(cad_emp_estado)
    time.sleep(2)
    pyautogui.write("SP")
    time.sleep(5)
    #Pais da empresa
    #cad_emp_pais = pyautogui.locateOnScreen(rf"{path}\cad_emp_pais.png", confidence=0.9)
    pyautogui.press('tab')
    #time.sleep(5)
    #pyautogui.click(cad_emp_pais)
    time.sleep(2)
    pyautogui.write("BRASIL")
    time.sleep(5)
    #Telefone 1 da empresa
    cad_emp_fone1 = pyautogui.locateOnScreen(rf"{path}\cad_emp_fone1.png", confidence=0.9)
    time.sleep(5)
    pyautogui.click(cad_emp_fone1)
    time.sleep(2)
    pyautogui.press('home')
    time.sleep(2)
    pyautogui.write("1639999999")
    time.sleep(5)
    #CNPJ da empresa
    cad_emp_cnpj = pyautogui.locateOnScreen(rf"{path}\cad_emp_cnpj.png", confidence=0.9)
    time.sleep(5)
    pyautogui.click(cad_emp_cnpj)
    time.sleep(2)
    pyautogui.press('home')
    time.sleep(2)
    pyautogui.write("85968303000155")
    time.sleep(5)
    #Nome Fantasia da empresa
    cad_emp_nome_fantasia = pyautogui.locateOnScreen(rf"{path}\cad_emp_nome_fantasia.png", confidence=0.9)
    time.sleep(5)
    pyautogui.click(cad_emp_nome_fantasia)
    time.sleep(2)
    pyautogui.write("NOME FANTASIA AUTOMATICO - 1")
    time.sleep(5)
    #Botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    pyautogui.click(btn_salvar)
    #Método implementado - Renan 03/12/2021
    #Método alterar dados > Cadastro de Empresas
def alterarDados():
    time.sleep(5)
    #Realiza a busca do registro inserido
    #Método implementado - Renan 06/12/2021
    #Método utilizando o filtro:
    cad_emp_grid_empresa = pyautogui.locateOnScreen(rf"{path}\cad_emp_grid_empresa.png", confidence=0.9)
    pyautogui.click(cad_emp_grid_empresa)
    time.sleep(5)
    #Campo Filtro
    procura_filtro = pyautogui.locateOnScreen(rf"{path}\procura_filtro.png", confidence=0.9)
    pyautogui.click(procura_filtro)
    time.sleep(5)
    #Insere a EMPRESA DE TESTE AUTOMATICO - 1
    pyautogui.write("EMPRESA DE TESTE AUTOMATICO - 1")
    time.sleep(10)
    #Aperta tab para selecionar o botão de filtro (Alterado para o teclado pois o mesmo estava com conflito no botão Filtro da grid superior Renan - 24/03/2022 )
    pyautogui.press('tab')
    time.sleep(5)
    #Aperta espaço para aplicar o filtro
    pyautogui.press('space')
    #A imagem foi trocada pelo 'tab' e 'space' pois estava dando conflito com a parte superior da grid. Código comentado. (Renan - 24/03/2022)
    #proc_filt_btn_filtrar_cad_emp = pyautogui.locateOnScreen(rf"{path}\proc_filt_btn_filtrar_cad_emp.png", confidence=0.9)
    #pyautogui.click(proc_filt_btn_filtrar_cad_emp)
    time.sleep(10)
    #Acha o campo 'Empresa' com preenchimento
    if pyautogui.locateOnScreen(rf"{path}\cad_emp_empresa_incluido.png", confidence=0.9):
        cad_emp_empresa_incluido = pyautogui.locateOnScreen(rf"{path}\cad_emp_empresa_incluido.png", confidence=0.9)
        time.sleep(10)
        #Clica no campo Empresa
        pyautogui.click(cad_emp_empresa_incluido)
        time.sleep(5)
        #Seleciona o campo inteiro
        pyautogui.hotkey('ctrl','a')
        time.sleep(5)
        #Exibe a mensagem do nome da empresa alterado
        pyautogui.write("EMPRESA DE TESTE AUTOMATICO - ALTERADO")
        time.sleep(5)
        pyautogui.click(btn_salvar)
    else:
        print("Achou a empresa e pressionou e ALTEROU o nome")
    #Fecha a tela de Cadastro de empresa
    time.sleep(5)
    pyautogui.getWindowsWithTitle("Cadastro de Empresa")[0].close()

        
