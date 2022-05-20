from maximiza_fecha import *
from metodos_venda_saida import *
from login_ouro import *
import pyautogui
import time


#Fernando 26/11/2021
#Caminho da pasta em uma variável

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Método implementado - Renan 17/01/2022
def conferenciaPedVenda():
    #Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl','1')
    time.sleep(15)
    #Seleciona >> Venda / Saída
    menu_venda_saida = pyautogui.locateOnScreen(rf"{path}\menu_venda_saida.png", confidence=0.9)
    pyautogui.click(menu_venda_saida)
    time.sleep(5)
    #Seleciona > Venda / Saída > Conferência do Pedido de Saída
    menu_venda_saida_conf_ped_said = pyautogui.locateOnScreen(rf"{path}\menu_venda_saida_conf_ped_said.png", confidence=0.9)
    pyautogui.click(menu_venda_saida_conf_ped_said)
    time.sleep(20)   
    #Seleciona o campo Pedidos
    conf_ped_said_campo_pedidos = pyautogui.locateOnScreen(rf"{path}\conf_ped_said_campo_pedidos.png", confidence=0.9)
    pyautogui.click(conf_ped_said_campo_pedidos)
    time.sleep(5)
    #Aperta a tecla END
    pyautogui.press('end')
    time.sleep(2)
    #Seleciona o texto que estiver no campo
    pyautogui.hotkey('shiftleft','shiftright','home')
    time.sleep(2)
    #Apaga o texto que estiver no campo
    pyautogui.press('backspace')
    time.sleep(2)
    #Digita no campo (Pedidos) PEDIDO DE VENDA
    pyautogui.write("PEDIDO DE VENDA")
    time.sleep(10)
    #Aperta enter 2x até ao campo do separador
    pyautogui.press('enter', presses=2)
    time.sleep(5)
    #Apaga o campo separador
    pyautogui.press('backspace')
    time.sleep(5)
    #Aperta f11 para retornar a mensagem de selecionar um valor válido no campo separador
    pyautogui.press('f11')
    #Verifica a mensagem para selecionar um Valor válido da Lista
    time.sleep(15)
    if pyautogui.locateOnScreen(rf"{path}\msg_esc_val_list.png", confidence=0.9):
        time.sleep(5)
        #Aperta enter para a mensagem de Escolher um Valor Válido da lista
        pyautogui.press('enter')
        time.sleep(5)
        #Aperta seta para baixo para selecionar um separador
        pyautogui.press('down')
        time.sleep(5)
        #Aperta a tecla Enter para colocar o separador
        pyautogui.press('enter')
    else:
        print("Atenção! Não foi possível selecionar o separador.Verifique o erro em tela")
        time.sleep(2)
    time.sleep(5)    
    #Seleciona o campo Nº Pedido
    pyautogui.press('up',presses=2)
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
    #Cola o Nº do Pedido Venda do txt na tela de Conferência de Pedido de Saída
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
    #Clica no Raio para carregar o pedido venda para conferência
    btn_raio_conf_ped_said = pyautogui.locateOnScreen(rf"{path}\btn_raio_conf_ped_said.png", confidence=0.9)
    pyautogui.click(btn_raio_conf_ped_said)
    time.sleep(20)
    #Clica no botão Carregar com Senha
    conf_ped_said_carreg_com_senh = pyautogui.locateOnScreen(rf"{path}\conf_ped_said_carreg_com_senh.png", confidence=0.9)
    pyautogui.click(conf_ped_said_carreg_com_senh)
    time.sleep(15)
    #Verifica se foi apresentado a mensagem de Senha para Liberação da Edição
    if pyautogui.locateOnScreen(rf"{path}\conf_ped_said_senh_p_lib_edi.png", confidence=0.9):
        time.sleep(5)
        #Chama o método loginOuro
        loginOuro()
        print("Fez o login com o Usuário e Senha")
    else:
        print("Não foi possível carregar os dados, verifique o erro em tela")
    time.sleep(15)
    #Verifica a mensagem (Digite a Mensagem da Ocorrência)
    if  pyautogui.locateOnScreen(rf"{path}\msg_para_conf_ped_said.png", confidence=0.9):
        time.sleep(5)
        pyautogui.write("MENSAGEM DE CONFERENCIA DE TESTE 0001")
        time.sleep(10)
        #Clica no botão OK
        btn_ok = pyautogui.locateOnScreen(rf"{path}\btn_ok.png", confidence=0.9)
        pyautogui.click(btn_ok)
        time.sleep(5)
        print("Escreceu a mensagem e clicou no botão OK")
    else:
        print("Não teve mensagem da ocorrência na conferência do pedido de saída! Verifique o erro em tela.")
    time.sleep(15)
    #Verifica o campo do volume = 0
    if pyautogui.locateOnScreen(rf"{path}\conf_ped_said_campo_vol.png", confidence=0.9):
        time.sleep(5)
        #Clica no campo do Volume = 0
        conf_ped_said_campo_vol = pyautogui.locateOnScreen(rf"{path}\conf_ped_said_campo_vol.png", confidence=0.9)
        pyautogui.click(conf_ped_said_campo_vol)
        time.sleep(2)
        #Aperta a tecla END
        pyautogui.press('end')
        time.sleep(2)
        #Seleciona o volume
        pyautogui.hotkey('shiftleft', 'shiftright','home')
        time.sleep(2)
        #Apaga o volume
        pyautogui.press('backspace')
        time.sleep(5)
        #Coloca o Volume = 1
        pyautogui.write("1")
        time.sleep(2)
        #Clica no botão Confere
        btn_confere = pyautogui.locateOnScreen(rf"{path}\btn_confere.png", confidence=0.9)
        pyautogui.click(btn_confere)
        time.sleep(15)
    else:
        print("Não achou o volume = 0")
        #Clica no botão Confere
        btn_confere = pyautogui.locateOnScreen(rf"{path}\btn_confere.png", confidence=0.9)
        pyautogui.click(btn_confere)
        time.sleep(15)
    time.sleep(15)
    #Verifica a mensagem de imprimir etiqueta
    if pyautogui.locateOnScreen(rf"{path}\msg_desej_imp_etiq.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('n')
    else:
        print("Não teve mensagem de imprimir etiqueta! Verifique o erro em tela.")
    time.sleep(15)
    #Verifica mensagem de concluir conferência
    if pyautogui.locateOnScreen(rf"{path}\msg_desej_concl_conf.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('s')
    else:
        print("Não teve mensagem de concluir a conferência! Verifique o erro em tela.")
    time.sleep(15)
    #Verifica mensagem de imprimir relatório
    if pyautogui.locateOnScreen(rf"{path}\msg_desej_imp_rel.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('n')
    else:
        print("Não teve mensagem de imprimir relatório! Verifique o erro em tela.")
    time.sleep(5)
    #Clica no botão X para fechar a tela que está aberta
    fechaTela()