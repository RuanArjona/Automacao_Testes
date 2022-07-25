import pyautogui
from time import sleep
from maximiza_fecha import *


# Pasta de imagens
path = r"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
# Implementação - Renan 02/12/2021
# Método de cadastro de Empresas

# Nome da empresa
global cad_emp_empresa
cad_emp_empresa = pyautogui.locateOnScreen(rf"{path}\cad_emp_empresa.png", confidence=0.9)


def cadastroEmpresas():
    sleep(1)
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('Ctrl', '1')
    sleep(10)
    # Menu Superior > Tabelas
    menu_tabelas = pyautogui.locateOnScreen(rf"{path}\menu_tabelas.png", confidence=0.9)
    pyautogui.click(menu_tabelas)
    sleep(2)
    # Menu Superior > Tabelas > Empresas
    menu_tab_empresas = pyautogui.locateOnScreen(rf"{path}\menu_tab_empresas.png", confidence=0.9)
    pyautogui.click(menu_tab_empresas)
    sleep(2)
    # Menu Superior > Tabelas > Empresas > Cadastro de Empresas
    menu_tab_emp_cadastro = pyautogui.locateOnScreen(rf"{path}\menu_tab_emp_cadastro.png", confidence=0.9)
    pyautogui.click(menu_tab_emp_cadastro)
    sleep(10)
    # Tela Cadastro de Empresas > Botão Novo
    # Verifica mensagem se não tiver cadastros
    if pyautogui.locateOnScreen(rf"{path}\msg_nen_reg_enc.png", confidence=0.9):
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        sleep(0.5)
        pyautogui.click(btn_ok)
        btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
        pyautogui.click(btn_novo)
        sleep(2)
    else:
        btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
        pyautogui.click(btn_novo)
        sleep(2)


cadastroEmpresas()


def inserirDados():
    sleep(15)
    # campo "Empresa"
    pyautogui.write("EMPRESA DE TESTE AUTOMATICO - 1")
    sleep(0.5)
    pyautogui.press("tab")
    sleep(0.5)
    # Endereço da empresa
    pyautogui.write("ENDEREÇO DE TESTE AUTOMATICO")
    sleep(0.5)
    pyautogui.press("tab")
    sleep(0.5)
    # Número do endereço da empresa
    pyautogui.write("444")
    sleep(0.5)
    pyautogui.press("tab", presses=2)
    sleep(0.5)
    # Bairro do endereço da empresa
    pyautogui.write("BAIRRO DE TESTE AUTOMATICO")
    sleep(0.5)
    pyautogui.press("tab")
    sleep(0.5)
    # CEP do endereço da empresa
    pyautogui.write("14082289")
    sleep(0.5)
    pyautogui.press("tab")
    sleep(0.5)
    # Cidade da empresa
    pyautogui.write("RIO PRETO")
    sleep(0.5)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    # Estado da empresa
    pyautogui.write("SP")
    sleep(0.5)
    pyautogui.press('tab')
    sleep(0.5)
    # Pais da empresa
    pyautogui.write("BRASIL")
    sleep(0.5)
    pyautogui.press("tab")
    sleep(0.5)
    # Telefone 1 da empresa
    pyautogui.write("1639999999")
    sleep(0.5)
    pyautogui.press("tab", presses=4)
    sleep(0.5)
    # CNPJ da empresa
    pyautogui.write("24923118000150")
    sleep(0.5)
    pyautogui.press("tab", presses=3)
    sleep(0.5)
    # Nome Fantasia da empresa
    pyautogui.write("NOME FANTASIA AUTOMATICO - 1")
    sleep(0.5)
    # Botão Salvar
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
    pyautogui.click(btn_salvar)
    # Método implementado - Renan 03/12/2021
    # Método alterar dados > Cadastro de Empresas


inserirDados()


def alterarDados():
    sleep(2)
    # Realiza a busca do registro inserido
    # Método implementado - Renan 06/12/2021
    # Método utilizando o filtro:
    cad_emp_grid_empresa = pyautogui.locateOnScreen(rf"{path}\cad_emp_grid_empresa.png", confidence=0.9)
    pyautogui.click(cad_emp_grid_empresa)
    sleep(0.5)
    # Campo Filtro
    procura_filtro = pyautogui.locateOnScreen(rf"{path}\procura_filtro.png", confidence=0.9)
    pyautogui.click(procura_filtro)
    sleep(0.5)
    # Insere a EMPRESA DE TESTE AUTOMATICO - 1
    pyautogui.write("EMPRESA DE TESTE AUTOMATICO - 1")
    sleep(0.5)
    # Aperta tab para selecionar o botão de filtro (Alterado para o teclado pois o mesmo estava
    # com conflito no botão Filtro da grid superior Renan - 24/03/2022 )
    pyautogui.press('tab')
    sleep(0.5)
    # Aperta espaço para aplicar o filtro
    pyautogui.press('space')
    sleep(5)
    # Acha o campo 'Empresa' com preenchimento
    if pyautogui.locateOnScreen(rf"{path}\cad_emp_empresa_incluido.png", confidence=0.9):
        cad_emp_empresa_incluido = pyautogui.locateOnScreen(rf"{path}\cad_emp_empresa_incluido.png", confidence=0.9)
        sleep(5)
        # Clica no campo Empresa
        pyautogui.click(cad_emp_empresa_incluido)
        sleep(0.5)
        # Seleciona o campo inteiro
        pyautogui.hotkey('ctrl', 'a')
        sleep(0.5)
        # Exibe a mensagem do nome da empresa alterado
        pyautogui.write("EMPRESA DE TESTE AUTOMATICO - ALTERADO")
        sleep(0.5)
        btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png", confidence=0.9)
        pyautogui.click(btn_salvar)
    else:
        print("Achou a empresa e pressionou e ALTEROU o nome")
    # Fecha a tela de Cadastro de empresa
    sleep(2)


alterarDados()


def excluirDados():
    procura_filtro = pyautogui.locateOnScreen(rf"{path}\btn_remov_filtro.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(procura_filtro)
    sleep(0.5)
    # Localiza e clica na aba "Filtro"
    aba_filtro = pyautogui.locateOnScreen(rf"{path}\btn_aba_filtro.png")
    sleep(0.5)
    pyautogui.click(aba_filtro)
    sleep(1)
    # Localiza e clica no botão "Remover Filtro"
    remove_filtro = pyautogui.locateOnScreen(rf"{path}\remove_filtro.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(remove_filtro)
    sleep(1)
    camp_emp = pyautogui.locateOnScreen(rf"{path}\camp_empres_aba_filtro.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(camp_emp)
    # Insere a EMPRESA DE TESTE AUTOMATICO - ALTERADO
    pyautogui.write("EMPRESA DE TESTE AUTOMATICO - ALTERADO")
    sleep(5)
    btn_filtrar = pyautogui.locateOnScreen(rf"{path}\btn_filtrar.png", confidence=0.9)
    sleep(0.5)
    btn_filtrar = pyautogui.click(btn_filtrar)
    sleep(10)
    # Clica no botão "Excluir" para realizar a exclusão do dado
    excluir_cad_emp = pyautogui.locateOnScreen(rf"{path}\btn_excluir.png")
    sleep(0.5)
    pyautogui.click(excluir_cad_emp)
    sleep(0.5)
    # Clica no botão "Sim" na mensagem de exclusão dos dados
    btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(btn_sim)
    sleep(0.5)
    print("O dados da empresa foi excluidos com sucesso!")
    sleep(5)
    fechaTelaOuroWeb()


excluirDados()