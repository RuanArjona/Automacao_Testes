from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 05/01/2022
def cadastroPedVendaSimples():
    #Selecionar a janela do Menu Principal dentro do Ouro
    #Implementado - Fernando 11/01/2022
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Atalho Controle Estoque
    pyautogui.hotkey('ctrl','f11')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(20)
    #Aperta tab 12 vezes para escrever Saldo Disp
    pyautogui.press('tab', presses=12)
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.hotkey('shiftleft','shiftright','home')
    time.sleep(2)
    pyautogui.press('backspace')
    time.sleep(2)
    #Digita no campo Valor Saldo: Saldo Disp
    pyautogui.write("Saldo Disp")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    #Clicar na coluna Saldo Disponível
    con_est_sld_disp = pyautogui.locateOnScreen(rf"{path}\con_est_sld_disp.png", confidence=0.9)
    pyautogui.click(con_est_sld_disp)
    time.sleep(5)
    pyautogui.click(con_est_sld_disp)
    time.sleep(5)
    #comando ctrl + c para salvar o código do produto
    pyautogui.hotkey('shift','tab')
    time.sleep(2)
    pyautogui.hotkey('shift','tab')
    time.sleep(5)
    #Copia o código do Produto
    pyautogui.hotkey('ctrlleft','ctrlright','c')
    time.sleep(10)
    time.sleep(5)
    #Colocar txt aqui
    #Abre o windows + r
    pyautogui.hotkey('win','r')
    time.sleep(5)
    #Escreve notepad e aperta enter
    pyautogui.write("notepad")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    #Cola o Nº do Pedido no txt
    pyautogui.hotkey('ctrlleft','ctrlright','v')
    time.sleep(5)
    #Salva o txt como Código do Produto a ser Utilizado
    pyautogui.hotkey('ctrl','s')
    time.sleep(5)
    pyautogui.write("CODIGO-PRODUTO")
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(10)
    #Minimiza o txt
    pyautogui.getWindowsWithTitle("CODIGO-PRODUTO.txt - Bloco de Notas")[0].minimize()
    time.sleep(5)
    #colocar o comando alt + f4 para fechar a tela do ouro ou colocar o alt + space
    pyautogui.hotkey('alt','f4')
    time.sleep(10)
    #==================================================================================================

    #Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Seleciona >> Venda / Saída
    menu_venda_saida = pyautogui.locateOnScreen(rf"{path}\menu_venda_saida.png", confidence=0.9)
    pyautogui.click(menu_venda_saida)
    time.sleep(5)
    #Seleciona >> Venda / Saída > Pedido de Venda Simples
    menu_venda_saida_ped_sai_simp = pyautogui.locateOnScreen(rf"{path}\menu_venda_saida_ped_sai_simp.png", confidence=0.9)
    pyautogui.click(menu_venda_saida_ped_sai_simp)
    time.sleep(15)
    #Clica no botão para maximizar a janela
    maximizaTela()
    #Espera 5s
    time.sleep(5)
    #Seleciona o campo do cliente
    cad_ped_vend_simp_cliente = pyautogui.locateOnScreen(rf"{path}\cad_ped_vend_simp_cliente.png", confidence=0.9)
    pyautogui.click(cad_ped_vend_simp_cliente)
    time.sleep(5)
    #Insere um clinte
    #cliente na MILFARMA
    pyautogui.write("00000002")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)
    #Seleciona o campo Código do Item no Pedido de Venda Simples
    time.sleep(5)
    #Seleciona o campo Nº Doc
    pyautogui.press('tab', presses=2)
    time.sleep(10)
    #Chama o método para gravar o Nº Doc no txt
    salvaNumeroPedVendSimp()
    #Implementação - Fernado 12/01/2022
    #Clica no campo Vendedor caso haja
    time.sleep(5)
    if pyautogui.locateOnScreen(rf"{path}\campo_vend_ped_saida_simp.png", confidence=0.9):
        #Clica no campo Vendedor
        time.sleep(5)
        campo_vend_ped_saida_simp = pyautogui.locateOnScreen(rf"{path}\campo_vend_ped_saida_simp.png", confidence=0.9)
        time.sleep(10)
        pyautogui.click(campo_vend_ped_saida_simp)
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        #Seleciona o campo Código do Produto
        pyautogui.press('tab',presses=5)
    else:
        time.sleep(5)
        pyautogui.press('tab',presses=7)
    #Implementado - Fernando 11/01/2022
    #Insere o Código do Produto com saldo
    time.sleep(15)
    #Maximiza o txt do CODIGO-PRODUTO
    pyautogui.getWindowsWithTitle("CODIGO-PRODUTO.txt - Bloco de Notas")[0].maximize()
    time.sleep(5)
    #Aperta a tecla end
    pyautogui.press('end')
    time.sleep(2)
    #Seleciona o código do produto
    pyautogui.hotkey('shiftleft','shiftright','home')
    time.sleep(5)
    #Copia o código do produto
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(5)
    #MInimiza o TXT
    pyautogui.getWindowsWithTitle("CODIGO-PRODUTO.txt - Bloco de Notas")[0].minimize()
    time.sleep(10)
    #Cola o Código do Produto no campo código > Pedido de Saída Simples
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    #Aperta enter para inserir o produto na tela
    pyautogui.press('enter')
    #====================================BKP DO CÓDIGO AQUI==============================================#
    time.sleep(5)
    #Salva o produto clicando no lápis
    btn_lapis = pyautogui.locateOnScreen(rf"{path}\btn_lapis.png", confidence=0.9)
    pyautogui.click(btn_lapis)
    time.sleep(10)
    #Fernando
    #selecionar o vendedor

    #Implementado - Renan 10/12/2021
    #Mensagem de rentabilidade
    if pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9):
        #Clica no botão OK para a mensagem de rentabilidade
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_ok)
        time.sleep(5)
        #Clica no botão Concluir
        btn_concluir_ped_venda_simples = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_venda_simples.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_venda_simples)
    else:
        #Clica no botão Concluir
        time.sleep(5)
        btn_concluir_ped_venda_simples = pyautogui.locateOnScreen(rf"{path}\btn_concluir_ped_venda_simples.png", confidence=0.9)
        time.sleep(2)
        pyautogui.click(btn_concluir_ped_venda_simples)
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
        time.sleep(10)
    #Clica no botão sim para concluir o movimento
        btn_sim = pyautogui.locateOnScreen(rf"{path}\btn_sim.png", confidence=0.9)
        pyautogui.click(btn_sim)
        time.sleep(5)
        print("Clicou no botão 'sim' para concluir o movimento")
        time.sleep(10)
    #Clica para não imprimir o movimento    
        btn_nao_imp_mov = pyautogui.locateOnScreen(rf"{path}\btn_nao_imp_mov.png", confidence=0.9)
        pyautogui.click(btn_nao_imp_mov)
        time.sleep(5)
        print("Clicou no botão 'não' para não imprimir o documento")
    else:
        print("Não teve mensagem de confirmação do movimento, verifique o erro!")
  
    #Implementado 06/01/2022
    time.sleep(5)
    #Clica no botão X para fechar a tela que está aberta
    fechaTela()
    