import pyautogui
from time import sleep

# Caminho das imagens
path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")
# Implementação - Ruan 16/05/2022
def CondPag():
    #Menu Superior > Tabelas
    menu_tabelas = pyautogui.locateOnScreen(rf"{path}\menu_tabelas.png", confidence=0.9)
    pyautogui.click(menu_tabelas)
    sleep(5)
    #Menu Superior > Tabelas > Financeiro
    menu_tab_financeiro = pyautogui.locateOnScreen(rf"{path}\menu_tab_financeiro.png", confidence=0.9)
    pyautogui.click(menu_tab_financeiro)
    sleep(5)
    #Menu Superior > Tabela > Financeiro > Condições de Pagamento
    menu_cond_pagto = pyautogui.locateOnScreen(rf"{path}\menu_tab_finan_cond_pagto.png")
    pyautogui.click(menu_cond_pagto)
    sleep(15)
    #Clica no botão "Novo"
    btn_novo = pyautogui.locateOnScreen(rf"{path}\btn_novo.png", confidence=0.9)
    pyautogui.click(btn_novo)
    sleep(5)
    #Clica no botão "Salvar"
    btn_salvar = pyautogui.locateOnScreen(rf"{path}\btn_salvar.png")
    pyautogui.click(btn_salvar)
    sleep(5)
    #Clica no botão "Ok" alerta
    btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png")
    pyautogui.click(btn_ok)
    print("é esse ok")
    #Preenche textbox "Parcela" com valor 3
    pyautogui.write("3")
    sleep(2)
    #Clica no botão "Salvar"
    pyautogui.click(btn_salvar)
    sleep(5)
    #Clica no botão "Ok" alerta
    pyautogui.click(btn_ok)
    #Preenche textbox "Descrição" com valor Teste
    pyautogui.write("Teste")
    sleep(2)
    #Clica no botão "Salvar"
    pyautogui.click(btn_salvar)
    sleep(5)
