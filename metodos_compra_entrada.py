import pyautogui
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método Implementado 13/05/2022
#Método para clicar no botão Filtro na tela de Histórico de Movimentos
def filtroHistMov():
    #Clica no botão filtrar na tela de Histórico de Movimentos
    btn_filtro_hist_orc = pyautogui.locateOnScreen(rf"{path}\btn_filtro_hist_orc.png", confidence=0.9)
    pyautogui.click(btn_filtro_hist_orc)

#=================================================================================================
#Implementado - Fernando 13/05/2022

#Método para salvar o número do Pedido de Compra em um txt
def salvaNumeroPedComp():
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
    pyautogui.write("NUMERO-PEDIDO-COMPRA")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-COMPRA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
#=================================================================================================
#Implementado - Fernando 13/05/2022

#Método Inserir Número do Pedido Compra na tela de Histórico de Movimentos
def insereNumeroPedComp():
    #Abre o Menu Principal    
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho >> Menu Superior > Histórico
    pyautogui.hotkey('shift','f8')
    time.sleep(10)
    #Digita no campo Classe do Mov. = "pedido compra"
    pyautogui.write("pedido compra")
    #Faz a verificação se o Pedido Compra está selecionado
    while pyautogui.locateOnScreen(rf"{path}\hist_mov_class_mov_ped_comp.png", confidence=0.9) == False:
        pyautogui.press('down')
        time.sleep(2)
    else:
        pyautogui.press('enter')
        print("Encontrou a classe Pedido Compra e clicou ENTER")
        time.sleep(2)
        
    time.sleep(5)
    '''#Aperta a tecla enter
    pyautogui.press('enter')
    time.sleep(2)
    #Insere a data = 01/01/2019
    pyautogui.write("010119")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)'''
    #Aperta tab 11 vezes até o campo Nº Documento
    pyautogui.press('tab', presses=12)
    time.sleep(5)
    #Maximiza o txt do número do Pedido Compra
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-COMPRA.txt - Bloco de Notas")[0].maximize()
    #Seleciona o Campo Nº do Pedido Compra
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'shiftright','home')
    time.sleep(2)
    #Copia o Nº do Pedido Compra
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-PEDIDO-COMPRA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #Cola o Nº do Pedido Compra do txt no Histórico de Movimentos
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
#=================================================================================================
#Método Concluir Pedido Compra
#Implementado - Fernando 13/05/2022
def concluirPedComp():
        #Mensagem de rentabilidade
    if pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9):
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
        time.sleep(5)
        #Clica no botão Concluir
        btn_concluir_ped_compra = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_compra.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_compra)
    else:
        #Clica no botão Concluir
        time.sleep(5)
        btn_concluir_ped_compra = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_compra.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_compra)
        time.sleep(2)
        #Mensagem de parcelamento
        if pyautogui.locateOnScreen(rf"{path}\msg_parc_ped_comp.png", confidence=0.9):
            time.sleep(2)
            #Clica no botão sim para concluir o movimento
            pyautogui.press('enter')
            msgParcelamentoPedComp()
        else:
            #Espera 15s    
            time.sleep(15)
            #Implementado - Fernando 10/12/2021
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
#Método aba Parcelas
#Implementado - Fernando 13/05/2022
def msgParcelamentoPedComp():
    if pyautogui.locateOnScreen(rf"{path}\cad_ped_comp_aba_parc.png", confidence=0.9):
        aba_parc = pyautogui.locateOnScreen(rf"{path}\cad_ped_comp_aba_parc.png", confidence=0.9)
        pyautogui.click(aba_parc)      
        
        # Criando objeto com data atual adcionando 1 mes.
        dataatual = datetime.now() + relativedelta(months=1)
        # Convertendo no formato desejado DDMMYY.
        data1mes = int(dataatual.strftime('%d%m%y'))
        time.sleep(2)
        #desabilita bit parcelamento automatico
        if pyautogui.locateOnScreen(rf"{path}\bit_parc_auto_ped_comp.png", confidence=0.9):
            bit_parc = pyautogui.locateOnScreen(rf"{path}\bit_parc_auto_ped_comp.png")
            time.sleep(2)
            pyautogui.click(bit_parc)
            time.sleep(2)
            #Localiza na tela o campo Vencimento
            camp_vencto = pyautogui.locateOnScreen(rf"{path}\campo_vencto_ped_compra.png", confidence=0.9)
            time.sleep(2)
            pyautogui.click(camp_vencto)
            #Cola o Nº do Pedido no txt
            time.sleep(2)
            pyautogui.write(str(data1mes))
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.write("10")
            pyautogui.press('enter')
            time.sleep(2)
            #Salva o parcelamento clicando no lápis
            btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
            pyautogui.click(btn_lapis)
            concluirPedComp()

