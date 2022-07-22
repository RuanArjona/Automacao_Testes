import pyautogui
from time import sleep

path = r"\\VM-SRVFILE01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img"
path_pmm = r"\\VM-SRVFILE01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img\pesq_mov_menu"

def copy_emp_padrao():
    sleep(1)
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('Ctrl', '1')
    sleep(10)
    # Localiza e clica no botão "Segurança"(Menu superior > Segurança) 
    menu_sup_seg = pyautogui.locateOnScreen(rf"{path}\menu_sup_seg.png")
    sleep(0.5)
    pyautogui.click(menu_sup_seg)
    sleep(1)
    # Localiza e clica no botão "Altera Empresa Padrão"
    # (Menu superior > Segurança > Altera Empresa Padrão)
    menu_sup_seg_alt_emp_padrao = pyautogui.locateOnScreen(rf"{path}\menu_sup_seg_alt_emp_padrao.png")
    sleep(0.5)
    pyautogui.click(menu_sup_seg_alt_emp_padrao)
    sleep(1)
    # Copia o que estiver preenchido no campo "Qual Empresa Padrão:" na tela
    # "Empresa Padrão"(Menu superior > Segurança > Altera Empresa Padrão)
    pyautogui.hotkey("ctrl", "c")
    sleep(1)
    # Localiza e clica no botão "Cancelar" da tela "Empresa Padrão"
    # (Menu superior > Segurança > Altera Empresa Padrão)
    btn_cancel = pyautogui.locateOnScreen(rf"{path_pmm}\btn_cancel.png")
    sleep(1)
    pyautogui.click(btn_cancel)
    sleep(1)

    
def pesq_mov_menu():
    # Selecionar a janela do Menu Principal dentro do Ouro
    pyautogui.hotkey('Ctrl', '1')
    sleep(10)
    # Localiza e clica no botão "Tabela"(Menu superior > Tabela)
    menu_sup_tab = pyautogui.locateOnScreen(rf"{path}\menu_sup_tab.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_sup_tab)
    sleep(1)
    # Localiza e clica no botão "Produto"(Menu superior > Tabela > Produto)
    menu_sup_tab_product = pyautogui.locateOnScreen(rf"{path_pmm}\menu_sup_tab_prod.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_sup_tab_product)
    sleep(1)
    # Localiza e clica no botão "Tipos de Movimento de Estoque"
    # (Menu superior > Tabela > Produto > Tipos de Movimento de Estoque)
    menu_sup_tab_prod_tip_mov_estoq = pyautogui.locateOnScreen(rf"{path_pmm}\menu_sup_tab_prod_tip_mov_estoq.png",
                                                               confidence=0.9)
    sleep(0.5)
    pyautogui.click(menu_sup_tab_prod_tip_mov_estoq)
    sleep(15)
    # Localiza e clica no botão "Filtrar" da tela "Cadastro de Tipos de Movimento de Estoque"
    # (Menu superior > Tabela > Produto > Tipos de Movimento de Estoque)
    btn_filtro = pyautogui.locateOnScreen(rf"{path_pmm}\btn_filtrar.png", confidence=0.9)
    sleep(0.5)
    pyautogui.click(btn_filtro)
    sleep(10)
    # Localiza e clica na aba "Filtro"
    aba_filtro = pyautogui.locateOnScreen(rf"{path}\btn_aba_filtro.png")
    sleep(0.5)
    pyautogui.click(aba_filtro)
    sleep(1)
    # Localiza e clica no botão "Remover Filtro"
    remove_filtro = pyautogui.locateOnScreen(rf"{path}\remove_filtro.png")
    sleep(0.5)
    pyautogui.click(remove_filtro)
    sleep(1)
    # Pressiona "Tab" 3x para chegar no campo "Empresa"
    pyautogui.press('tab', presses=3)
    sleep(0.5)
    # Cola o que foi copiado na tela "Empresa Padrão"(Menu superior > Segurança > Altera Empresa Padrão)
    pyautogui.hotkey("ctrl", "v")
    sleep(2)
    # Clica na seta para baixo para selecionar a empresa
    pyautogui.press("down")
    sleep(1)
    # Pressionaa enter para confirmar a seleção
    pyautogui.press('enter')
    sleep(1)
    # Localiza o bit "Ativo: " desmarcado da tela "Cadastro de Tipos de Movimento de Estoque"
    # (Menu superior > Tabela > Produto > Tipos de Movimento de Estoque)
    btn_ativ_off = pyautogui.locateOnScreen(rf"{path_pmm}\btn_atv_off_cad_tip_mov.png", confidence=0.9)
    sleep(0.5)
    # Verifica se o bit "Ativo" está marcado
    # Se o bit Ativo estiver desmarcado
    if btn_ativ_off:
        # Clica no bit para marcar
        pyautogui.click(btn_ativ_off)
        sleep(0.5)
        # Clica no botão "Filtrar"
        pyautogui.click(btn_filtro)
    # Se bit "Ativo: " já estiver marcado
    else:
        sleep(0.5)
        # Clica no botão "Filtrar"
        pyautogui.click(btn_filtro)
    sleep(25)
    # Localiza o campo "Empresa Padrão" com a empresa selecionada
    emp_padrao = pyautogui.locateOnScreen(rf"{path_pmm}\emp_padrao.png", confidence=0.9)
    sleep(2)
    contador = 0
    # Looping feito para pressionar a seta "para baixo" para que se verifique nos movimentos: 
    # Se a Empresa Padrão condiz com a imagem localizada e verifica se o bit "Ativo" da aba Configurações está marcada
    while contador <= 4:
        if emp_padrao:
            print('O movimento pertence a empresa padrão!')
            # Localiza e clica na aba "Configurações"
            aba_config = pyautogui.locateOnScreen(rf"{path_pmm}\aba_config_cad_tip_mov_estoq.png", confidence=0.9)
            sleep(2)
            pyautogui.click(aba_config)
            sleep(5)
            # Localiza o bit "Ativo"
            bit_ativo = pyautogui.locateOnScreen(rf"{path_pmm}\bit_ativ_config.png", confidence=0.9)
            sleep(0.5)
            # Verifica se o bit "Ativo" está marcado
            if bit_ativo:
                print('O bit "Ativo" está marcado!')
            else:
                print('O bit "Ativo" está desmarcado!')
            # Localiza e clica na aba "Principal"
            aba_principal = pyautogui.locateOnScreen(rf"{path_pmm}\aba_prin_cad_tip_mov_estoq.png", confidence=0.9)
            sleep(0.5)
            pyautogui.click(aba_principal)
            sleep(5)
            # Localiza e clica no quadrado azul ao lado de código da tabela
            btn_tst = pyautogui.locateOnScreen(rf"{path_pmm}\bloco_azul.png", confidence=0.9)
            sleep(0.5)
            pyautogui.click(btn_tst)
            sleep(2)
            # Pressiona a seta "para baixo"
            pyautogui.press("down")
            sleep(5)
            contador += 1
        else:
            print('O movimento não pertence a empresa padrão!')
            contador += 1


