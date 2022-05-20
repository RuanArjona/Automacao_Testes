import pyautogui
import time

#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método Implementado 10/01/2022
#Método para clicar no botão Filtro na tela de Histórico de Movimentos
def filtroHistMov():
    #Clica no botão filtrar na tela de Histórico de Movimentos
    btn_filtro_hist_orc = pyautogui.locateOnScreen(rf"{path}\btn_filtro_hist_orc.png", confidence=0.9)
    pyautogui.click(btn_filtro_hist_orc)

#=================================================================================================
#Implementado - Renan 07/01/2022

#Método para salvar o número do Orçamento de Venda em um txt
def salvaNumeroOrcVend():
    #Seleciona o Campo Nº do Orçamento
    time.sleep(2)
    #Copia o Nº do orçamento
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Abre o windows + r
    pyautogui.hotkey('win','r')
    time.sleep(5)
    #Escreve notepad e aperta enter
    pyautogui.write("notepad")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Cola o Nº do orçamento no txt
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    #Salva o txt como NUMERO-ORCAMENTO-VENDA
    pyautogui.hotkey('ctrl','s')
    time.sleep(2)
    pyautogui.write("NUMERO-ORCAMENTO-VENDA")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-ORCAMENTO-VENDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)

#Método Inserir Número do Orçamento de Venda na tela de Histórico de Movimentos
def insereNumeroOrcVend():
    #Abre o Menu Principal    
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Menu Superior > Histórico
    pyautogui.hotkey('shift','f8')
    time.sleep(10)
    #Digita no campo Classe do Mov. = "or"
    pyautogui.write("or")
    time.sleep(5)
    #Aperta a tecla enter
    pyautogui.press('enter')
    time.sleep(2)
    #Insere a data = 01/01/2019
    #pyautogui.write("010119")
    time.sleep(2)
    #Aperta tab 11 vezes até o campo Nº Documento
    pyautogui.press('tab', presses=11)
    time.sleep(5)
    #Maximiza o txt do número do orçamento
    pyautogui.getWindowsWithTitle("NUMERO-ORCAMENTO-VENDA.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Campo Nº do Orçamento
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Nº do orçamento
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-ORCAMENTO-VENDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Nº do orçamento do txt no Histórico de Movimentos
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
#=================================================================================================
    

#Método para salvar o número do Pedido de Venda em um txt
def salvaNumeroPedVend():
    #Seleciona o Campo Nº do Pedido
    time.sleep(5)
    #Copia o Nº do Pedido
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Abre o windows + r
    pyautogui.hotkey('win','r')
    time.sleep(5)
    #Escreve notepad e aperta enter
    pyautogui.write("notepad")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Cola o Nº do Pedido no txt
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    #Salva o txt como NUMERO-PEDIDO
    pyautogui.hotkey('ctrl','s')
    time.sleep(2)
    pyautogui.write("NUMERO-PEDIDO-VENDA")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
#=================================================================================================

#Método Inserir Número do Pedido Venda na tela de Histórico de Movimentos
def insereNumeroPedVend():
    #Abre o Menu Principal    
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Menu Superior > Histórico
    pyautogui.hotkey('shift','f8')
    time.sleep(10)
    #Digita no campo Classe do Mov. = "pedido venda"
    pyautogui.write("pedido venda")
    #Faz a verificação se o Pedido Venda está selecionado
    while pyautogui.locateOnScreen(rf"{path}\hist_mov_class_mov_ped_vend.png", confidence=0.9) == False:
        pyautogui.press('down')
        time.sleep(2)
    else:
        pyautogui.press('enter')
        print("Encontrou a classe Pedido Venda e clicou ENTER")
        time.sleep(2)
        
    time.sleep(5)
    #Aperta a tecla enter
    #pyautogui.press('enter')
    time.sleep(2)
    #Insere a data = 01/01/2019
    #pyautogui.write("010119")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Aperta tab 11 vezes até o campo Nº Documento
    pyautogui.press('tab', presses=11)
    time.sleep(5)
    #Maximiza o txt do número do Pedido Venda
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Campo Nº do Pedido Venda
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Nº do Pedido Venda
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Nº do Pedido Venda do txt no Histórico de Movimentos
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
#=================================================================================================

#==================================PEDIDO DE VENDA SIMPLES========================================#
#Método para salvar o número do Pedido de Venda Simples em um txt
def salvaNumeroPedVendSimp():
    #Seleciona o Campo Nº do Pedido
    time.sleep(5)
    #Copia o Nº do Pedido
    pyautogui.hotkey('ctrl','c')
    time.sleep(10)
    #Abre o windows + r
    pyautogui.hotkey('win','r')
    time.sleep(5)
    #Escreve notepad e aperta enter
    pyautogui.write("notepad")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Cola o Nº do Pedido no txt
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    #Salva o txt como NUMERO-PEDIDO
    pyautogui.hotkey('ctrl','s')
    time.sleep(2)
    pyautogui.write("NUMERO-PEDIDO-VENDA-SIMPLES")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA-SIMPLES.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)


