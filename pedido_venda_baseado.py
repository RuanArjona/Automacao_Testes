from maximiza_fecha import *
from metodos_venda_saida import *
import pyautogui
from time import sleep

# Fernando 26/11/2021
# Caminho da pasta das imagens e documentos
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
path2 = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\doc"

# Método implementado - Renan 08/12/2021
def pedVendBaseado():
    # Selecionar a janela do Ouro Web
    pyautogui.hotkey('ctrl', '1')
    sleep(5)
    # Abre a janela "Pedido de Saída"
    pyautogui.hotkey('ctrl', 'p')
    sleep(20)
    # Método para maximizar a janela
    maximizaTela()
    sleep(10)
    # Localiza e clica no campo "Baseado"
    nmr_ped_vend_baseado = pyautogui.locateOnScreen(rf"{path}\nmr_ped_vend_baseado.png", confidence=0.9)
    sleep(2)
    pyautogui.click(nmr_ped_vend_baseado)
    sleep(5)
    # Locaiza arquivo "NUMERO-PEDIDO-VENDA.txt" em modo leitura
    with open(rf"{path2}\ NUMERO-PEDIDO-VENDA.txt", 'r', encoding="utf8") as ler_str:
        # Le todas as linhas do arquivo uma a uma
        line = ler_str.read()
        sleep(5)
        # Escreve no campo e pressiona a tecla "Enter"
        pyautogui.write(line)
    sleep(10)
    # Aperta a tecla enter para carregar o pedido venda baseado
    pyautogui.press('enter')
    sleep(30)
    # Chama o método concluirPedVend para concluir o Pedido Venda
    sleep(10)
    # Implementado 06/01/2022
    concluirPedVend()
    sleep(5)
    # Chama o método fechaTela para fechar a tela de Pedido Venda
    fechaTela()