#=================================================================================================

#Implementado - Fernando 17/05/2022

def imppedsaida():
    time.sleep(5)
    #Clica na aba Imposto
    aba_imp = pyautogui.locateOnScreen(rf"{path}\cad_ped_comp_aba_imp.png", confidence=0.9)
    pyautogui.click(aba_imp)
    print("Selecionada aba Imposto")
    time.sleep(5)
    if pyautogui.locateOnScreen(rf"{path}\chk_imp_ICM_0.png", confidence=0.9):
        chk_imp_ICM = pyautogui.locateOnScreen(rf"{path}\chk_imp_ICM_0.png", confidence=0.9)
        pyautogui.click(chk_imp_ICM)
        time.sleep(15)
        time.sleep(5)
    elif pyautogui.locateOnScreen(rf"{path}\chk_imp_ICM_1.png", confidence=0.9):
        chk_imp_ICM = pyautogui.locateOnScreen(rf"{path}\chk_imp_ICM_1.png", confidence=0.9)
        pyautogui.click(chk_imp_ICM)
        time.sleep(15)
        pyautogui.click()
        time.sleep(10)
    
    #Selecionar o bit ICM Itens
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(10)
    #Clicar no bit Não Tributa Pis /Cofins
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(10)
    #Desmarcar o bit IPI e Marcar novamente o campo o bit IPI;
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.press('space')
    time.sleep(10)
    #Marcar e desmarcar o bit Calcular IPI sobre Frete
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.press('space')
    time.sleep(10)
    #Marcar e desmarcar o bit Somar FCP ST no total documento
    chk_FCP_total_doc = pyautogui.locateOnScreen(rf"{path}\chk_imp_FCP_total_doc.png")
    pyautogui.click(chk_FCP_total_doc)
    time.sleep(10)
    pyautogui.click()
    time.sleep(10)
    #Clicar no botão Impostos ICMS e ICMS ST
    btn_imp_ICMS = pyautogui.locateOnScreen(rf"{path}\btn_imp_ICMS.png")
    pyautogui.click(btn_imp_ICMS)
    time.sleep(10)
    #Marcar o primeiro Bit Alterar Impostos
    pyautogui.press('right', presses=6)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(2)
    #Marcar o bit Alterar Valores Manual
    pyautogui.press('right', presses=4)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(2)
    #Marcar o segundo bit Alterar Valores Manual
    pyautogui.press('right', presses=7)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    #Clicar no botão Fechar
    pyautogui.hotkey('alt','f')
    time.sleep(5)
    #Clicar no botão Impostos II e IPI
    btn_II_IPI = pyautogui.locateOnScreen(rf"{path}\btn_imp_II_IPI.png")
    pyautogui.click(btn_II_IPI)
    time.sleep(2)
    #Clicar no bit Alterar Imposto Manual
    pyautogui.press('right', presses=10)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    #Clicar no botão Fechar
    pyautogui.hotkey('alt','f')
    time.sleep(3)
    #Clicar no botão Impostos PIS e COFINS
    btn_PIS_COFINS = pyautogui.locateOnScreen(rf"{path}\btn_imp_PIS_COFINS.png")
    pyautogui.click(btn_PIS_COFINS)
    time.sleep(2)
    #Clicar no bit Alterar Imposto Manual
    pyautogui.press('right', presses=8)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(2)
    #Clicar no botão Fechar
    pyautogui.hotkey('alt','f')
    time.sleep(5)
    
#=================================================================================================

#Implementado - Fernando 17/05/2022

#Método para salvar o número do Movimento de Compra em um txt
def salvaNumeroCompEnt():
    #Seleciona o Campo Nº do Movimento
    time.sleep(5)
    #Copia o Nº do Movimento
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
    #Cola o Nº do Movimento no txt
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    #Salva o txt como NUMERO-COMPRA
    pyautogui.hotkey('ctrl','s')
    time.sleep(2)
    pyautogui.write("NUMERO-COMPRA-ENTRADA")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("NUMERO-COMPRA-ENTRADA.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)