#Método Inserir Número do Pedido Venda Simples na tela de Histórico de Movimentos
def insereNumeroPedVendSimp():
    #Abre o Menu Principal    
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Menu Superior > Histórico
    pyautogui.hotkey('shift','f8')
    time.sleep(10)
    #Digita no campo Classe do Mov. = "pedido venda"
    pyautogui.write("pedido venda")
    #Faz a verificação se o Pedido Venda está selecionado
    while pyautogui.locateOnScreen(rf"{path}\hist_mov_class_mov_ped_vend.png", confidence=0.9) == False:
        pyautogui.press('down')
        time.sleep(2)
    else:
        time.sleep(5)
        pyautogui.press('enter')
        print("Encontrou a classe Pedido Venda e clicou ENTER")
        time.sleep(2)
        
    time.sleep(7)
    #Aperta a tecla enter
    #pyautogui.press('enter')
    #Insere a data = 01/01/2019
    #pyautogui.write("010119")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Aperta tab 11 vezes até o campo Nº Documento
    pyautogui.press('tab', presses=11)
    time.sleep(5)
    #Maximiza o txt do número do Pedido Venda
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA-SIMPLES.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Campo Nº do Pedido Venda
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Nº do Pedido Venda
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-VENDA-SIMPLES.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Nº do Pedido Venda do txt no Histórico de Movimentos
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)

#=================================================================================================
#==================================VENDA SAÍDA====================================================#
#Método para salvar o número do Venda Saída em um txt
def salvaNumeroVendSaid():
    #Seleciona o Campo Nº do Venda Saída
    time.sleep(5)
    #Copia o Nº do Venda Saída
    pyautogui.hotkey('ctrl','c')
    time.sleep(10)
    #Abre o windows + r
    pyautogui.hotkey('win','r')
    time.sleep(5)
    #Escreve notepad e aperta enter
    pyautogui.write("notepad")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Cola o Nº do Venda Saída no txt
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    #Salva o txt como NUMERO-VENDA-SAIDA
    pyautogui.hotkey('ctrl','s')
    time.sleep(2)
    pyautogui.write("NUMERO-VENDA-SAIDA")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-VENDA-SAIDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)


#Método Inserir Número do Venda Saída na tela de Histórico de Movimentos
def insereNumeroVendSaid():
    #Abre o Menu Principal    
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Menu Superior > Histórico
    pyautogui.hotkey('shift','f8')
    time.sleep(10)
    #Digita no campo Classe do Mov. = "Venda Saída"
    pyautogui.write("venda")
    #Faz a verificação se a Venda Saída está selecionado
    while pyautogui.locateOnScreen(rf"{path}\hist_mov_class_mov_vend_said.png", confidence=0.9) == False:
        pyautogui.press('down')
        time.sleep(2)
    else:
        time.sleep(5)
        pyautogui.press('enter')
        print("Encontrou a classe Venda e clicou ENTER")
        time.sleep(2)
        
    time.sleep(7)
    #Aperta a tecla enter
    #pyautogui.press('enter')
    #Insere a data = 01/01/2019
    #pyautogui.write("010119")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #Aperta tab 11 vezes até o campo Nº Documento
    pyautogui.press('tab', presses=10)
    time.sleep(5)
    #Maximiza o txt NUMERO-VENDA-SAIDA
    pyautogui.getWindowsWithTitle("NUMERO-VENDA-SAIDA.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Campo Nº da Venda Saída
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Nº da Venda Saída
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-VENDA-SAIDA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Nº do Venda Saída do txt no Histórico de Movimentos
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)

