import pyautogui
from time import sleep

# Caminho da pasta das imagens
path = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
path2 = rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\doc"
# Implementado - Ruan 23/05/2022


def consulProduAtiv():
    sleep(2)
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('ctrl', '1')
    sleep(10)
    # Localiza e clica no botão "Cadastro"
    mn_btn_cad = pyautogui.locateOnScreen(rf"{path}\menu_cadastro.png")
    pyautogui.click(mn_btn_cad)
    sleep(2)
    # Localiza e clica no botão "Produto"
    mn_btn_cad_prod = pyautogui.locateOnScreen(rf"{path}\menu_cadastro_prod.png")
    pyautogui.click(mn_btn_cad_prod)
    sleep(30)
    # Localiza e clica no botão "Ativo" existente na aba "Classificação"
    btn_ativ_cad_prod = pyautogui.locateOnScreen(rf"{path}\btn_ativo_cad_produc.png")
    pyautogui.click(btn_ativ_cad_prod)
    sleep(2)
    # Localiza e clica no botão "Apenas saldo positivo" existente na aba "Relaciona"
    btn_saldo_true = pyautogui.locateOnScreen(rf"{path}\btn_saldo_true.png")
    pyautogui.click(btn_saldo_true)
    sleep(2)
    # Localiza e clica no botão "Filtrar"
    btn_filtrar = pyautogui.locateOnScreen(rf"{path}\btn_filtrar.png")
    pyautogui.click(btn_filtrar)
    sleep(30)
    # Pressiona a tecal "Tab"
    pyautogui.press('tab')
    sleep(1)
    # Pressiona as teclas "Ctrl" + "C" para copiar
    pyautogui.hotkey("ctrl", "c")
    sleep(3)
    # Abre o windows + r
    pyautogui.hotkey('win', 'r')
    sleep(5)
    # Escreve notepad e aperta enter
    pyautogui.write("notepad")
    sleep(2)
    pyautogui.press('enter')
    sleep(5)
    # Cola e salva o arquivo Txt
    pyautogui.hotkey("ctrl", "v")
    sleep(2)
    pyautogui.hotkey("ctrl", "s")
    sleep(5)
    # Nome do arquivo txt e clica em confirmar
    pyautogui.write("DESCRICAO-PRODUTO")
    sleep(5)
    pyautogui.press('enter')
    sleep(10)
    # Minimiza o txt
    pyautogui.getWindowsWithTitle("DESCRICAO-PRODUTO.txt - Bloco de Notas")[0].minimize()
    sleep(5)
    ''' erro -> Caso seja encontrado "DESCONTINUADO" e/ou "INATIVO"
     será considerado Verdadeiro já que enquanto achar o loop continua '''
    erro = True
    while erro is True:
        # Abre o arquivo DESCRICAO-PRODUTO.txt em modo leitura com codificação UTF-8
        with open(rf"{path2}\DESCRICAO-PRODUTO.txt", 'r', encoding="utf8") as ler_str:
            # Ler todas as linhas do arquivo uma a uma
            for line in ler_str:
                print(line)
                # Para cada linha, verifique se a linha contém a string
                if "DESCONTINUADO" in line:
                    print("Descontinuado localizado!")
                    # Pressiona o botão "Seta para baixo"
                    pyautogui.hotkey("down")
                    sleep(2)
                    # pressiona os botões "Ctrl" + "C" para copiar descrição do produto da tabela
                    pyautogui.hotkey("ctrl", "c")
                    sleep(3)
                    # Maximiza tela do arquivo txt
                    pyautogui.getWindowsWithTitle("DESCRICAO-PRODUTO.txt - Bloco de Notas")[0].maximize()
                    sleep(5)
                    # Pressiona Ctrl + a para selecionar tudo
                    pyautogui.hotkey("ctrl", "a")
                    sleep(1)
                    # Cola o que estiver no "Ctrl" + "C"
                    pyautogui.hotkey("ctrl", "v")
                    sleep(2)
                    # Salva arquivo txt
                    pyautogui.hotkey("ctrl", "s")
                    sleep(2)
                    # Minimiza arquivo txt
                    pyautogui.getWindowsWithTitle("DESCRICAO-PRODUTO.txt - Bloco de Notas")[0].minimize()
                    sleep(5)

                    erro = True
                elif "INATIVO" in line:
                    print("Inativo localizado!")
                    # Pressiona o botão "Seta para baixo"
                    pyautogui.hotkey("down")
                    sleep(2)
                    # pressiona os botões "Ctrl" + "C" para copiar descrição do produto da tabela
                    pyautogui.hotkey("ctrl", "c")
                    sleep(3)
                    # Maximiza tela do arquivo txt
                    pyautogui.getWindowsWithTitle("DESCRICAO-PRODUTO.txt - Bloco de Notas")[0].maximize()
                    sleep(5)
                    # Pressiona Ctrl + a para selecionar tudo
                    pyautogui.hotkey("ctrl", "a")
                    sleep(1)
                    # Cola o que estiver no "Ctrl" + "C"
                    pyautogui.hotkey("ctrl", "v")
                    sleep(2)
                    # Salva arquivo txt
                    pyautogui.hotkey("ctrl", "s")
                    sleep(2)
                    # Minimiza arquivo txt
                    pyautogui.getWindowsWithTitle("DESCRICAO-PRODUTO.txt - Bloco de Notas")[0].minimize()
                    sleep(5)

                    erro = True
                else:
                    print('Inativo e descontinuado não encontrado! \nProduto Ativo!')
                    sleep(2)
                    # Fecha a tela de Tabela de Cadastro Produto
                    pyautogui.hotkey('alt', 'F4')
                    erro = False

consulProduAtiv()