#=================================================================================================#
#Método Concluir Orçamento de Venda
def concluirOrc():
    if pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9):
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.press('o')
        time.sleep(5)
        #Clica no botão Concluir
        btn_concluir_orc_venda = pyautogui.locateOnScreen(rf"{path}\btn_concluir_orc_venda.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_orc_venda)
    else:
        #Clica no botão Concluir
        time.sleep(5)
        btn_concluir_orc_venda = pyautogui.locateOnScreen(rf"{path}\btn_concluir_orc_venda.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_orc_venda)
        #Mensagem de rentabilidade
        time.sleep(5)
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.press('o')
        

    #Espera 15s    
    time.sleep(15)

    #Implementado - Renan 10/12/2021
    #Verifica mensagem de conclusão de movimento
    if pyautogui.locateOnScreen(rf"{path}\msg_conf_movi.png", confidence=0.9):
        time.sleep(2)
    #Clica no botão sim para concluir o movimento
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.press('s')
        time.sleep(10)
        print("Clicou no botão 'sim' para concluir o movimento")
        time.sleep(5)
    #Clica no botâo não para não imprimir o movimento
        btn_nao_imp_mov = pyautogui.locateOnScreen(rf"{path}\btn_nao_imp_mov.png", confidence=0.9)
        pyautogui.press('n')
        time.sleep(10)
        print("Clicou no botão 'não' para não imprimir o documento")
    else:
        print("Não teve mensagem de confirmação do movimento, verifique o erro!")
#=================================================================================================
#Método Concluir Pedido Venda
#Implementado - Renan 10/12/2021
def concluirPedVend():
        #Mensagem de rentabilidade
    if pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9):
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
        time.sleep(5)
        #Clica no botão Concluir
        btn_concluir_ped_venda = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_venda.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_venda)
    else:
        #Clica no botão Concluir
        time.sleep(5)
        btn_concluir_ped_venda = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_venda.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_venda)
        #Mensagem de rentabilidade
        time.sleep(5)
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
        

    #Espera 15s    
    time.sleep(15)

    #Implementado - Renan 10/12/2021
    #Verifica mensagem de conclusão de movimento
    if pyautogui.locateOnScreen(rf"{path}\msg_conf_movi.png", confidence=0.9):
        time.sleep(2)
    #Clica no botão sim para concluir o movimento
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.click(btn_sim)
        time.sleep(5)
        print("Clicou no botão 'sim' para concluir o movimento")
        time.sleep(5)
    #Clica no botão Não para não imprimir o movimento
        btn_nao_imp_mov = pyautogui.locateOnScreen(rf"{path}\btn_nao_imp_mov.png", confidence=0.9)
        pyautogui.click(btn_nao_imp_mov)
        time.sleep(5)
        print("Clicou no botão 'não' para não imprimir o documento")
    else:
        print("Não teve mensagem de confirmação do movimento, verifique o erro!")

#=================================================================================================

#============================Métodos Venda Saída==================================================
def concluirVendSaid():
        #Implementado - Renan 10/12/2021
        #Mensagem de rentabilidade
    if pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9):
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
        time.sleep(5)
        #Clica no botão Concluir
        btn_concluir_venda_saida = pyautogui.locateOnScreen(rf"{path}\btn_concluir_venda_saida.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_venda_saida)
    else:
        #Clica no botão Concluir
        time.sleep(5)
        btn_concluir_venda_saida = pyautogui.locateOnScreen(rf"{path}\btn_concluir_venda_saida.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_venda_saida)
        #Mensagem de rentabilidade
        time.sleep(5)
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
        

    #Espera 15s    
    time.sleep(15)

    #Implementado - Renan 10/12/2021
    #Verifica mensagem de conclusão de movimento
    if pyautogui.locateOnScreen(rf"{path}\msg_conf_movi.png", confidence=0.9):
        time.sleep(2)
    #Clica no botão sim para concluir o movimento
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.click(btn_sim)
        time.sleep(5)
        print("Clicou no botão 'sim' para concluir o movimento")
        time.sleep(5)
    #Clica no botão Não para não imprimir o movimento
        btn_nao_imp_mov = pyautogui.locateOnScreen(rf"{path}\btn_nao_imp_mov.png", confidence=0.9)
        pyautogui.click(btn_nao_imp_mov)
        time.sleep(5)
        print("Clicou no botão 'não' para não imprimir o documento")
    else:
        print("Não teve mensagem de confirmação do movimento, verifique o erro!")
#=================================================================================================